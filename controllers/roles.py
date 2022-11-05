from models.models import Role


def get_roles():
    return Role.query.join(Role.lineups)
