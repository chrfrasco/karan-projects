"""
takes an integer (maybe a float later?) between
0 and 999 and spells it out in plain english.

TODO: add support for thousands and beyond. must be
      a better method than current one, though.

author: christian scott
"""

import random as rand

digits = {

    "ones": ["", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"],

    "teens": ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],

    "tens": ["", "ten", "twenty", "thirty", "forty",
             "fifty", "sixty", "seventy", "eighty", "ninety"],

    "hundreds": ["", "one hundred", "two hundred", "three hundred",
                 "four hundred", "five hundred", "six hundred",
                 "seven hundred", "eight hundred", "nine hundred"]

}


def pretty_print(hundreds, tens, ones):

    if hundreds:
        hundy = digits["hundreds"][hundreds]
        if tens and ones:
            if tens == 1:
                teens = digits["teens"][ones]
                return "%s and %s" % (hundy, teens)
            else:
                tenner = digits["tens"][tens]
                uno = digits["ones"][ones]
                return "%s and %s %s" % (hundy, tenner, uno)

        elif tens:
            tenner = digits["tens"][tens]
            return "%s and %s" % (hundy, tenner)

        elif ones:
            uno = digits["ones"][ones]
            return "%s and %s" % (hundy, uno)

        else:
            hundy = digits["hundreds"][hundreds]
            return hundy

    elif tens:
        tenner = digits["tens"][tens]
        if tens == 1:
            teens = digits["teens"][ones]
            return "%s" % (teens)
        elif ones:
            uno = digits["ones"][ones]
            return "%s %s" % (tenner, uno)
        else:
            return "%s" % tenner

    elif ones:
        uno = digits["ones"][ones]
        return "%s" % uno

    else:
        return "zero"


def translate(num):
    assert type(num) == int
    sign = "pos" if num >= 0 else "neg"
    num = abs(num)
    hundreds = num // 100
    tens = (num - hundreds * 100) // 10
    ones = num - (hundreds * 100) - (tens * 10)

    if sign == "pos":
        return pretty_print(hundreds, tens, ones)
    elif sign == "neg":
        return "negative " + pretty_print(hundreds, tens, ones)


count = 0
for i in range(-999, 1000):
    try:
        case = translate(i)
    except Exception as e:
        count += 1
        print("{0} failed with error: {1}".format(i, e))

print("of 1999, {0} failed".format(count))
