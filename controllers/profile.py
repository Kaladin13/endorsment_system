from models.models import Profile


def get_users_uuid_by_specialization(specialization_uuid):
    profiles = Profile.query.filter_by(specialization_uuid=specialization_uuid)
    users_uuids = map(lambda profile: profile.user_uuid, profiles)
    return list(users_uuids)
