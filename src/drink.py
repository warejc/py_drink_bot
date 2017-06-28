#!/usr/bin/env python3
import requests
import configparser
import os

conf = configparser.ConfigParser()
conf.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../', 'config.ini'))

key = conf.get('Creds', 'key')
body = {}
url = 'https://maker.ifttt.com/trigger/drink_water/with/key/{0}'.format(key)

# should add logging here to log the request/response
req = requests.post(url)
