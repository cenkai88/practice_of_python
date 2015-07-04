L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print sorted(L,key=lambda t:t[0])
print sorted(L,key=lambda t:t[1], reverse=True)