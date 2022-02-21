from sqlalchemy import Table, Column, String, select, Boolean, Integer
from sqlalchemy.dialects.postgresql import JSONB

from storage.base import BaseModel


class SearchData(BaseModel):
    __tablename__ = "search_data"
    __table_args__ = {"extend_existing": True}
    search_data = Table(
        "search_data",
        BaseModel.metadata,
        Column("id", Integer, primary_key=True),
        Column("search_id", String(255), unique=True),
        Column("status", String(20), default="PENDING"),
        Column("data", JSONB, nullable=True, default={})
    )

    async def add_new_search(self, search_data: dict):
        query = (
            self.search_data.insert().values(**search_data)
        )
        await self.connection.fetchrow(query)
        return
