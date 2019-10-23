def getUpdatedStatement(statement):
    
    # Create a list of all the words that makes up the statment. So "i know you know" will be converted to list ["i", "know", "you", "know"]
    # statement.lower() converts the string to lowercase. statement.split(" ") converts statement to a list divided by space
    stmtList = statement.lower().split(" ")
    # List to save all the indexes in the stmtList where value = "i"
    iIndexList = []
    # List to save all the indexes in the stmtList where value = "you"
    youIndexList = []

    # Using this variable to maintain the value of the index where you find "i" or "you"
    idx = 0

    # Iterate over each word in stmtList
    for string in stmtList:
        # if current word is "i", save the index in the list that saves all indexes of "i"
        if string.lower() == "i":
            iIndexList.append(idx)
        # if current word is "you", save the index in the list that saves all indexes of "you"
        elif string.lower() == "you":
            youIndexList.append(idx)
        # increment index for each iteration
        idx += 1
   
   # Using the list that saves all the indexes of i, replace all i's with you
    for x in iIndexList:
        stmtList[x] = "you"
    
    # Using the list that saves all the indexes of you, replace all you's with i
    for x in youIndexList:
        stmtList[x] = "i"

    # After replacing is with yous and yous with is, check if first word on the list is i or you
    # use " ".join(list) to create a string from all the items in the list separated by space. 
    # if we instead did ",".join(list), then we create a list of all the items in the list separated by comma
    if stmtList[0].lower() == "i":
        #if first word is i, add "you know" to front of the string
        return "you know " + " ".join(stmtList)
    else:
        #if first word is you, add "i know" to front of the string
        return "i know " + " ".join(stmtList)

myStatement = "i know you know"
print(getUpdatedStatement(myStatement))