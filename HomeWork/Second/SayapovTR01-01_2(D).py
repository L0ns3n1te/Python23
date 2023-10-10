#You are given an array asteroids of integers representing asteroids in a row.
#For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. There won't be any 0 in the given list.
#Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

def d (a,b):
    while(True):
        for i in range(len(a) - 1):
            if (a[i] > 0 and a[i+1] < 0):
                if abs(a[i]) > abs(a[i+1]):
                    b.remove(a[i+1])
                elif abs(a[i]) < abs(a[i+1]):
                    b.remove(a[i])
                elif abs(a[i]) == abs(a[i+1]):
                    b.remove(a[i])
                    b.remove(a[i+1])
        if a != b:
            a = []
            for j in b:
                a.append(j)
        else:
            break
    return b

n = (int)(input("Enter number of asteroids:"))
a = []
b = []
for i in range(n):
    c = (int)(input("enter asteroid data:"))
    a.append(c)
    b.append(c)
print(d(a,b))
