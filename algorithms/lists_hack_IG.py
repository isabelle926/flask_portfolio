# Challenge 1: Name the variable types of the following variables. Print them out into console in the format "Variable: Variable Type" (might have to google "how to print variables in python")

integer = 3
string = "Mr. Mortensen"
character = 'f'
float = 0.4
print(integer, ": Variable Type", type(integer))
print(string, ": Variable Type", type(string))
print(character, ": Variable Type", type(character))
print(float, ": Variable Type", type(float))


# Challenge 2: Pass list1 into list2. However, list2 must contain the elements of list1 in order. Print list2. +0.3 if you can create a function to order a list and can display it on your website

list1 = [5, 3, 4, 1, 2]
list2 = []
# requirements
# list2.append(list1[3])
# list2.append(list1[4])
# list2.append(list1[1])
# list2.append(list1[2])
# list2.append(list1[0])
# extra credit
def orderList (firstList, finalList):
    for i in firstList:
        finalList.append(min(firstList))
        firstList.remove(min(firstList))
    print(finalList)

orderList(list1, list2)
# Challenge 3: Find a way to add 3 to each element in the array. Then, take the average of the array and put it into the variable avg. +0.2 if you can turn this into a function and display it on your website.

averageList = [23, 41, 90, 55, 71, 83]

averageList[0] += 3
averageList[1] += 3
averageList[2] += 3
averageList[3] += 3
averageList[4] += 3

#print(averageList)

#avg = 0

#for i in averageList:
    #avg += i

#avg = avg/len(averageList)

#print(avg)
# extra credit
def averageListfun (list):
    avg = 0
    for i in list:
        avg += i
    avg = avg/len(list)
    print(avg)

averageListfun(averageList)