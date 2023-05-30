def readFile():
    file_name = "cord.txt"
    with open(file_name, 'r') as file:
        lines = file.readlines()
        array_2d = [list(map(int, line.strip().replace('(', '').replace(')', '').split(','))) for line in lines]
        return array_2d

result = readFile()

sumX = 0;
sumY = 0;
sumXY = 0;
sumX2 = 0;
total = 0;
for cord in result:
    sumX += cord[0]
    sumY += cord[1]
    sumXY += cord[0] * cord[1]
    sumX2 += cord[0] * cord[0]
    total += 1

slope = (sumXY * total - sumX * sumY) / (sumX2 * total - sumX * sumX)
intercept = (sumY - slope * sumX) / total
print("y = " + str(slope) + "x + " + str(intercept))