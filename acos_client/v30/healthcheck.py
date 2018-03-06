import base


class Healthcheck(base.BaseV30):
    def __init__(self, client):
        super(Healthcheck, self).__init__(client)
        self.protocol = ""
        self.url_prefix = "/health/monitor/"

    def _build_payload(self, **kwargs):
        pass

    def create(self, **kwargs):
        params = self._build_payload(**kwargs)
        self._post(self.url_prefix, params)

    @property
    def hchttps(self):
        return HCHTTPS(self.client)

    @property
    def hchttp(self):
        return HCHTTP(self.client)


class HCHTTPS(Healthcheck):
    def __init__(self, client):
        super(HCHTTPS, self).__init__(client)
        self.protocol = "https"

    def _build_payload(self, **kwargs):
        rv = rv = {
            "monitor": {
                "name": kwargs.get("hc_name"),
                "retry": 3,
                "up-retry": 1,
                "passive": 0,
                "strict-retry-on-server-err-resp": 0,
                "disable-after-down": 0,
                "interval": 5,
                "timeout": 5,
                "method": {
                    "https": {
                        "https": 1,
                        "https-url": 1,
                        "url-type": "GET",
                        "url-path": kwargs.get("hc_url"),
                        "https-expect": 1,
                        "https-text": kwargs.get("hc_expect"),
                    }
                }
            }
        }
        return rv


class HCHTTP(Healthcheck):
    def __init__(self, client):
        super(HCHTTP, self).__init__(client)
        self.protocol = "http"

    def _build_payload(self, **kwargs):
        rv = {
            "monitor": {
                "name": kwargs.get("hc_name"),
                "retry": 3,
                "up-retry": 1,
                "passive": 0,
                "strict-retry-on-server-err-resp": 0,
                "disable-after-down": 0,
                "interval": 5,
                "timeout": 5,
                "method": {
                    "http": {
                        "http": 1,
                        "http-url": 1,
                        "url-type": "GET",
                        "url-path": kwargs.get("hc_url"),
                        "http-expect": 1,
                        "http-text": kwargs.get("hc_expect"),
                    }
                }
            }
        }
        return rv
