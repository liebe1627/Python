str = ["flower","flow","flaunt"]
str = ["flower","flow","flaunt"]
s = iter(str)
print(s)
# C:\PythonPrograms\Python\Leetcode>python Practice.py
# <list_iterator object at 0x000001F2CC9FB880>

#next return current element
#if i say again next(s) again it will give us the second element
v=next(s)
print(v)
# C:\PythonPrograms\Python\Leetcode>python Practice.py
# <list_iterator object at 0x0000029C2BC2B8B0>
# flower


#for i in range(len(str)):#
#  print(str[i])
    # for j in str[i]:
    #     print(j)
