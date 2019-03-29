import base


class RouteMap(base.BaseV30):

    def create(self, name, sequence, action, ip_prefix=None):
        params = {
            "route-map": {
                "action": action,
                "sequence": sequence,
                "tag": name
            }
        }
        if ip_prefix:
            params['route-map'].setdefault('match', {
                "ip": {
                    "address": {
                        "prefix-list": {
                            "name": ip_prefix
                        }
                    }
                }
            })
        self._post("/route-map/", params)

    def all(self):
        return self._get('/route-map')
