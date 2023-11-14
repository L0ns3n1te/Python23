# Your task is to write a function that accepts a floating point number and formats it using the notation given above.
# The resulting number should include 3 most significant digits and be rounded down towards zero (for example, 1238 should be 1.23K, and -1238 should be -1.23K).
# All trailing zeroes after the decimal point should be removed, and the decimal point should be excluded if the resulting number is whole number of units after the rounding down.
# If the number is too small, and it's rounded down to 0, then 0 should be returned.
# Beware of the negative zero, which should not appear in the output, instead the regular zero 0 should be returned.
import math


def d(i):
    if i == 0:
        return 0
    elif 0.01 >= i >= -0.01:
        return "0 (too small)"
    if -1000 < i < 1000:
        f = ""
        if i < 0:
            i = abs(i)
            f = "-"
        i = (math.floor(i * 100) / 100)
        if i % 1 != 0:
            return f + str(i)
        elif i % 1 == 0:
            return f + str(int(i))
    elif -10 ** 15 < i < 10 ** 15:
        i = math.floor(i)
        if i < 0:
            i = abs(i)
            f = "-"
        else:
            f = ""
        len_i = len(str(i))
        r = (len_i - 1) // 3
        i /= int("1" + "0" * r * 3)
        if i < 10:
            i = math.floor(i * 100) / 100
        elif i < 100:
            i = math.floor(i * 10) / 10
        else:
            i = math.floor(i)
        a = ["K", "M", "B", "T"]
        if i % 1 != 0:
            return f + str(i) + a[r - 1]
        else:
            return f + str(int(i)) + a[r - 1]
    elif -10 ** 15 > i or i > 10 ** 15:
        i = math.floor(i)
        if i < 0:
            i = abs(i)
            f = "-"
        else:
            f = ""
        len_i = len(str(i))
        r = (len_i - 1) // 3
        i /= int("1" + "0" * r * 3)
        r -= 5
        if i < 10:
            i = math.floor(i * 100) / 100
        elif i < 100:
            i = math.floor(i * 10) / 10
        else:
            i = math.floor(i)
        a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]
        a1 = r // 26
        a2 = r % 26
        if i % 1 != 0:
            return f + str(i) + a[a1] + a[a2]
        else:
            return f + str(int(i)) + a[a1] + a[a2]


print(d(0))
print(d(1))
print(d(-1))
print(d(123))
print(d(0.25))
print(d(-0.9999))
print(d(0.009))
print(d(1000))
print(d(1234))
print(d(-4000))
print(d(5809))
print(d(100000))
print(d(123456789))
print(d(1234567890))
print(d(1234567890000))
print(d(999999999999999))
print(d(1234567890000000000))
print(d(-0.0000001))
print(d(10 ** 300))
