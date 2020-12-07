
def swap_tow_number_with_out_use_tmp(inputdata):
    inputdata["num1"]=inputdata["num1"]+inputdata["num2"]
    inputdata["num2"]=inputdata["num1"]-inputdata["num2"]
    inputdata["num1"]=inputdata["num1"]-inputdata["num2"]
    return {"num1":inputdata["num1"],"num2":inputdata["num2"]}



if __name__=="__main__":
    my_var={"num1":10,"num2":20}
    print(f"befor swap {my_var}")
    my_var=swap_tow_number_with_out_use_tmp(my_var)
    print(f"after swap {my_var}")


