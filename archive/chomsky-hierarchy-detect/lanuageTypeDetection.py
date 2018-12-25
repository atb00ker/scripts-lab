
def checkLangauge(variables, terminals, startSymbol, productionRules):
    '''
    Check Chomsky Heirarchy, Spit the 
    langauge's type! this is a BAD code!
    I am only making a project!
    Do not Judge my coding!
    '''
    langaugeType = 3
    # Check Only Type 3
    for rule in productionRules:
        equalPoint = rule.find('=')
        if rule[equalPoint+1] in variables and rule[-1] in variables:
            langaugeType = 2
            break
        for letter in range(0, equalPoint):
            if letter in terminals:
                langaugeType = 2
                break
        if langaugeType != 3:
            break

    if langaugeType == 3:
        print ("Type", langaugeType, "Language")
        return

    # Check Only Type 2
    for rule in productionRules:
        if rule[0] in terminals or rule[1] != '=':
            langaugeType = 1

    if langaugeType == 2:
        print ("Type", langaugeType, "Language")
        return

    # Check Only Type 1
    for rule in productionRules:
        equalPoint = rule.find('=')
        if equalPoint is 0 or equalPoint*2 > len(rule):
            print (rule)
            print (equalPoint)
            print (len(rule))
            langaugeType = 0

    print ("Type", langaugeType, "Language")


def takeInput():
    '''
    Hope wouldn't make it to production,
    This function only takes in the variables 
    and called checklangauge function!
    '''
    V = []
    nV = int(input("Enter number of variables: "))
    for index in range(0, nV):
        V.append(input("Enter Variable: "))

    T = []
    nT = int(input("Enter number of Terminals: "))
    for index in range(0, nT):
        T.append(input("Enter Terminals: "))

    P = []
    nP = int(input("Enter number of Production rules: "))
    for index in range(0, nP):
        P.append(input("Enter Production rules: "))

    S = input("Enter Start Symbol: ")

    checkLangauge(V, T, S, P)


if __name__ == "__main__":
    takeInput()
