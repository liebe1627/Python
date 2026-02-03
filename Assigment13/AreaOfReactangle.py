def Area(l,w):
    area = 0
    area = l*w
    print("Area reactangle",area)

def main():
    Length = int(input("Length of the reactangle: "))
    width = int(input("Width of the reactangle: "))
    Area(Length,width)

if __name__=="__main__":
    main()