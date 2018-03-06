import base


class Routerbgp(base.BaseV30):

    def create(self, as_number, route_address, remote_as_address_ls):

        group_neighbor_ls = [
            {
                "peer-group": t["remote_address"],
                "peer-group-remote-as": t["remote_as_number"]} for t in remote_as_address_ls]

        params = {
            "bgp": {
                "as-number": as_number,
                "bgp": {
                    "log-neighbor-changes": 1,
                    "router-id": route_address,
                },
                "neighbor": {
                    "peer-group-neighbor-list": group_neighbor_ls
                }
            }
        }
        self._post("/router/bgp/", params)

    def add_remote_as(self, as_number, remote_address, remote_as):
        params = {
            "bgp": {
                "as-number": as_number,
                "neighbor": {
                    "peer-group-neighbor-list": [
                        {
                            "peer-group": remote_address,
                            "peer-group-remote-as": remote_as
                        }
                    ]
                }
            }
        }
        self._post("/router/bgp/{0}/".format(as_number), params)
