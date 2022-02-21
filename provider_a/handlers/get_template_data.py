import json

from aiohttp.web import Request
from aiohttp.web_response import json_response


async def read_json_from_file(request: Request):
    async with open('/server/templates/response-a.json', 'r') as provider_a:
        data = provider_a.read()
    result = json.loads(data)
    return json_response(data=result)
