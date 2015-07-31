#!/usr/bin/env python
# -*- coding: utf-8 -*-


from textwrap import TextWrapper

class StdOutAction(object):
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

