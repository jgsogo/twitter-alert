#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import open
from textwrap import TextWrapper

class DumpPlace(object):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')
    file = None

    def __init__(self, filename):
        self.file = open(filename, 'a', encoding='utf-8')

    def on_status(self, status):
        try:
            print("")
            print(self.status_wrapper.fill(status.text))
            print('\n\t\t%s  %s  via %s' % (status.author.screen_name, status.created_at, status.source))
            data = ['', '']
            if status.coordinates:
                data[0] = status.coordinates['coordinates']
                print('\t\tcoords: %s' % status.coordinates)
            if status.place:
                data[1] = status.place.full_name
                print('\t\tplace: %s' % status.place.full_name)
            self.file.write(u'%s\n' % ';'.join(data))
        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass

