from aiohttp.web import Request, json_response

from storage.models.providers import ProviderModel
from storage.models.search_data import SearchData


async def fetch_providers_data(request: Request):

    async with request.app["db_pool"].acquire() as connection:
        providers = await ProviderModel(connection).get_providers()
    search_result = []

    for provider in providers:
        async with request.app["HTTP_SESSION"].post(provider["url"], json=provider["containers"]) as response:
            json_response = await response.json(content_type=response.content_type)
            search_result.extend(json_response)

    async with request.app["db_pool"].transaction() as conn:
        result = {
            "search_id": request["search_id"],
            "data": search_result
        }
        await SearchData(conn).add_new_search(result)

    return json_response(data={"search_id": request["search_id"]})





