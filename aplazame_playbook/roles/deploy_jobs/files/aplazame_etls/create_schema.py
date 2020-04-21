from sqlalchemy import create_engine
from aplazame_etls.models.stage import base as stage_base
from aplazame_etls.models.dw import base as dw_base

def get_engine():
    db_string = "postgresql+psycopg2://postgres:postgres@aplazame1.vm:5432/postgres"
    return create_engine(db_string)

def create_stage_schema():
    stage_base.metadata.create_all(get_engine())

def create_dw_schema():
    dw_base.metadata.create_all(get_engine())


if __name__ == '__main__':
    create_stage_schema()
    create_dw_schema()
