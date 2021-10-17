# stop points to get the data from the address string
async def get_constants(ship_address: str):
    city_start = ship_address.find("city") + 8
    city_end = ship_address.find(")", city_start) - 1
    street_start = ship_address.find("street_line1") + 16
    street_end = ship_address.find(")", street_start) - 1
    post_start = ship_address.find("post_code") + 13
    post_end = ship_address.find(")", post_start) - 1

    constants = [city_start, city_end, street_start, street_end, post_start, post_end]

    return constants

