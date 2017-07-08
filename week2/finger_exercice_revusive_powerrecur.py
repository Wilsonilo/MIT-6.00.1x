def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    final = 1

    if exp == 0:
        return final
    else:

        while exp > 0:

            final = base * (final * recurPower(base, exp - 1))
            print("exp: {}, final: {}".format(exp, final))

            return final



recurPower(2, 2)