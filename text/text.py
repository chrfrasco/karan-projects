from collections import defaultdict
import re

def fizzbuzz(n):
    # True = 1 and False = 0... Magic. It's pretty ugly but a one line solution
    # to fizzbuzz is too cool not to do it
    print("\n".join(["" + "fizz"*(i%3 == 0) + "buzz"*(i%5 == 0) or str(i) for i in range(n)]))

def string_reverse(s):
    print(str[::-1])

def pig_latin(s):
    s = s.lower().split()
    for i in range(len(s)):
        if s[i][0] in 'aeiou':
            s[i] += "-yay"
        else:
            s[i] = s[i][1:] + s[i][0] + "-ay"
    print(" ".join(s))

def vowel_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counts = zip(vowels, map(s.lower().count, vowels))
    total = 0
    for pair in counts:
        print("    %s: %d" % pair)
        total += pair[1]
    print("total: %d" % total)

def palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False

def word_count(s):
    words = s.lower().split()
    d = defaultdict(int)
    pattern = re.compile('[\W]+')
    for word in words:
        word = pattern.sub('', word)
        d[word] += 1
    for pair in d.items():
        print("%s: %d" % pair)

s = """Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate, we can not consecrate, we can not hallow this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth.
"""

word_count(s)
