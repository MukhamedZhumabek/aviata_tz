from aiohttp.web import Application

from handlers.get_template_data import read_json_from_file


def configure_routes(app: Application):
    app.router.add_route("POST", "/search", read_json_from_file)

