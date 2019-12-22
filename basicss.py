import math as m


def everything_at_once(x, square, angle, stuff, cash, a, a1, a2):
    """
    Six exercizes are included here.
    Let me describe the arguments necessary for each exercize
    1) no arguments
    2) x -- list to be sorted
    3) square -- tuple with coords of a square; angle -- the angle of rotation
    4) stuff -- dictionary like {good,price}; cash -- integer equal to the amount of money you have
    5) a -- set of elements
    6) a1, a2 -- sets which are to be subtracted
    """
    """
    Ex. 1.
    Finds all prime numbers less than 1000.
    Checks whether current i is divisible by any of the elements of the current list.
    """
    prime_number=[]
    for i in range (2, 1000):
        flag = 0
        for num in prime_number:
            if i % num == 0:
                flag = 1
        if flag == 0:
            prime_number.append(i)
    print('1)', prime_number)
    """
    Ex. 2.
    Sorts the given list with the selection choice.
    """
    for i in range(len(x)):
        minimum = x[i]
	for j in range(len(x)):
	    if x[j] < minimum:
		minimun = x[j]
		jmin = j
	x[jmin] = x[i]
	x[i] = minimum
    print('2)', x)
    """
    Ex. 3.
    Rotates the given square by the given angle.
    """
        sqnew = [[0, 0], [0, 0],  [0, 0],  [0, 0]]
        for i in range(4):
            sqnew[i][0] = (square[i][0] - ((square[0][0] + square[2][0])/2))*m.cos(angle) - \
                          (square[i][1] - ((square[0][1] + square[2][1])/2))*m.sin(angle)
            sqnew[i][1] = (square[i][0] - ((square[0][0] + square[2][0])/2))*m.sin(angle) + \
                          (square[i][1] - ((square[0][1] + square[2][1])/2))*m.cos(angle)
            sqnew[i] = tuple(sqnew[i])
        print('3)', sqnew)
    """
    Ex. 4.
    Checks if cash is enough to buy every piece of stuff
    """
        a = []
        for key in stuff:
            if item[key] < cash:
                a.append(key)
        print('4)', a)
    """
    Ex. 5.
    Everything is quite simple, I quess.
    """
        set1 = set(a)
        print('5)', list(set1))
    """
    Ex. 6.
    This is also simple.
    """
        a3 = a1.difference(a2)
        print('6)', a3)