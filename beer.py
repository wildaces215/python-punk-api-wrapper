
import requests

url = 'https://api.punkapi.com/v2/'




def random_beer():
    r = requests.get(url+'/beers/random')
    return r.text


def beer_name_data(beer_name):
    res = requests.get(url+'/beers?beer_name='+beer_name)
    return res.text


