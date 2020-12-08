test_data=[1,6,4,3,1,6,6,6,6]

dict_to_solv=dict()
for i in test_data:
    dict_to_solv[i]=i
print(dict_to_solv)
size=len(dict_to_solv.keys())
keys_sorted=sorted(dict_to_solv.keys())
print(dict_to_solv)
print(size)
count_bounas=1
for i in keys_sorted:
    dict_to_solv.update({i:count_bounas})
    count_bounas=count_bounas+1
print(dict_to_solv)

for i in test_data:
    print(f" {i}  : {dict_to_solv[i]}")




