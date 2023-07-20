def factor(num):
    i=1
    count=0
    while i*i <=num:
        if num%i==0:
            if num/i==i:
                count+=1
            else:
                count+=2
        i+=1
    return count

def FactorsSort(array):
    array.sort(key=lambda num:(factor(num),num)) #to sort based on factors count
    return array

array=list(map(int,input().split()))
print(FactorsSort(array))