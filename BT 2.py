# 1 tính giá trị tổng 2 biến 

def myfunc1():
    a = input("nhập biến a: ")
    b = input("Nhập biến b: ")
    c = int(a) + int(b)
    print("Tổng 2 biến: " + str(c))

myfunc1()

# 2 viết function in ra dòng chữ hello word 
def myfunc2():
    
    print("Hello world")

myfunc2()


# 3 viết ct tính toán cộng trừ nhân chia in ra màn hình với yêu cầu ng dùng nhập biến thứ nhất cộng trừ nhân hoặc chia ( số )
# Biến thứ 2 cộng trừ nhân chia ( chữ )
# Biến 3 nhập biến ng ta mún cộng trừ nhân chia khi bấm enter sẽ ra kq 
import numbers
from pydoc import text
from unittest.util import strclass


def myfunc3():
    num1 = input("Biến thứ 1: ")
    num2 = input("Biến thứ 2: ")
    total = input("nhập phép tính: ")

    if  num1.isdigit() and num2.isdigit() and total == "cộng":       
        cộng = float(num1) + float(num2)
        print("phép cộng: " + str(cộng))

    elif num1.isdigit() and num2.isdigit() and total == "trừ":
         trừ = float(num1) - float(num2)
         print("phép trừ: " + str(trừ))

    elif num1.isdigit() and num2.isdigit() and total == "nhân":
         nhân = float(num1) * float(num2)
         print("phép nhân: " + str(nhân))

    elif num1.isdigit() and num2.isdigit() and total == "chia":
         chia = float(num1) / float(num2)
         print("phép chia: " + str(chia))

    else:
        print("Giá trị biến 1, 2 hoặc phép tính của bạn đã nhập sai")


myfunc3()

# 4 viết ct tính toán tuổi có đủ vị thành niên k 

def myfunc4():
    year = input("Nhập năm sinh của bản thân: ")
    if year.isdigit():
        kq = 2022 - int(year)
        kq >= 18
        print(str(kq) + " tuổi rồi, đủ tuổi đi tù rồi")
    else:
        print("năm sinh mà nhập chữ bị ngu hả th mẹt lìn")
myfunc4()
