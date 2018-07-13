# Copyright 2014-2016 A10 Networks.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import acos_client.v30.base as base

from ip_net_pool import IPnetpool
from ip_prefix_list import IPPrefixList


class IP(base.BaseV30):
    # For status args

    @property
    def net_pool(self):
        return IPnetpool(self.client)

    @property
    def prefix_list(self):
        return IPPrefixList(self.client)
