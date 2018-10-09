import requests

url = 'https://api.punkapi.com/v2/beers'






#Gets a random Beer 
def random_beer():
    r = requests.get(url+'/random')
    return r.text

def whiteToUnder(userString):
    return userString.replace(" ","_")


#Gets the beer names from api, uses partial strings.
def beer_name_data(beer_name):
    res = requests.get(url+'?beer_name='+beer_name)
    return res.text

#Takes the parameters before date brewed
def brewDateBefore(stringBef):
    res = requests.get(url+'?brewed_before='+stringBef)
    if res.status_code ==400:
        return res.status_code
    else:
        return res.text

def brewDateAfter(afterDate):
    res = requests.get(url+'?brewed_after='+afterDate)
    return res.text