import asyncpgsa


async def init_db_pool(app, db_credentials: dict):
    db_pool = await asyncpgsa.create_pool(
        host=db_credentials["POSTGRES_HOST"],
        port=db_credentials["POSTGRES_PORT"],
        database=db_credentials["POSTGRES_DB"],
        user=db_credentials["POSTGRES_USER"],
        password=db_credentials["POSTGRES_PASSWORD"],
        min_size=1,
        max_size=db_credentials["DB_MAX_POOL_SIZE"]
    )

    app["db_pool"] = db_pool
