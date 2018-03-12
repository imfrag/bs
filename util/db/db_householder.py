from main.models import HouseHolder


def get_by_id(householder_id=0):

    if householder_id <= 0:
        return None

    try:
        householder = HouseHolder.objects.get(id=householder_id)
    except HouseHolder.DoesNotExist:
        return None
    return householder


# ue -> username or email
def get_by_uoe(username="", email=""):

    if username or email:
        try:
            if username:
                householder = HouseHolder.objects.get(username=username)
            elif email:
                householder = HouseHolder.objects.get(email=email)
        except HouseHolder.DoesNotExist:
            return None
        finally:
            return householder

    return None


def get_by_tel(tel):

    if not tel:
        return None

    householders = HouseHolder.objects.filter(tel__contains=tel)

    if householders:
        return None
    elif len(householders) == 1:
        return householders[0]
    else:
        return householders



