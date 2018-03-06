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
