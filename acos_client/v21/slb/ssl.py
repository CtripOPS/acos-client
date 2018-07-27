#!/usr/bin/env python
#! -*- coding: utf-8 -*-

__author__ = 'pete.c.guan'

from acos_client.v21 import base

class SSL(base.BaseV21):

    def get_all_ssl(self, **kwargs):
        return self._get("slb.ssl.getAll", **kwargs)