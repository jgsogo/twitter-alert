#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tweepy


class Listener(tweepy.StreamListener):

    def __init__(self, query, action, *args, **kwargs):
        super(Listener, self).__init__(*args, **kwargs)
        self.query = query
        self.action = action

    def on_status(self, status):
        if self.query.match(status):
            self.action.on_status(status)

    def on_error(self, status_code):
        print('An error has occured! Status code = %s' % status_code)
        return True  # keep stream alive

    def on_timeout(self):
        print('Snoozing Zzzzzz')