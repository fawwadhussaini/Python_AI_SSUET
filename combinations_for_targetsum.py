import itertools


all_combinations = []
dic = {}
target = 5
result = {}
all_combinations = list(itertools.combinations([1,2,3,4,], 2))
print (all_combinations)

for c in all_combinations:
    dic[c]= (c[0]+c[1])
    if dic[c] > target:
        result[c] = dic[c]
print (result)


