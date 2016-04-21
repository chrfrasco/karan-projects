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

def main():
	currency()
	pass

if __name__ == "__main__":
	main()