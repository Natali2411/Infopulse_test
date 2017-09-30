'''x = 10
while x > 0:
    print(str(x), end = '!\n')
    x -= 1'''

'''
l = [1,2,3,4,5,6,7,8,9,10]
while len(l) > 0:  # while l
    print(l.pop(len(l)-1))
#print(l)'''
'''
l = [1,10,3,5,6,7,11]

for item in l:
    if item % 2 == 0:
        print(item)
    elif item % 2 != 0:
        item += 1
        print(item)
'''
'''
l = [1,10,3,5,6,7,11]
for item in l:
    if item % 2 != 0:
        n = l.index(item)
        item += 1
        l[n] = item
        n += 1
print(l)'''

'''
l = [1,10,3,5,6,7,11]
for i in range(len(l)):
    if l[i] % 2 == 1:
        l[i] += 1
print(l)'''

'''
def repeat (s, exclaim):
    result = s *3
    if exclaim:
        result = str(result) + "!!!"
    return result

r = repeat(5, True)
print(r)'''

import math
def hypot(s1,s2):
    n = math.sqrt(s1**2 + s2**2)
    return(n)

#print(hypot(5,9))
