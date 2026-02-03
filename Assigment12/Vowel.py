def vowel(char):
    listofVowel = ['A','a','E','e','I','i','O','o','U','u']
    lenoflist = len(listofVowel)
    # print(lenoflist)
    if char in listofVowel:
        print("match")
    else:
        print("not a match")

def main():
    char = input("Enter a character: ")
    vowel(char)

if __name__=="__main__":
    main()