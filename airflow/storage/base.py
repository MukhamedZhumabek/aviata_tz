from typing import List

from asyncpg import Record
from sqlalchemy import MetaData, Column, func, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    metadata = MetaData()

    def __init__(self, connection):
        self.connection = connection

    @classmethod
    def records_to_dicts(cls, list_of_records: List[Record]) -> List[dict]:
        """
        Converting asyncpg raw objects [Record] to python [dict]
        :param list_of_records:
        :return: list of dicts
        """
        list_of_dicts = [dict(record) for record in list_of_records]
        return list_of_dicts