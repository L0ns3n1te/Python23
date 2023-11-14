# Your task is to write a function that accepts a floating point number and formats it using the notation given above.
# The resulting number should include 3 most significant digits and be rounded down towards zero (for example, 1238 should be 1.23K, and -1238 should be -1.23K).
# All trailing zeroes after the decimal point should be removed, and the decimal point should be excluded if the resulting number is whole number of units after the rounding down.
# If the number is too small, and it's rounded down to 0, then 0 should be returned.
# Beware of the negative zero, which should not appear in the output, instead the regular zero 0 should be returned.
import math


def d(i):
    if -1000 < i < 1000:
        i = (math.floor(i * 100) / 100)
        if i % 1 != 0:
            return i
        elif i % 1 == 0:
            return int(i)
    elif -10 ** 15 < i < 10 ** 15:
        if i >= 1000:
            i = math.floor(i)
            len_i = len(str(i))
            r = (len_i - 1) // 3
            i /= int("1" + "0"*r*3)
            if i < 10
            a = ["K", "M", "B", "T"]
            if i % 1 != 0:
                return str(i) + a[r - 1]
            else:
                return str(int(i)) + a[r - 1]


print(d(0))
print(d(1))
print(d(-1))
print(d(123))
print(d(0.25))
print(d(0.9999))
print(d(0.009))
print(d(1000))
print(d(123456789))
print(d(1234567890))
print(d(1234567890000))
print(d(999999999999999))
