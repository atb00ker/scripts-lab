def seperator:
    enrollNumbers = open('records.txt', "r").read().split(' ')
    for current in range(0,len(enrollNumbers)):
        for counter in range(current+1, len(enrollNumbers)):
            if enrollNumbers[current] == enrollNumbers[counter]:
                print enrollNumbers[counter]

if __name__ == "__main__":
    seperator()
