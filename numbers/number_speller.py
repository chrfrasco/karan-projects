"""
takes an integer (maybe a float later?) between
0 and 100 and spells it out in plain english.

TODO: increase range to 1000 then add support for neg numbers

author: christian scott
"""

digits = {
    "ones": {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    },

    "tens": {
        0: "",
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }
}

def get_columns(number):
    tens = number // 10
    ones = number - tens * 10

    return tens, ones

def translate(number):
    tens, ones = get_columns(number)

    if not (ones or tens):
        return "zero"

    elif ones and tens:
        return "%s %s" % (digits["tens"][tens], digits["ones"][ones])

    elif ones:
        return "%s" % digits["ones"][ones]

    elif tens:
        return "%s" % digits["tens"][tens]

def test_translate():
    assert translate(0) == "zero"
    assert translate(1) == "one"
    assert translate(10) == "ten"
    assert translate(12) == "ten two"
    assert translate(45) == "forty five"

    assert get_columns(45) == (4, 5)

    print("tests pass")

translate(45)
test_translate()
