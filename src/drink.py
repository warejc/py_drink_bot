import requests
import configparser

conf = configparser.ConfigParser()
conf.read('/config.ini')

key = conf.get('Creds', 'key')
body = {}
url = 'https://maker.ifttt.com/trigger/drink_water/with/key/{0}'.format(key)

# should add logging here to log the request/response
req = requests.post(url)
