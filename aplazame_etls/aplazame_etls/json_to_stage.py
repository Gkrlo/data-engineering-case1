import json
from pandas.io.json import json_normalize
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from aplazame_etls.models.stage import StagePayment, StagePrePayment

def get_engine():
    db_string = "postgresql+psycopg2://postgres:postgres@aplazame1.vm:5432/postgres"
    return create_engine(db_string)

def get_session():
    Session = sessionmaker(bind=get_engine())
    session = Session()
    return session

def load_json(file_path="/opt/aplazame_data/data_engineer_test.json"):
    with open(file_path) as json_file:
        return json.loads(json_file.read())

def payment_stage_df(json_data):
    payments_df = json_normalize(data=json_data,
                                 record_path=["capture_set", "instalment_plan_set", "payments"],
                                 record_prefix="payment_",
                                 meta=["merchant", "country", "id", "amount", "created"],
                                 meta_prefix="order_")
    return payments_df

def prepayment_stage_df(json_data):
    prepayments_df = json_normalize(data=json_data,
                                    record_path=["capture_set", "instalment_plan_set", "prepayments"],
                                    record_prefix="prepayment_",
                                    meta=["merchant", "country", "id", "amount", "created"],
                                    meta_prefix="order_")
    return prepayments_df

def flat_external_data(stage_dict: dict):
    merchant = stage_dict.pop("order_merchant")
    country = stage_dict.pop("order_country")
    stage_dict["merchant_id"] = merchant["id"],
    stage_dict["merchant_name"] = merchant["name"],
    stage_dict["industry_code"] = merchant["industry"]["code"],
    stage_dict["industry_name"] = merchant["industry"]["name"],
    stage_dict["country_alpha3"] = country["alpha3"],
    stage_dict["country_name"] = country["name"]
    return stage_dict


def store_stage_payments(payment_df):
    stage_payments = [StagePayment(**flat_external_data(payment_dict))
                      for payment_dict in payment_df.to_dict(orient="record")]
    session = get_session()
    session.add_all(stage_payments)
    session.commit()

def store_stage_prepayments(prepayment_df):
    stage_prepayments = [StagePrePayment(**flat_external_data(prepayment_dict))
                         for prepayment_dict in prepayment_df.to_dict(orient="record")]
    session = get_session()
    session.add_all(stage_prepayments)
    session.commit()


if __name__ == '__main__':
    # Store Payments
    payment_df = payment_stage_df(load_json())
    store_stage_payments(payment_df)

    # Store PrePayments
    prepayment_df = prepayment_stage_df(load_json())
    store_stage_prepayments(prepayment_df)


