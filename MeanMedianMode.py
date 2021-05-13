import csv
from collections import Counter
from typing import Counter

with open("Height&Weight.csv",newline="")as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    num = file_data[i][1]
    new_data.append(float(num))
# for mode
data = Counter(new_data)
modeDataForRange = {
    '50-60':0,
    '60-70':0,
    '70-80':0,
}

for height,occurrence in data.items():
    if(50<float(height)<60):
        modeDataForRange['50-60']+=occurrence
    elif(60<float(height)<70):
        modeDataForRange['60-70']+=occurrence
    elif(70<float(height)<80):
        modeDataForRange['70-80']+=occurrence

mode_range,mode_occurrence = 0,0
for range,occurrence in modeDataForRange.items():
    if(occurrence>mode_occurrence):
        mode_range,mode_occurrence = [int(range.split('-')[0]),int(range.split('-')[1])],occurrence


mode = float ((mode_range[0]+mode_range[1])/2)

#for median

nl = len(new_data)
new_data.sort()
if(nl%2==0):
    median1 = float(new_data[nl//2])
    median2 = float(new_data[nl//-1])
    median = (median1 + median2/2)
else:
    median = new_data[nl//2]

# for mean
n = len(new_data)
sum = 0

for x in new_data:
    sum+=x

mean = sum/n

print(mean)
print(str(mode))
print(median)