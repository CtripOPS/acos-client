import acos_client.errors as acos_errors
import acos_client.v30.base as base


class Basetemplate(base.BaseV30):

    def __init__(self, client):
        super(Basetemplate, self).__init__(client)
        self.prefix = "/slb/template/{0}/".format(self.pers_type)

    def create(self, name, **kwargs):
        payload = kwargs["payload"] if "payload" in kwargs.keys(
        ) else self.get_params(name)
        self._post(self.prefix, payload, **kwargs)

    def delete(self, name, **kwargs):
        self._delete(self.prefix + name, **kwargs)


class Httptemplate(Basetemplate):

    def __init__(self, client):
        self.pers_type = 'http'
        super(Httptemplate, self).__init__(client)

    def get_params(self, name):
        return {
            "http": {
                "name": name,
                "insert-client-ip": 1,
                "insert-client-ip-header-name": "X-Forwarded-For",
                "client-ip-hdr-replace": 1
            }
        }


class Httpurlhashtemplate(Basetemplate):

    def __init__(self, client):
        self.pers_type = 'http'
        super(Httpurlhashtemplate, self).__init__(client)

    def get_params(self, name):
        return {
            "http": {
                "name": name,
                "insert-client-ip": 1,
                "insert-client-ip-header-name": "X-Forwarded-For",
                "url-hash-persist": 1,
                "url-hash-last": 80
            }
        }


class Tcptemplate(Basetemplate):

    def __init__(self, client):
        self.pers_type = 'tcp'
        super(Tcptemplate, self).__init__(client)

    def get_params(self, name):
        return {
            "tcp": {
                "name": name,
                "reset-fwd": 1,
                "reset-rev": 1
            }
        }


class TcpProxyTemplate(Basetemplate):

    def __init__(self, client):
        self.pers_type = 'tcp-proxy'
        super(TcpProxyTemplate, self).__init__(client)

    def get_params(self, name):
        return {
            "tcp-proxy": {
                "name": name,
                "reset-fwd": 1,
                "reset-rev": 1
            }
        }