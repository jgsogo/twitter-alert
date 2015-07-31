#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from textwrap import TextWrapper

import logging
log = logging.getLogger(__name__)


class StdOutListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            print("")
            print(self.status_wrapper.fill(status.text))
            print('\n\t\t%s  %s  via %s' % (status.author.screen_name, status.created_at, status.source))
            if status.coordinates:
                print('\t\tcoords: %s' % status.coordinates)
            if status.place:
                print('\t\tplace: %s' % status.place.full_name)

        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

    def on_error(self, status_code):
        print('An error has occured! Status code = %s' % status_code)
        return True  # keep stream alive

    def on_timeout(self):
        print('Snoozing Zzzzzz')


class QueryListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def __init__(self, query_callback=None, *args, **kwargs):
        log.debug("Built FundeuQueryListener with query_callback %r" % query_callback)
        super(QueryListener, self).__init__(*args, **kwargs)
        self.query_callback = query_callback

    def on_status(self, status):
        # Tweet must be something like ---
        if False:  # Check if this status is interesting for query_listener
            self.on_query(status)

    def on_error(self, status_code):
        return True

    def on_query(self, status):
        log.debug("Query: %r" % status.text)
        if not self.query_callback:
            print(self.status_wrapper.fill(status.text))
            print('\n %s  %s  via %s\n' % (status.author.screen_name, status.created_at, status.source))
        else:
            try:
                self.query_callback(status)
            except:
                pass
