import math 
for i in range(1,135):
    ID = '18DCS'
    for j in range(2-int(math.log10(i))):
        ID=ID + '0'
    ID=ID + str(i)
    print(ID)
    