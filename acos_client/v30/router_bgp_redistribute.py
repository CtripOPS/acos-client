import base


class Routerbgpredistribute(base.BaseV30):

    def create(self, as_number):
        params = {
            "redistribute": {
                "ip-nat-cfg": {
                    "ip-nat": 1
                },
                "vip": {
                    "only-flagged-cfg": {
                        "only-flagged": 1,
                    }
                }
            }
        }
        self._post("/router/bgp/{0}/redistribute/".format(as_number), params)
