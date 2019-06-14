import acos_client.v30.base


class IPPrefixList(acos_client.v30.base.BaseV30):

    def create(self, prefix_name, rules):

        params = {
            "prefix-list": {
                "name": prefix_name,
                "rules": rules
            }
        }
        return self._post("/ip/prefix-list/", params)

    def all(self):
        return self._get('/ip/prefix-list/')
