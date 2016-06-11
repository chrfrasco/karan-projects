#!/usr/bin/python3
"""
Convert currency, mass, length and time.

Currency conversion done using currencylayer API.

author: christian scott
"""

from urllib.request import urlopen
import json

units = {
    'mass': {
        'g': 1,
        'oz': 0.035274,
        'kg': 0.001,
        'lb': 0.00220462,
    },

    'length': {
        'm': 1,
        'mm': 1000,
        'cm': 100,
        'km': 0.001,
        'ft': 3.28084,
        'in': 39.3701
    },

    'time': {
        's': 1,
        'ms': 1000,
        'min': 1/60,
        'hr': 1/3600,
        'day': 1/86400,
        'yr': 1/31557600
    }
}


def valid_number(s):
    try:
        float(s)
        return True
    except:
        return False


def valid_currency_codes(*codes):
    for code in codes:
        if len(code) == 3 and all(char.isalpha() for char in code):
            pass
        else:
            return False
    return True

def get_input(quantity):
    if quantity == "currency":
        from_code = input("Enter the source currency: ").upper()
        to_code = input("Enter the currency you would like to convert to: "
                        ).upper()

        while not valid_currency_codes(from_code, to_code):
            print("Currency codes may only consist of three letters "
                  "(EUR, NZD, USD etc)."
                  " Please try again.")
            from_code = input("Enter the source currency: ").upper()
            to_code = input("Enter the currency you would like to convert to: "
                            ).upper()

        user_amount = input("Enter amount to convert: ")

        while not valid_number(user_amount):
            user_amount = input("Enter amount to convert: ")

        return from_code, to_code, user_amount

    else:
        choices = ', '.join(units[quantity].keys())
        print("Can convert between %s." % choices)

        from_unit = input("Enter the starting unit: ")

        while from_unit not in choices:
            from_unit = input("Please enter a valid starting unit: ")

        to_unit = input("Enter the unit you'd like to convert to: ")

        while to_unit not in choices or to_unit == from_unit:
            to_unit == input("Please enter a valid starting unit."
                             "Must be different to the starting unit: ")

        user_amount = input("Enter the starting %s: " % quantity)

        while not valid_number(user_amount):
            user_amount = input("Non-numeric amount entered. "
                                "Please try again: ")

        return from_unit, to_unit, user_amount


def load_response(api_key, from_currency, to_currency):
    try:
        request = urlopen(
            "http://apilayer.net/api/"
            "live?access_key=%s&currencies=%s,%s&format=1"
            % (api_key, from_currency, to_currency))

        response = json.loads(request.read().decode('utf-8'))

        return response

    except:
        print("Must be able to connect to the internet to convert currency.")
        exit()


def currency(from_currency, to_currency, user_currency):
    try:
        api_key = json.loads(open('api_keys.json').read())['currency']

    except:
        api_key = input("Please enter your currencylayer API key: ")

    response = load_response(api_key, from_currency, to_currency)

    if response["success"]:
        try:
            from_rate = response['quotes']['USD%s' % (from_currency)]

        except:
            print("%s is not a valid currency code." % from_currency)

        try:
            to_rate = response['quotes']['USD%s' % (to_currency)]

        except:
            print("%s is not a valid currency code." % to_currency)

        from_rate, to_rate, user_currency = map(float, (
                            from_rate, to_rate, user_currency))

        return user_currency / from_rate * to_rate

    elif not response["success"]:
        print("Error:")

        if response["error"]["code"] == "101":
            print("Invalid currencylayer API key.")

        elif response["error"]["code"] == "202":
            print("Both currency codes are invalid.")

    else:
        print("No response from currencylayer.")


def mass(from_mass, to_mass, user_mass):
    return float(user_mass) / units['mass'][from_mass] * units['mass'][to_mass]


def length(from_length, to_length, user_length):
    return float(user_length) / units['length'][from_length] * \
                units['length'][to_length]


def time(from_time, to_time, user_time):
    return float(user_time) / units['time'][from_time] * units['time'][to_time]


def main():
    print("\n1. Currency",
          "2. Mass",
          "3. Length",
          "4. Time\n",
          sep="\n")

    choice = input("What kind of conversion would you like to do? ")

    while (not valid_number(choice)) or (not 0 < int(choice) < 5):
        choice = input("Please enter a number between 1 and 4: ")

    if choice == '1':
        from_unit, to_unit, user_amount = get_input('currency')
        final_amount = currency(from_unit, to_unit, user_amount)

    elif choice == '2':
        from_unit, to_unit, user_amount = get_input('mass')
        final_amount = mass(from_unit, to_unit, user_amount)

    elif choice == '3':
        from_unit, to_unit, user_amount = get_input('length')
        final_amount = length(from_unit, to_unit, user_amount)

    elif choice == '4':
        from_unit, to_unit, user_amount = get_input('time')
        final_amount = time(from_unit, to_unit, user_amount)

    print("%s %s is equivalent to %.2f %s." % (
        user_amount, from_unit, final_amount, to_unit))

if __name__ == "__main__":
    main()
