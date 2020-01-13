#Your choice of function or lambda expression


l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

"""def length_tester(x1, x2):
       if x1 > 3 and x2 > 3:
        return True
    else:
        return False
    filter(lambda x1: x1 > 3, l1)
    filter(lambda x2: x2 > 3, l2)

opposites = [lambda x1, x2: length_tester, zip(l1,l2)]

print(opposites)"""

opposites = list(filter(lambda x: (len(x[0]) > 3 and len(x[1]) > 3), zip(l1, l2)))
