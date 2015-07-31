#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Query(object):
    def match(self, status):
        raise NotImplementedError


class MatchAll(Query):
    def match(self, status):
        return True
