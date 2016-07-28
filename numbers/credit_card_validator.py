"""
credit card validator

credit to Mike Hall for details on the Luhn algorithm
(http://www.brainjar.com/js/validation/default2.asp).

author: christian scott
"""


def validator(card_number):
    double = []
    for i, digit in enumerate(card_number[::-1]):
        if i % 2 == 1:
            double += [int(digit) * 2]
        else:
            double += [int(digit)]

    total = 0
    for digit in ''.join(map(str, double)):
        total += int(digit)

    if total % 10 == 0 and total != 0:
        return True
    else:
        return False

if __name__ == "__main__":
    sample = "1234567890123452"
    print("{0} {1} a valid credit card number.".format(sample, "is" if validator(sample) else "is not"))
