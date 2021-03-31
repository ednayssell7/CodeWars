def positive_sum(arr):
    # Your code here
    for i in arr:
        if  i>0:
            p_sum= sum(x for x in arr if x > 0)
            return print(p_sum)
        elif i<=0:
            return print("0")
    if len(arr)==0:
            return print("0")
    
array = [1, -4, 7, 12]
array1 = [0]
array2 = []
result_positive= positive_sum(array)
print= result_positive