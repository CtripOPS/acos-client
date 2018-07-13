import acos_client.v30.base


class IPnetpool(acos_client.v30.base.BaseV30):

    def create(self, pool_name, start_address, end_address, netmask):
        params = {
            "pool": {
                "pool-name": pool_name,
                "start-address": start_address,
                "end-address": end_address,
                "netmask": netmask,
                "ip-rr": 1
            }
        }
        self._post("/ip/nat/pool/", params)
