import json


class RoomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialise = {
                'code': str(o.code),
                'size': o.size,
                'price': o.price,
                'lat': o.lat,
                'long': o.long
            }
            return to_serialise
        except Exception as error:
            return super().default(o)
