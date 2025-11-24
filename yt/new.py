Array = [2,7,11,15]
number = [2,7,11,15]
start = 0 
end = len(number)-1
target = 9
total = 0
while(start < end):
    total = number[start] + number[end]
    if(total==target):
        print([start+1, end+1])
        break
    elif(total > target):
        end-=1
    else:
        start+=1
