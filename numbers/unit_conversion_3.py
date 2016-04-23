"""
python 3

convert currency and mass

author: christian scott
"""

import json, datetime, re, sys
from urllib.request import urlopen

def is_numerical(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def check_currency_code(code):
    if len(code) == 3 and all(char.isalpha() for char in code):
        return False
    else:
        return True

def get_input():
    amount = input("Enter amount to convert: ").replace(' ', '')

    while not is_numerical(amount):
        input("Non-numerical amount entered. Press enter to try again.")
        amount = input("Enter amount to convert: ").replace(' ', '')

    from_currency = input("Enter your source currency "
        "(3 digit code): ").upper().replace(' ', '')

    while check_currency_code(from_currency):
        print("Invalid currency code")
        from_currency = from_currency = input("Enter your source currency "
        "(3 digit code): ").upper().replace(' ', '')

    to_currency = input("Enter the currency you would like "
        "to convert to (3 digit code): ").upper().replace(' ', '')

    while check_currency_code(from_currency):
        print("Invalid currency code")
        to_currency = to_currency = input("Enter the currency you would "
            "like to convert to (3 digit code): ").upper().replace(' ', '')

    return amount, from_currency, to_currency

def load_response(api_key, from_currency, to_currency):
    request = urlopen(
        'http://apilayer.net/api/live?access_key=%s&currencies=%s,%s&format=1' 
        % (api_key, from_currency, to_currency))

    response = json.loads(request.read().decode('utf-8'))

    try:
        from_rate = response['quotes']['USD%s' % (from_currency)]
        to_rate = response['quotes']['USD%s' % (to_currency)]
        return from_rate, to_rate, False
    except Exception as e:
        return _, _, e

def currency():
    try:
        api_key = json.loads(open('api_keys.json').read())['currency']
    except:
        api_key = input("Please enter your currencylayer API key: ")

    if len(sys.argv) == 1:
        amount, from_currency, to_currency = get_input()

    elif len(sys.argv) == 4:
        args = [arg.upper().replace(' ', '') for arg in sys.argv][1:]
        amount, from_currency, to_currency = args
        while not is_numerical(amount):
            input("Non-numerical amount entered. "
                "Press enter to try again.")
            amount = input("Enter amount to convert: ").replace(' ', '')

    else:
        print("Wrong number of command line arguments.")
        amount, from_currency, to_currency = get_input()

    response = load_response(api_key, from_currency, to_currency)

    while type(response) != tuple:
        input('\nYou have entered one or more invalid '
                  'currency codes. Press enter to try again.')
        amount, from_currency, to_currency = get_input()
        response = load_response(api_key, from_currency, to_currency)

    from_rate, to_rate = response

    to_amount = (float(amount) / float(from_rate)) * float(to_rate)

    time = re.findall(r"\d+-\d+-\d+", str(datetime.datetime.now()))[0]

    print("\nAs of %s, %s %s is worth %.2f %s\n" % (time, amount, 
                        from_currency, round(to_amount, 2), to_currency))
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
    
    from_mass = input("Starting unit? (1-4) ")

    while (not 0 < int(from_mass) < 5 or
           not is_numerical(from_mass)):
        print("Please enter a number from 1 to 4.")
        from_mass = input("Starting unit? (1-4) ")

    to_mass = input("Unit you'd like to convert to? (1-4) ")

    while ((not 0 < int(to_mass) < 5) or
           not is_numerical(to_mass) or
           from_mass == to_mass):
        print("Please enter a number from 1 to 4. "
               "Must be different from first unit.")
        to_mass = input("Unit you'd like to convert to? (1-4) ")

    start_mass = input("Enter the starting mass: ")

    while not is_numerical(start_mass):
        print("Non-numerical quantity entered. Please try again.")
        start_mass = input("Enter the starting mass: ")

    from_mass, to_mass = int(from_mass), int(to_mass)

    units = ['', 'g', 'kg', 'oz', 'lb']

    key = ''.join((units[from_mass], units[to_mass]))

    final_mass = float(start_mass) * masses[key]

    print("%s %s is equal to %.2f %s" % (start_mass, units[from_mass], 
                                         final_mass, units[to_mass]))

def length():
    pass

def temp(from_temp, to_temp, user_temp):
    if from_temp == 'c':
        user_temp = user_temp + 273.15
    elif from_temp == 'f':
        user_temp = (user_temp + 459.67) * (5/9)
    if to_temp == 'k':
        return user_temp
    elif to_temp == 'c':
        return user_temp - 273.15
    elif to_temp == 'f':
        return (user_temp / (5/9)) - 459.67

def main():
    print("What kind of conversion would you like to do?",
          "",
          "1. Currency",
          "2. Mass\n",
          sep="\n")
    choice = int(input("Enter your choice: "))
    while not 0 < choice < 3:
        choice = int(input("Please enter a valid choice: "))
    if choice == 1:
        currency()
    elif choice == 2:
        mass()


if __name__ == "__main__":
    main()
