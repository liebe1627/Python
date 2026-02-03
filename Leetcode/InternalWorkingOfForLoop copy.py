# str = ["flower","flow","flaunt"]

# for i in range(len(str)):
#     first = str[i]
#     print(str[i])
    
#     var = first[:1]
#     var2 = first[1:2]
      
#     print(var)
#     print(var2)


strs = ["flower","flow","flaunt"]
for i in range(len(strs[0])):
    s = strs[0][i]
    print(s)
    for t in strs:
        j=t[i]
        print(j)
  
            