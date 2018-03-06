import base


class Password(base.BaseV30):

    def create_or_update(self, user_name, password):
        params = {
            "password": {
                "password-in-module": password,
            }
        }
        self._post("/admin/{0}/password".format(user_name), params)
