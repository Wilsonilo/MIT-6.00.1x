'''
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here

    counter = 0
    finaltuple = ()
    for tuple in aTup:
        if (counter % 2) != 1:
            finaltuple = finaltuple + (tuple,)
        counter += 1
    return finaltuple

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
