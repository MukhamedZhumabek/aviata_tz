import sys

sys.path = ['', '..'] + sys.path[1:]

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from sqlalchemy import create_engine
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
from storage.base import BaseModel
target_metadata = BaseModel.metadata
from storage.models.providers import ProviderModel
from storage.models.search_data import SearchData
# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def get_url():
    from settings import DB_CREDENTIALS
    return f"postgresql://{DB_CREDENTIALS['POSTGRES_USER']}:{DB_CREDENTIALS['POSTGRES_PASSWORD']}@" \
           f"{DB_CREDENTIALS['POSTGRES_HOST']}:{DB_CREDENTIALS['POSTGRES_PORT']}/{DB_CREDENTIALS['POSTGRES_DB']}"


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=get_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    alembic_config = config.get_section(config.config_ini_section)
    # engine = engine_from_config(
    #     alembic_config, prefix='sqlalchemy.', poolclass=pool.NullPool)
    engine = create_engine(get_url())

    def include_object(object, name, type_, reflected, compare_to):
        if not reflected and object.info.get("skip_autogenerate", False):
            return False
        else:
            return True

    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        include_object=include_object,
        compare_type=True)

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
