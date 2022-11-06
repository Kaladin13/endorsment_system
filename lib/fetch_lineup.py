from controllers.profile import get_users_uuid_by_specialization
from controllers.roles import get_roles
from controllers.specializations import get_specializations
from lib.get_by_uuid import get_by_uuid


def fetch_lineup(lineup):
    roles = get_roles()
    specializations = get_specializations()

    lineup_role = get_by_uuid(roles, lineup.role_uuid)

    specialization_by_lineup = get_by_uuid(specializations, lineup_role.specialization_uuid)

    users = get_users_uuid_by_specialization(specialization_by_lineup.uuid)

    return [users, specialization_by_lineup.uuid]
