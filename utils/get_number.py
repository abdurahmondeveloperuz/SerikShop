import asyncio
from pyonlinesim import OnlineSMS

def get_country(nm):
	if nm == "russia":
		return 7
	if nm == "india":
		return 91
	if nm == "brazil":
		return 55
	if nm == "kenya":
		return 254
	if nm == "ukraine":
		return 380
	if nm == "france":
		return 33
	if nm == "peru":
		return 51
	if nm == "mexico":
		return 52
	if nm == "turkey":
		return 90
	if nm == "nicagura":
		return 505
	if nm == "combodia":
		return 855
	if nm == "thailand":
		return 66
	if nm == "usa":
		return 1
	if nm == "malaysia":
		return 60
	if nm == "kazakhstan":
		return 7
	if nm == "netherlands":
		return 31
	if nm == "estonia":
		return 372
	if nm == "kyrgyzstan":
		return 996
	if nm == "indonesia":
		return 62
	if nm == "Vietnam":
		return 84
	if nm == "hungary":
		return 36
	if nm == "africa":
		return 27
	if nm == "venezuela":
		return 58
	if nm == "argentina":
		return 54
	if nm == "congo":
		return 243
	if nm == "egypt":
		return 20
	if nm == "philippens":
		return 63
	if nm == "hongkong":
		return 852
	if nm == "romania":
		return 40
	if nm == "singapore":
		return 65
	if nm == "tobago":
		return 868
	if nm == "china":
		return 86
	if nm == "switzerland":
		return 41 
	if nm == "slovakia":
		return 421
	if nm == "moldova":
		return 373
	if nm == "korea":
		return 82
	if nm == "spain":
		return 34
	if nm == "morocco":
		return 212
	if nm == "bangladesh":
		return 880
	if nm == "pakistan":
		return 92
	if nm == "germany":
		return 49
	if nm == "qatar":
		return 974
	if nm == "portugal":
		return 351
	if nm == "sweden":
		return 46
	if nm == "canada":
		return 1
	if nm == "bahrain":
		return 973
	if nm == "kuwait":
		return 965
	if nm == "italy":
		return 39




async def get_price(api_token: str, country: str, service_) -> None:
    async with OnlineSMS(api_token) as client:
        country = await client.get_services(country=country)
        for service in country.services:
            if service_.capitalize().startswith(service.service) or service.service.capitalize().startswith(service_) or service.service.lower() == service_.lower():
                return service.count 

# asyncio.run(get_price(api_token='8f2zKvQjFrtzU86-e7gHV3HG-YBzT5Q65-7qC95pnL-6CnSC2DdvRQWH88', service_="telegram",country='380'))




async def get_phone(api_token: str, service: str, country: int) -> None:
    async with OnlineSMS(api_token) as client:
        order = await client.order_number(service=service, country=country, number=True)
        # print(f'Operation ID: {order.operation_id} | Received number: {order.number}')
        return order

# a = asyncio.run(get_phone(api_token='8f2zKvQjFrtzU86-e7gHV3HG-YBzT5Q65-7qC95pnL-6CnSC2DdvRQWH88', service='yandex', country="39")) # 2 is a country id received from get_services method.

async def get_sms(api_token: str, operation_id: int) -> None:
    async with OnlineSMS(api_token) as client:
        my_orders = await client.get_order_info(operation_id=operation_id) # Get Orders
        order = my_orders.orders # Get First Order
        return order.pop()
# asyncio.run(get_sms(api_token='8f2zKvQjFrtzU86-e7gHV3HG-YBzT5Q65-7qC95pnL-6CnSC2DdvRQWH88', operation_id=))
    
def cancel_sms(phone_id):
    id = str(phone_id)

    headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}

    response = requests.get('https://5sim.net/v1/user/cancel/' + id, headers=headers)
    if response.status_code == '200' or response.status_code == 200:
        return True
    else:
        return False


