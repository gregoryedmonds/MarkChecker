#Import modules required for program
import os
import statistics
import operator

#Checks if input file exists
def openFile(fileName):
    validFileName = None
    if(os.path.isfile(fileName)):
        validFileName = fileName
    return validFileName

#Runs function to create list if specified input file exists, else prints error message
def runFile(fileName):
    allowList = list()
    if(openFile(fileName) == fileName):
        allowList = createList(fileName)
    else:
        print("Error: file not found")
    return allowList

#Creates list for specified input file
def createList(inputFile):
    fullList = list()
    with open(inputFile) as data:
        for line in data:
            singleList = list()
            values = line.strip().split(',')
            singleList.append(values[0])
            for mark in values[1:]:
                if mark == "":
                    singleList.append(None)
                else:
                    singleList.append(int(mark))
            fullList.append(singleList)
        return fullList

#Creates normailised list of the marks of each student
def normalise(unitList, studentList):
    normaliseList = list()
    for student in studentList:
        updatedList = list()
        updatedList.append(student[0])
        row = 0
        for mark in student[1:]:
            if mark != None:
                mark = mark/unitList[row][1]
            updatedList.append(mark)
            row +=1
        normaliseList.append(updatedList)
    return normaliseList

#Determines the mean mark for each student from the normalised list
def getMean(normaliseList):
    studentMean = list()
    for student in normaliseList:
            tempList = list()
            noNone = list()
            for mark in student[1:]:
                if mark != None:
                    noNone.append(mark)
            meanValue = statistics.mean(noNone)
            tempList.append(meanValue)
            tempList.append(student[0])
            studentMean.append(tempList)
    return studentMean

#Sorts list of students by highest normalised mean mark (final mark)
def orderListBy(unorderedList):
    orderedList = sorted(unorderedList, key=operator.itemgetter(0), reverse=True)
    return orderedList

#Rounds final mark of each student to 3 decimal places
def roundListToThreeDecimal(meanList):
    for student in meanList:
        student[0] = round(student[0], 3)
    return meanList

#Prints output of students awith their corresponding final mark
def finalOutput(studentMean):
    roundedAndSortedList = orderListBy(studentMean)
    roundedAndSortedList = roundListToThreeDecimal(roundedAndSortedList)
    for student in roundedAndSortedList:
        print(student[1] + " " + str(student[0]))
        
#Prompts the user for the unit and student files and pulls together all other functions
def main():
    unitFile = input("Enter the units file name: ")
    unitList = runFile(unitFile)
    studentFile = input("Enter the students file name: ")
    studentList = runFile(studentFile)
    print("\n")
    normaliseList = normalise(unitList, studentList)
    studentMean = getMean(normaliseList)
    finalOutput(studentMean)
    
main()