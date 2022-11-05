def convert_recommend_response(users, uuid, lineup_uuid):
    return {
        'user_uuids': users,
        'specialization_uuid': uuid,
        'lineup_uuid': lineup_uuid
    }
