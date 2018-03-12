from main.models import House


def get_by_id(house_id=0):

    if house_id <= 0:
        return None

    try:
        house = House.objects.get(house_id=house_id)
    except House.DoesNotExist:
        return None
    finally:
        return house


def get_list(min_size=0, max_size=200, location="", description=""):

    if min_size <= 0 or max_size < min_size:
        return None

    houses = House.objects.filter(size__range=(min_size, max_size))

    if location:
        houses = houses.filter(location__contains=location)
    if description:
        houses = houses.filter(text_description__contains=description)

    if houses:
        return houses
    else:
        return None
