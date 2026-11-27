import datetime as dt

from fastmcp import FastMCP

mcp = FastMCP("Авиарейсы")

FLIGHTS = [
    {"flight_number": "SU-100", "origin": "Москва", "destination": "Санкт-Петербург", "price": 5200},
    {"flight_number": "DP-200", "origin": "Москва", "destination": "Санкт-Петербург", "price": 3800},
    {"flight_number": "S7-300", "origin": "Москва", "destination": "Санкт-Петербург", "price": 6100},
    {"flight_number": "DP-201", "origin": "Санкт-Петербург", "destination": "Москва", "price": 1800},
    {"flight_number": "SU-400", "origin": "Москва", "destination": "Казань", "price": 2500},
    {"flight_number": "S7-500", "origin": "Казань", "destination": "Санкт-Петербург", "price": 2900},
]


@mcp.tool
def get_all_flights(date: str) -> dict:
    """Верни все рейсы на дату YYYY-MM-DD.

    Args:
        date: Дата вылета в формате YYYY-MM-DD.
    """
    departure_date = dt.date.fromisoformat(date).isoformat()
    return {"date": departure_date, "currency": "RUB", "flights": FLIGHTS}


@mcp.tool
def calculate_trip_cost(ticket_price: int, hotel_price_per_night: int, nights: int) -> dict:
    """Посчитай бюджет поездки на одного человека в рублях.

    Args:
        ticket_price: цена выбранного билета в одну сторону.
        hotel_price_per_night: стоимость одной ночи в отеле из запроса пользователя.
        nights: число ночей. Обратный билет и другие расходы не учитываются.
    """
    if min(ticket_price, hotel_price_per_night, nights) < 0:
        raise ValueError("Цены и число ночей должны быть неотрицательными.")
    hotel_total = hotel_price_per_night * nights
    return {
        "ticket_price": ticket_price,
        "hotel_total": hotel_total,
        "total": ticket_price + hotel_total,
        "currency": "RUB",
    }


if __name__ == "__main__":
    # Запустите файл отдельно: python mcp_flights_server.py
    # Клиент подключается к URL http://127.0.0.1:8001/mcp.
    mcp.run(transport="http", host="127.0.0.1", port=8001)
