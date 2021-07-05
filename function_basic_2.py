# 1
# def countDown(num):
#     newList = []
#     for x in range(num, -1, -1):
#         newList.append(x)
#         if x == 0:
#             return newList

# answer = countDown(5)
# print(answer)

# 2
# def printAndReturn(list):
#     print(list[0])
#     return list[1]

# print(printAndReturn([1, 2]))

# 3
# def firstPlusLength(list):
#     return list[0] + len(list)

# print(firstPlusLength([7, 5, 7, 4, 3, 4, 8]))

# 4
# def valuesGreaterThenSecond(list):
#     newList = []
#     for x in list:
#         if len(list) < 2:
#             return False
#         elif x > list[1]:
#             newList.append(x)
#             continue
#     print(len(newList))
#     return newList

# print(valuesGreaterThenSecond([2, 4, 7, 8, 58]))
# print(valuesGreaterThenSecond([2]))

# 5
# def thisLengthThatLength(size, value):
#     newList = []
#     for x in range(size):
#         newList.append(value)
#         continue
#     return newList


# print(thisLengthThatLength(4, 12))
