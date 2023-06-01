import numpy as np

def readFile():
    file_name = "cord.txt"
    with open(file_name, 'r') as file:
        lines = file.readlines()
    array_2d = [list(map(int, line.strip().replace(
        '(', '').replace(')', '').split(','))) for line in lines]
    return array_2d

order = 1
result = readFile()
data = np.delete(np.array(result), 0, 1)
if order == 1:
    sumX = np.zeros((len(result[0]) - 1))
    sumY = np.zeros((len(result[0]) - 1))
    sumXY = np.zeros((len(result[0]) - 1))
    sumX2 = np.zeros((len(result[0]) - 1))
    total = np.zeros((len(result[0]) - 1))

    for i in range(len(result)):
        sumX += result[i][0]
        sumY += data[i]
        sumXY += data[i] * result[i][0]
        sumX2 += result[i][0] * result[i][0]
        total += 1

    slope = (sumXY * total - sumX * sumY) / (sumX2 * total - sumX * sumX)
    intercept = (sumY - slope * sumX) / total
    print("y = " + str(slope) + "x + " + str(intercept))
else:
    summationList = []
    for i in range(order * 2):
        sum = 0
        for cord in result:
            sum += cord[0]**(i+1)
        summationList.append(sum)

    matrixR = np.zeros([order + 1, len(data[0])])
    for i in range(order + 1):
        row = np.zeros([len(data[0])])
        for j in range(len(result)):
            row += data[j] * result[j][0]**(i)
        matrixR[order - i] = row
    
    matrixL = []
    for i in range(order + 1):
        row = []
        for j in range(len(summationList) - i - 1, len(summationList) - order - 2 - i, -1):
            if j == -1:
                row.append(len(result))
            else:
                row.append(summationList[j])
        matrixL.append(row)
    
    matrixL = np.array(matrixL)
    inverseL = np.linalg.inv(matrixL)
    answer = np.matmul(inverseL, matrixR)
    
    ending = "y = "
    for i in range(order):
        ending += str(answer[i]) + "x^" + str(order - i) + " + "
    ending += str(answer[order])
    print(ending)