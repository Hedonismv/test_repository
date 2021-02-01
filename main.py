from classes import *

def main():
    circle = Circle(5)
    triangle = Triangle(4, 4, 4)
    print(circle.perimeter())
    print(circle.square())
    list_f = [circle, triangle]
    for f in list_f:
        print(f)




if __name__ == '__main__':
    main()
