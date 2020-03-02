# coding: utf-8
from sqlalchemy import Column, DECIMAL, MetaData, String, TIMESTAMP, Table, text
#from sqlalchemy.dialects.mysql import DECIMAL, INTEGER
#from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()


t_rating_yield_curve = Table(
    'rating_yield_curve', metadata,
    Column('date', TIMESTAMP, nullable=False, server_default=text("current_timestamp()")),
    Column('currency', String(10), nullable=False, server_default=text("'USD'"), comment='幣別'),
    Column('rating', String(50), nullable=False, comment='信評等級'),
    Column('maturity', DECIMAL(8, 5), nullable=False),
    Column('ytm', DECIMAL(19, 16), nullable=False)
)
