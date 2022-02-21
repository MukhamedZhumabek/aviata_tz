import json

from aiohttp.web import Request
from aiohttp.web_response import json_response


async def read_json_from_file(request: Request):
    with open('/templates/provider_b.json', 'r') as provider_b:
        data = provider_b.read()
    result = json.loads(data)
    return json_response(data=result)
