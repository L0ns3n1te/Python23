#The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string.
#Ignore capitalization when determining if a character is a duplicate.
def d(s):
    s = s.replace("(", "☺")
    s = s.lower()
    for i in s:
        if s.count(i) > 1:
            s = s.replace(i, ")")
        else:
            s = s.replace(i, "(")
    return s


print(d("din"))
print(d("Success"))
print(d("(( @"))
print(d("recede"))
print(d("recede("))
print(d("recede(("))
