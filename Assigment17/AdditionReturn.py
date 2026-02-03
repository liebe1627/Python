def sum_of_digits(No):
    total = 0
    while No > 0:
        digit = No % 10      
        total = total + digit
        No = No // 10       
    return total

def main():
    No = int(input("Enter a number: "))
    result = sum_of_digits(No)
    print("The sum is:", result)

if __name__ == "__main__":
    main()
