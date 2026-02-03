# str = ["flower","flow","flaunt"]

# for i in range(len(str)):
#     first = str[i]
#     print(str[i])
    
#     var = first[:1]
#     var2 = first[1:2]
      
#     print(var)
#     print(var2)
strs = []
def longestCommonPrefix():
    res=""
    if not strs:
        return 
    if len(strs)==0:
        return ""
    a = min(strs, key=len)
    l = len(a)
    for i in range(l):
        for s in strs:
            if s[i] != a[i]:
                return res
        res +=a[i]
    return(res)
l = longestCommonPrefix()
print(l)
print("top level")
