numberoflines = 0
file = 'data.dat'

with open(file) as f:    
        lines = f.readlines()   
        for line in lines:
                zero = line.count('0') 
                one = line.count('1')   
                if (zero % 3 == 0) or (one % 2 == 0):
                        numberoflines = numberoflines + 1

f.close()
print(numberoflines)