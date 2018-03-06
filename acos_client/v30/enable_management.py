import base


class Enablemanagement(base.BaseV30):
    def __init__(self, client):
        super(Enablemanagement, self).__init__(client)
        self.iftype = ""
        self.url_prefix = "/enable-management/service/"

    def _build_payload(self, **kwargs):
        rv = {
            self.iftype: {
                "ve-cfg": [
                    {
                        "ve-start": kwargs.get("vlan_num"),
                        "ve-end": kwargs.get("vlan_num")
                    }
                ]
            }
        }
        return rv

    def create(self, **kwargs):

        payload = self._build_payload(**kwargs)
        return self._post(self.url_prefix,
                          payload)

    @property
    def enablehttp(self):
        return ENABLEHTTP(self.client)

    @property
    def enablessh(self):
        return ENABLESSH(self.client)

    @property
    def enablehttps(self):
        return ENABLEHTTPS(self.client)

    @property
    def enablesnmp(self):
        return ENABLESNMP(self.client)


class ENABLEHTTP(Enablemanagement):
    def __init__(self, client):
        super(ENABLEHTTP, self).__init__(client)
        self.iftype = "http"
        self.url_prefix = "{0}{1}/".format(self.url_prefix, self.iftype)


class ENABLESSH(Enablemanagement):
    def __init__(self, client):
        super(ENABLESSH, self).__init__(client)
        self.iftype = "ssh"
        self.url_prefix = "{0}{1}/".format(self.url_prefix, self.iftype)


class ENABLEHTTPS(Enablemanagement):
    def __init__(self, client):
        super(ENABLEHTTPS, self).__init__(client)
        self.iftype = "https"
        self.url_prefix = "{0}{1}/".format(self.url_prefix, self.iftype)


class ENABLESNMP(Enablemanagement):
    def __init__(self, client):
        super(ENABLESNMP, self).__init__(client)
        self.iftype = "snmp"
        self.url_prefix = "{0}{1}/".format(self.url_prefix, self.iftype)
