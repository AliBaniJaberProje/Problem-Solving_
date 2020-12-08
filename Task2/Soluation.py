test_data=['ray','seed','seeds','dog','deeds','dedses','moon','nom','rat','tar','tartar','rya','loop','pool']
dict_to_solv=dict()

for word in test_data:

    for char in word:
        dict_to_solv[char]=[z for z in test_data if char in z]

print(dict_to_solv)
input_text=input(" enter data :")
result_dec=dict()

for i in input_text:
    result_dec[i]=dict_to_solv[i]

size=len(result_dec)
tmp_list=[]
for i in result_dec:
    tmp_list.extend(result_dec[i])

#print(tmp_list)
my_out_put=[]
for i in list(result_dec[list(result_dec.keys())[0]]):
    if tmp_list.count(i)==len(list(result_dec.keys())):
        my_out_put.append(i)

print(my_out_put)
