"""
takes an integer (maybe a float later?) between
-9999 and 9999 and spells it out in plain english.

TODO: add support for thousands and beyond. must be
      a better method than current one, though.

author: christian scott
"""

num_names = {

    "ones": ["", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"],

    "teens": ["", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],

    "tens": ["", "ten", "twenty", "thirty", "forty",
             "fifty", "sixty", "seventy", "eighty", "ninety"]

}


def make_word(thousands, hundreds, tens, ones):
    """
    Takes four integers, each representing powers of ten up to 10^3, and makes a string representing them.
    """

    if thousands:
        ten3 = num_names["ones"][thousands] + " thousand"
    else:
        ten3 = ""

    if hundreds:
        ten2 = num_names["ones"][hundreds] + " hundred"
    else:
        ten2 = ""

    if tens:
        ten1 = num_names["tens"][tens]
    else:
        ten1 = ""

    if ones:
        ten0 = num_names["ones"][ones]
    else:
        ten0 = ""

    if tens == 1 and ones:
        ten1 = num_names["teens"][ones]
        ten0 = ""

    if (thousands or hundreds) and (ones or tens):
        connective = "and"
    else:
        connective = ""

    components = [ten3, ten2, connective, ten1, ten0]

    string_number = ' '.join([w for w in components if w])

    if string_number:
        return string_number
    else:
        return "zero"


def get_digits(n):
    """
    Takes an integer and returns the digit for each power of ten up to 10^3.
    """
    four_char_number = "0"*(4-len(str(n))) + str(n)
    digits = [int(c) for c in four_char_number]
    return digits


def translate(n):
    """
    Takes an integer and returns a string with the English translation of that number.
    """
    if n >= 0:
        sign = ""
    else:
        sign = "negative "
    abs_n = abs(n)
    thousands, hundreds, tens, ones = get_digits(abs_n)
    return sign + make_word(thousands, hundreds, tens, ones)
