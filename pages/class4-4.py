def hello():
    print("hello")


def hello2(name):
    print("hello", name)


def my_max(a, b):
    if a > b:
        return a
    else:
        return b


def calculate_circle_area(r, pi=3.14, scale=1):
    return (r * scale) ** 2 * pi


hello()
hello2("Mike")
print(my_max(10, 20))
print(calculate_circle_area(10))
print(calculate_circle_area(10, scale=2))
print(calculate_circle_area(10, 3.14159, 2))

print("-" * 20)

length = 5
area = 123


def calculate_square_area():
    # print("面積是", area) #會報錯
    area = length**2
    print("面積是", area)


def calculate_square_area2():
    area = length**2
    return area


def calculate_square_area3():
    global area
    area = length**2


length = 10
calculate_square_area()
print(calculate_square_area2())
calculate_square_area3()
print(area)


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


x1, y1, x2, y2 = (
    int(input("請輸入x1座標值: ")),
    int(input("請輸入y1座標值: ")),
    int(input("請輸入x2座標值: ")),
    int(input("請輸入y2座標值: ")),
)
print(distance(x1, y1, x2, y2))
