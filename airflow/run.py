from asyncio import gather

from aiohttp import web, ClientSession
from settings import DB_CREDENTIALS
from storage.setup import init_db_pool
from urls import configure_routes


async def persistent_http_sessions(app):
    app['HTTP_SESSION'] = session1 = ClientSession()
    yield
    await gather(*[session1.close()])


async def initialize_application():
    app = web.Application()
    configure_routes(app)
    app.cleanup_ctx.append(persistent_http_sessions)
    await init_db_pool(app, DB_CREDENTIALS)
    return app


def get_application():
    app = initialize_application()
    return app


if __name__ == '__main__':
    app = get_application()
    web.run_app(app, port=8080)
