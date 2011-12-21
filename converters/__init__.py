def days_to_seconds(days):
    ''' This function converts days to seconds '''
    return days*24*60*60

def celsius_to_fahrenheit(degrees):
    ''' Converts degrees Celsius to degrees Fahrenheit '''
    fahrenheit = degrees *9.0 /5.0 +32
    return fahrenheit

def fahrenheit_to_celsius(degrees):
    ''' Converts degrees Fahrenheit to degrees Celsius '''
    return 0

def surface_of_circle(radius):
    ''' Calculates the surface of a circle. Hint: Use pow(radius, exponent) for power '''
    from math import pi
    return radius * radius * pi

def cube_volume(length, width, height):
    ''' Returns the volume of the cube '''
    return 0

def usd_to_chf(usd):
    ''' Fetches the current exchange rate and converts to swiss francs '''
    import urllib2
    import json
    req = urllib2.Request('https://raw.github.com/currencybot/open-exchange-rates/master/latest.json')
    opener = urllib2.build_opener()
    f = opener.open(req)
    data = json.loads(f.read())
    exchange_rate = data['rates']['CHF']
    return 0

def lessons_to_minutes(lessons):
    
    ''' Returns the amount of minutes spent in lessons '''
    return lessons * 45

def mwst(amount):
    ''' This returns the amount of tax (mwst) on a given amount. Watch out, the amount already
    includes the tax! '''
    return 0

def joules_to_calories(joules):
    ''' Converts joules to calories '''
    j = 0.239005736
    calories = joules * j 
    return calories

def kmh_to_mph(kmh):
    return 0

def distance_between_points(x1, x2):
    ''' Returns the distance between the points x1 and x2.
    The points are tuples (1,5). sqrt() is the root, pow(x, exponent) is the power
    '''
    from math import sqrt
    return 0

def cat_and_dog_speech(animal):
    if animal=='hund': return 'wuff'
    if animal== 'katze': return 'miau'
    
def element_in_list(element, list):
    ''' Checks if an element is in a list and returns True if so,
    otherwise False
    '''
    return False
