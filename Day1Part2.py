puzzleInputfile = open("d1p1input.txt", "r") 
puzzleInputList = puzzleInputfile.read()
splitPuzzleList = puzzleInputList.split("\n")
for first in range(len(splitPuzzleList) -1):
    firstInSum = int(splitPuzzleList[first])
    for second in range(len(splitPuzzleList) -1):
        if first != second:
            secondInSum = int(splitPuzzleList[second])
            for third in range(len(splitPuzzleList) -1):
                if first != second != third:
                    thirdInSum = int(splitPuzzleList[third])
                    if firstInSum + secondInSum + thirdInSum == 2020:
                        print(f"{firstInSum * secondInSum * thirdInSum}")
                        quit()