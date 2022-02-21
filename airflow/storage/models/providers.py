from sqlalchemy import Table, Column, String, select, Boolean, Integer
from sqlalchemy.dialects.postgresql import JSONB

from storage.base import BaseModel


class ProviderModel(BaseModel):
    __tablename__ = "provider"
    __table_args__ = {"extend_existing": True}

    providers = Table(
        "provider",
        BaseModel.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(255)),
        Column("url", String(500)),
        Column("content_type", String(100)),
        Column("containers", JSONB, nullable=True, default={}),
        Column("is_active", Boolean, default=True)
    )

    async def get_providers(self):
        query = select([ProviderModel.providers])\
            .where(ProviderModel.providers.c.is_active == True)
        providers = await self.connection.fetch(query)
        return self.records_to_dicts(providers) if providers else []
