#open txt file, read file into a list, split individual items and add them to new list
puzzleInputfile = open("d1p1input.txt", "r") 
puzzleInputList = puzzleInputfile.read()
splitPuzzleList = puzzleInputList.split("\n")
#loop through entire list
for first in range(len(splitPuzzleList) -1):
    firstInSum = int(splitPuzzleList[first])
    #loop through list a second time to find second number in sum
    for second in range(len(splitPuzzleList) -1):
        #ensure you aren't adding the same item in the list together
        if first != second:
            secondInSum = int(splitPuzzleList[second])
            #if the two numbers add up to 2020 then multiple them together, print result and quit the program
            if firstInSum + secondInSum == 2020:
                print(f"{firstInSum * secondInSum}")
                quit()

