def Count(No):
   count = 0
   if No == 0:
      print("Count is 1")
   else:
      while No>0:
         count+=1
         No = No//10
      print(count)

def main():
   No = int(input("Enter value: "))
   Count(No)

if __name__ == "__main__":
   main()
       