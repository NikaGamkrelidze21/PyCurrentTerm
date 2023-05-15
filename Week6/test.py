import requests
from pprint import pprint

response = requests.get('https://google.com')

pprint(response.headers['Content-Type'])