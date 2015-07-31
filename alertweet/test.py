#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from listeners import StdOutListener

from secret import consumer_key, consumer_secret, TOKENS


import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

def main():
    log.info("\n")
    log.info("========================")
    log.info("= Started Alert Tweet! =")
    log.info("========================")

    # Build listener
    listener = StdOutListener()

    # Connect to stream
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    tokens = TOKENS.get('chimp_ski', None)
    if not tokens:
        return None

    auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])
    stream = tweepy.Stream(auth, listener, timeout=None)

    # Run!
    # stream.userstream()  # El stream del usuario
    # stream.filter(languages=["es"], track=['RAE', 'i18n', 'vacaciones'])  # Algunos filtros

    # LOCATIONS. Use http://boundingbox.klokantech.com/ for boundingboxes
    SPAIN_GEOBOX = [-9.38,36.05,3.35,43.75]
    # Must read: http://arxiv.org/ftp/arxiv/papers/1403/1403.2345.pdf
    stream.filter(languages=["es"], locations=SPAIN_GEOBOX)  # Algunos filtros



if __name__ == '__main__':
    main()