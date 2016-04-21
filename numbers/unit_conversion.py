"""
convert temp, currency, volume, mass

author: christian scott
"""
from __future__ import division
import json, datetime, re, sys
from urllib2 import urlopen

def is_numerical(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def get_input():
    amount = str(raw_input("Enter amount to convert: ")).replace(' ', '')

    while not is_numerical(amount):
        raw_input("Non-numerical amount entered. Press enter to try again.")
        amount = str(raw_input("Enter amount to convert: ")).replace(' ', '')

    from_currency = str(raw_input("Enter your source currency (3 digit code): ")).upper().replace(' ', '')
    to_currency = str(raw_input("Enter the currency you would like to convert to (3 digit code): ")).upper().replace(' ', '')

    return amount, from_currency, to_currency

def load_response(api_key, from_currency, to_currency):
    request = urlopen('http://apilayer.net/api/live?access_key=%s&currencies=%s,%s&format=1' 
        % (api_key, from_currency, to_currency))
    response = json.loads(request.read())

    try:
        from_rate = response['quotes']['USD%s' % (from_currency)]
        to_rate = response['quotes']['USD%s' % (to_currency)]
        return from_rate, to_rate
    except Exception, e:
        return e

def currency():
    try:
        api_key = json.loads(open('api_keys.json').read())['currency']
    except:
        api_key = str(raw_input("Please enter your currencylayer API key: "))

    if len(sys.argv) == 1:
        amount, from_currency, to_currency = get_input()

    elif len(sys.argv) == 4:
        args = [arg.upper().replace(' ', '') for arg in sys.argv][1:]
        amount, from_currency, to_currency = args
        while not is_numerical(amount):
            raw_input("Non-numerical amount entered. Press enter to try again.")
            amount = str(raw_input("Enter amount to convert: ")).replace(' ', '')

    else:
        print "Wrong number of command line arguments."
        amount, from_currency, to_currency = get_input()

    response = load_response(api_key, from_currency, to_currency)

    while type(response) != tuple:
        raw_input('\nYou have entered one or more invalid currency codes. Press enter to try again.')
        amount, from_currency, to_currency = get_input()
        response = load_response(api_key, from_currency, to_currency)

    from_rate, to_rate = response

    to_amount = (float(amount) / float(from_rate)) * float(to_rate)

    time = re.findall(r"\d+-\d+-\d+", str(datetime.datetime.now()))[0]

    print "\nAs of %s, %s %s is worth %.2f %s\n" % (time, amount, 
                        from_currency, round(to_amount, 2), to_currency)
def mass():
    masses = {'ozg': 28.3495, 
             'ozkg': 0.0283495, 
             'ozlb': 0.0625, 
             'goz': 0.035274, 
             'gkg': 0.001, 
             'glb': 0.00220462, 
             'kgoz': 35.274, 
             'kgg': 1000, 
             'kglb': 2.20462, 
             'lboz': 16, 
             'lbg': 453.592, 
             'lbkg': 0.453592
             }
    print ('1. gram\n'
           '2. kilogram\n'
           '3. ounce\n'
           '4. pound\n')
    
    from_mass = str(raw_input("Starting unit? (1-4) "))

    while not 0 < int(from_mass) < 5 or not is_numerical(from_mass):
        print "Please enter a number from 1 to 4."
        from_mass = int(raw_input("Starting unit? (1-4) "))

    to_mass = str(raw_input("Unit you'd like to convert to? (1-4) "))

    while not 0 < int(to_mass) < 5 or not is_numerical(to_mass) or from_mass == to_mass:
        print "Please enter a number from 1 to 4. Must be different from first unit."
        from_mass = int(raw_input("Unit you'd like to convert to? (1-4) "))

    start_mass = str(raw_input("Enter the starting mass: "))

    while not is_numerical(start_mass):
        print "Non-numerical quantity entered. Please try again."
        start_mass = str(raw_input("Enter the starting mass: "))

    from_mass, to_mass = int(from_mass), int(to_mass)

    units = ['', 'g', 'kg', 'oz', 'lb']

    key = ''.join((units[from_mass], units[to_mass]))

    final_mass = float(start_mass) * masses[key]

    print "%s %s is equal to %.2f %s" % (start_mass, units[from_mass], final_mass, units[to_mass])

def main():
    currency()
    mass()

if __name__ == "__main__":
    main()
