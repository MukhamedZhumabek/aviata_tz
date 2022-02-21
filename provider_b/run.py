from aiohttp import web

from urls import configure_routes


def init_application():
    app = web.Application()
    configure_routes(app)
    return app


if __name__ == '__main__':
    app = init_application()
    web.run_app(app, port=8082)
