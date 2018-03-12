from main.models import Car


def get_by_id(car_id=0):

    if car_id <= 0:
        return None

    try:
        car = Car.objects.get(car_id=car_id)
    except Car.DoesNotExist:
        return None
    finally:
        return car


def get_by_number(car_number=0):

    if car_number <= 0:
        return None

    try:
        car = Car.objects.get(car_number=car_number)
    except Car.DoesNotExist:
        return None
    finally:
        return car


def get_list():

    cars = Car.objects.all()
    if cars:
        return cars
    else:
        return None
