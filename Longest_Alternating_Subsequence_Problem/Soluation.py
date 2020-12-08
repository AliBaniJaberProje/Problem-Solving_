test_data=[8,9,6,4,5,7,3,2,4]
my_result=list()
my_result.append(test_data[0])

if __name__=="__main__":
    my_index=0
    flage=False # A[i] < A[i++]
    counter =1
    for i in range(len(test_data)):
        if i==0:
            continue
        if not flage:
                if  test_data[i] > test_data[my_index]:
                    my_result.append(test_data[i])
                    counter += 1
                    my_index = i
                    flage = not flage
                    continue
        else:
                if  test_data[i] < test_data[my_index]:
                    my_result.append(test_data[i])
                    counter += 1
                    my_index = i
                    flage=not flage
                    continue


    print(counter)
    print(my_result)

