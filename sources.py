# import 
import math

def solve():
    # input factor
    print("Phương trình mặc định: ax^2 + bx + c = 0")
    print(".")
    a = int(input("Nhập hệ số bậc hai: "))
    b = int(input("Nhập hệ số bậc nhất: "))
    c = int(input("Nhập hằng số tự do: "))

    # delta
    delta = b * b - 4 * a * c 
    if delta > 0:
        x1 = (math.sqrt(delta) - b) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a) 
        print("Phương trình tồn tại 2 nghiệm: x1 = " + str(x1) + ", x2 = " + str(x2))
    elif delta == 0:
        x = -b / 2 * a
        print("Phương trình có nghiệm kép: x = " + x)
    else:
        print("Phương trình vô nghiệm")
    ask()

def ask():
    choice = input("Tiếp tục? (Y/n): ")
    if choice == "Y" or choice == "y":
        print(".")
        solve()
    else:
        return 0
solve()
