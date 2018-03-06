import base


class Vrrpavrid(base.BaseV30):

    def create(self, address):
        params = {
            "vrid": {
                "vrid-val": 0,
                "floating-ip": {
                    "ip-address-part-cfg": [
                        {
                            "ip-address-partition": address
                        }
                    ]
                },
                "follow": {
                    "vrid-lead": "default-vrid-lead"
                }

            }
        }
        self._post("/vrrp-a/vrid/", params)

    def get(self, vrid=0):

        return self._get("/vrrp-a/vrid/{0}".format(vrid))

    def add_address(self, address):
        tmp = self.get()
        ip_address_list = tmp["vrid"]["floating-ip"]["ip-address-part-cfg"]
        exist_address_set = set(t["ip-address-partition"] for t in tmp["vrid"][
                                "floating-ip"]["ip-address-part-cfg"] if "ip-address-partition" in t.keys())
        if address not in exist_address_set:
            ip_address_list.append({"ip-address-partition": address})

        params = {
            "vrid": {
                "floating-ip": {
                    "ip-address-part-cfg": ip_address_list
                }
            }
        }
        return self._post("/vrrp-a/vrid/0/", params)
