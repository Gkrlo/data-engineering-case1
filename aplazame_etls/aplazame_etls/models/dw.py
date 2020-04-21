from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class DimCountry(base):
    __tablename__ = 'dim_countries'
    country_id = Column(String, name="country_id", primary_key=True)
    name = Column(String)

    def __init__(self,country_id, name):
        self.country_id = country_id
        self.name = name

class DimMerchant(base):
    __tablename__ = 'dim_merchants'
    merchant_id = Column(String, primary_key=True)
    name = Column(String)
    industry_code = Column(String)
    industry_name = Column(String)

    def __init__(self, merchant_id, name, industry_code, industry_name):
        self.merchant_id = merchant_id
        self.name = name
        self.industry_code = industry_code
        self.industry_name = industry_name

class FactPayment(base):
    __tablename__ = 'fact_payment'
    payment_id = Column(String, primary_key=True)
    country_id = Column(String, ForeignKey('dim_countries.country_id'), nullable=False)
    merchant_id = Column(String, ForeignKey('dim_merchants.merchant_id'), nullable=False)
    total_interest = Column(Numeric)
    amount = Column(Numeric)

    def __init__(self, payment_id, country_id, merchant_id, total_interest, amount):
        self.payment_id =payment_id
        self.country_id = country_id
        self.merchant_id = merchant_id
        self.total_interest = total_interest
        self.amount = amount




