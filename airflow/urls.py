from aiohttp.web import Application

from handlers.fetch_data_from_providers import fetch_providers_data
from handlers.get_serch_results import get_search_by_id


def configure_routes(app: Application):
    app.router.add_route("POST", "/search", fetch_providers_data)
    app.router.add_route("GET", "/search/{search_id}/{currency}", get_search_by_id)
