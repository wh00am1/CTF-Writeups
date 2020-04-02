count = 0
file = 'data.dat'

with open(file) as f:    
        l = f.readlines()   
        for line in l:
                zero = line.count('0') 
                one = line.count('1')   
                if (zero % 3 == 0) or (one % 2 == 0):
                        count = count + 1

f.close()
print(str(count))