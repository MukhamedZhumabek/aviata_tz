import xml.etree.ElementTree as ET
from decimal import Decimal

from aiohttp.web import Request, json_response

from storage.models.search_data import SearchData
from utils.get_rate import get_rate_to_tenge


async def get_search_by_id(request: Request):
    currency = request.match_info['currency']
    search_id = request.match_info['search_id']

    if currency != 'KZT':
        return json_response(data="invalid currency")

    async with request.app["db_pool"].acquire() as connection:
        result = await SearchData(connection).get_search_by_id()

    tree = ET.parse('/template/country_data.xml')
    xml_tree = tree.getroot()

    converted_list = get_converted_list(result, xml_tree, currency)

    sorted_data = sorted(converted_list, key=lambda x: x['converted_price'])

    response = {
        "search_id": search_id,
        "status": result["status"],
        "items": sorted_data
    }
    return json_response(data=response)


def get_converted_list(flights_list, xml_tree, currency):
    converted_list = []
    for flights in flights_list:
        if flights["currency"] != currency:
            flights = convert_amount(flights, xml_tree)
    converted_list.append(flights)
    return converted_list


def convert_amount(flights, xml_tree):
    rate = get_rate_to_tenge(flights["currency"], xml_tree)
    if rate:
        flights["total"] = str(Decimal(flights["total"]) * Decimal(rate))
        flights["base"] = str(Decimal(flights["base"]) * Decimal(rate))
        flights["taxes"] = str(Decimal(flights["taxes"]) * Decimal(rate))
        flights["currency"] = str(Decimal(flights["currency"]) * Decimal(rate))
    return flights
