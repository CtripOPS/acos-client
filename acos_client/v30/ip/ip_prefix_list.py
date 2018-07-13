import acos_client.v30.base


class IPPrefixList(acos_client.v30.base.BaseV30):

    def create(self, prefix_name, ip_cidr, seq, action='permit'):
        params = {
            "prefix-list": {
                "name": prefix_name,
                'rules': [
                    {
                        'seq': seq,
                        'action': action,
                        'ipaddr': ip_cidr
                    }
                ]
            }
        }
        return self._post("/ip/prefix-list/", params)

    def all(self):
        return self._get('/ip/prefix-list/')
