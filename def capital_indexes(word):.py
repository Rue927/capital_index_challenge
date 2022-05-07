def capital_indexes(word):
    mylist = []
    mylistindexcounter = 0
    
    for x in range(0, len(word)):
        if(word[x].isupper()):
            mylist.insert(mylistindexcounter, x)
            mylistindexcounter = mylistindexcounter + 1
    return mylist