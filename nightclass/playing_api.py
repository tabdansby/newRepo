import requests

r = requests.get('http://api.icndb.com/jokes/random')


data = r.json()

print('Joke #{}: '.format(data['value']['id']))

print('{}'.format(data['value']['joke']))
"""don't put imports in functions. You generally won't have to do that ever"""
#we will be using this script A LOT. We should know how to drill down in to a JS
#object and figure out its path/tree. Need to be able to look at a JSON piece and
#create this path
