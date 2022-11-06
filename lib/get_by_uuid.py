def get_by_uuid(array, uuid):
    return [x for x in array if x.uuid == uuid][0]
