from car_profile.models import CarProfile


def get_first_profile():
    return CarProfile.objects.first()
