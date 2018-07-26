import base


class Admin(base.BaseV30):

    def create(self, user_name, partition_name):
        params = {
            "admin": {
                "user": user_name,
                "privilege-list": [
                    {
                        "partition-name": partition_name,
                        "privilege-partition": "partition-write"
                    }
                ]
            }
        }
        self._post("/admin", params)

    def delete(self, user_name):
        self._delete("/admin/{0}".format(user_name))

    def all(self, ):
        return self._get('/admin')

