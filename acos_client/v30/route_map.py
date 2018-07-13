import base


class RouteMap(base.BaseV30):

    def create(self, tag, ip_prefix, sequence, action='deny'):
        params = {
            "route-map": {
                "action": action,
                "sequence": sequence,
                "tag": tag,
                "match": {
                    "ip": {
                        "address": {
                            "prefix-list": {
                                "name": ip_prefix
                            }
                        }
                    }
                }
            }
        }
        self._post("/route-map/", params)

    def all(self):
        return self._get('/route-map')
