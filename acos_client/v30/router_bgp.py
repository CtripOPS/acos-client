import base


class Routerbgp(base.BaseV30):

    def create(self, as_number, route_address, remote_as_address_ls):

        group_neighbor_ls = [
            {
                "peer-group": t["remote_address"],
                "peer-group-remote-as": t["remote_as_number"],
                "advertisement-interval": 1
            } for t in remote_as_address_ls]

        params = {
            "bgp": {
                "as-number": as_number,
                "bgp": {
                    "log-neighbor-changes": 1,
                    "router-id": route_address,
                },
                "neighbor": {
                    "peer-group-neighbor-list": group_neighbor_ls
                },
                "timers": {
                    "bgp-holdtime": 3,
                    "bgp-keepalive": 1
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
                            "peer-group-remote-as": remote_as,
                            "advertisement-interval": 1
                        }
                    ],

                }
            }
        }
        self._post("/router/bgp/{0}/".format(as_number), params)

    def add_route_map(self, as_number, remote_address, remote_as, nbr_route_map, nbr_rmap_direction='in'):
        params = {
            "bgp": {
                "as-number": as_number,
                "neighbor": {
                    "ipv4-neighbor-list": [
                        {
                            "nbr-remote-as": remote_as,
                            "neighbor-ipv4": remote_address,
                            "neighbor-route-map-lists": [
                                {
                                    "nbr-rmap-direction": nbr_rmap_direction,
                                    "nbr-route-map": nbr_route_map
                                }
                            ],
                        }
                    ]
                }
            }
        }
        self._post("/router/bgp/{0}/".format(as_number), params)


    def get(self, as_number):
        return self._get("/router/bgp/{0}/".format(as_number))
