from models.models import Specialization


def get_specializations():
    return Specialization.query.join(Specialization.roles)
