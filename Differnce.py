A = 10
B = 10
print(id(A))
print(id(B))

a = [10]
b = [10]
print(id(a))
print(id(b))

# Result
# 140723283510472
# 140723283510472
# 2239517188544
# 2239517335808

#Python sometimes reuses memory for immutable objects (as an optimization)
#Mutable objects do get new memory address each time