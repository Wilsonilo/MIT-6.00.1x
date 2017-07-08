def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    keywithmax = {"count": 0, "keyname": None}

    for element in aDict.keys():
        if len(aDict[element]) > keywithmax["count"]:
            keywithmax["count"] = len(aDict[element])
            keywithmax["keyname"] = element


    return keywithmax["keyname"]




animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(biggest(animals))
