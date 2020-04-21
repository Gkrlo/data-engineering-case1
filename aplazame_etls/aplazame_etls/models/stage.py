from sqlalchemy import create_engine
from sqlalchemy import Column, String, Numeric, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


base = declarative_base()

class StagePayment(base):
    __tablename__ = 'stage_payments'
    payment_id = Column(String, primary_key=True)
    payment_principal = Column(Numeric, name="principal")
    payment_total_interest = Column(Numeric, name="total_interest")
    payment_amount = Column(Numeric, name="amount")
    payment_collected = Column(String, name="collected")
    payment_created = Column(String, name="created")
    order_id = Column(String)
    order_amount = Column(Numeric)
    order_created = Column(String)
    merchant_id = Column(String)
    merchant_name = Column(String)
    industry_code = Column(String)
    industry_name = Column(String)
    country_alpha3 = Column(String)
    country_name = Column(String)

    def __init__(self, payment_id, payment_principal, payment_total_interest,  payment_amount, payment_collected,
                 payment_created, order_id, order_amount, order_created, merchant_id, merchant_name, industry_code,
                 industry_name, country_alpha3, country_name):
        self.payment_id = payment_id
        self.payment_principal = payment_principal
        self.payment_total_interest = payment_total_interest
        self.payment_amount = payment_amount
        self.payment_collected = payment_collected
        self.payment_created = payment_created
        self.order_id = order_id
        self.order_amount = order_amount
        self.order_created = order_created
        self.merchant_id = merchant_id
        self.merchant_name = merchant_name
        self.industry_code = industry_code
        self.industry_name = industry_name
        self.country_alpha3 = country_alpha3
        self.country_name = country_name


class StagePrePayment(base):
    __tablename__ = 'stage_prepayments'
    surrogate_key = Column(Integer, primary_key=True, autoincrement="auto")
    prepayment_id = Column(Integer)
    prepayment_interest = Column(Numeric, name="interest")
    prepayment_principal_not_accrued = Column(Numeric, name="principal_not_accrued")
    prepayment_state = Column(String, name="p_state")
    prepayment_t2 = Column(String, name="t2")
    order_id = Column(String)
    order_amount = Column(Numeric)
    order_created = Column(String)
    merchant_id = Column(String)
    merchant_name = Column(String)
    industry_code = Column(String)
    industry_name = Column(String)
    country_alpha3 = Column(String)
    country_name = Column(String)

    def __init__(self, prepayment_id,  prepayment_interest, prepayment_principal_not_accrued, prepayment_state,
                 prepayment_t2, order_id, order_amount, order_created, merchant_id, merchant_name, industry_code,
                 industry_name, country_alpha3, country_name):
        self.prepayment_id = prepayment_id
        self.prepayment_interest = prepayment_interest
        self.prepayment_principal_not_accrued = prepayment_principal_not_accrued
        self.prepayment_state = prepayment_state
        self.prepayment_t2 = prepayment_t2
        self.order_id = order_id
        self.order_amount = order_amount
        self.order_created = order_created
        self.merchant_id = merchant_id
        self.merchant_name = merchant_name
        self.industry_code = industry_code
        self.industry_name = industry_name
        self.country_alpha3 = country_alpha3
        self.country_name = country_name

# class DimCountry(base):
#     __tablename__ = 'dim_countries'
#     alpha3 = Column(String, primary_key=True)
#     name = Column(String)
#
#
# class DimMerchant(base):
#     __tablename__ = 'dim_merchant'
#     id = Column(String, primary_key=True)
#     name = Column(String)
#     industry_code = Column(String)
#     industry_name = Column(String)

