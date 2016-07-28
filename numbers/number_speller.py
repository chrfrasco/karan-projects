"""
takes an integer (maybe a float later?) between
0 and 999 and spells it out in plain english.

TODO: add support for thousands and beyond. must be
      a better method than current one, though.

author: christian scott
"""

digits = {

    "ones": ["", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"],

    "teens": ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],

    "tens": ["", "ten", "twenty", "thirty", "forty",
             "fifty", "sixty", "seventy", "eighty", "ninety"]

}

def wordify(hundreds, tens, ones):
	if hundreds:
		top = digits["ones"][hundreds] + " hundred"*(bool(hundreds)) + " and "*(bool(tens) or bool(ones))
	else:
		top = ""

	if tens == 1:
		middle = digits["teens"][ones]
		bottom = ""
	else:
		middle = digits["tens"][tens]
		bottom = " "*(bool(tens) and bool(ones)) + digits["ones"][ones]
		
	full_number = top + middle + bottom

	if not full_number:
		return "zero"
	else:
		return full_number

def translate(n):
	sign = "" if n >= 0 else "negative"
	hundreds = n // 100
	tens = (n - hundreds * 100) // 10
	ones = n - (hundreds * 100) - (tens * 10)
	
	return sign + wordify(hundreds, tens, ones)


count = 0
for i in range(0, 1000):
    try:
        case = translate(i)
    except Exception as e:
        count += 1
        print("{0} failed with error: {1}".format(i, e))

print("Of 999, {0} failed".format(count))
