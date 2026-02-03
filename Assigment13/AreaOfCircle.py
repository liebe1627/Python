def Area(r):
    Pi = 3.142
    radiussquare = r**2
    area = Pi*radiussquare
    print("Area of circle is: ",area)

def main():
    r = int(input("Enter the radius: "))
    Area(r)

if __name__=="__main__":
    main()