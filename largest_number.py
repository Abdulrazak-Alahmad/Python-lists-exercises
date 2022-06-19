# Input : list1 = [10, 20, 4]
# Output : 20

# Input : list2 = [20, 10, 20, 4, 100]
# Output : 100

list=[1,2,3,4,5,6,7]
def max_num(list):
    max=0
    for num in list:
        if num>max:
            max=num
    return max

print(max_num(list))
