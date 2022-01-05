ctemp = input("vui lòng nhập độ c cần chuyển đổi:")
while ctemp != "c":
    if  ctemp.isdigit():
        F = 9/5 * int(ctemp) + 32
        print("Độ F là:" + str(F))
    else:
        print("vui lòng nhập số")
    ctemp = input("vui lòng nhập độ c cần chuyển đổi:")  
    if ctemp == "c":
        exit
    
    