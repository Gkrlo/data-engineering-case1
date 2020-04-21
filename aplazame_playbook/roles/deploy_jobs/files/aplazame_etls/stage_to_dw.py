import json
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from aplazame_etls.models.dw import DimMerchant, DimCountry,FactPayment

def get_engine():
    db_string = "postgresql+psycopg2://postgres:postgres@aplazame1.vm:5432/postgres"
    return create_engine(db_string)

def get_session():
    Session = sessionmaker(bind=get_engine())
    session = Session()
    return session

def countries_df():
    country_df = pd.read_sql("select distinct country_alpha3 as country_id, country_name as name from stage_payments",
                              con=get_engine().connect())
    return country_df

def merchants_df():
    merchant_df = pd.read_sql("""select distinct merchant_id, merchant_name as name, industry_code, industry_name 
                                 from stage_payments""",
                              con=get_engine().connect())
    return merchant_df

def fact_payment_df():
    merchant_df = pd.read_sql("""select payment_id, amount, total_interest, 
                                 country_alpha3 as country_id, merchant_id
                                 from stage_payments""",
                              con=get_engine().connect())
    return merchant_df

def store_dim_merchant(merchant_df):
    stage_payments = [DimMerchant(**merchant_dict)
                      for merchant_dict in merchant_df.to_dict(orient="record")]
    session = get_session()
    session.add_all(stage_payments)
    session.commit()

def store_dim_countries(countries_df):
    stage_prepayments = [DimCountry(**country_dict)
                         for country_dict in countries_df.to_dict(orient="record")]
    session = get_session()
    session.add_all(stage_prepayments)
    session.commit()

def store_fact_payment(payment_df):
    stage_prepayments = [FactPayment(**payment_dict)
                         for payment_dict in payment_df.to_dict(orient="record")]
    session = get_session()
    session.add_all(stage_prepayments)
    session.commit()


if __name__ == '__main__':
    # Store Dim_Merchant
    store_dim_merchant(merchants_df())
    # Store Dim_Country
    store_dim_countries(countries_df())
    # Store Fact_Payment
    store_fact_payment(fact_payment_df())





