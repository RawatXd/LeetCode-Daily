number = [12,15,14,19,16,25,89,2]
max_val = number[0]
min_val = number[0]
for n in number:
    if n > max_val:
        max_val = n
    elif n < min_val : 
        min_val = n
print("Maximum number is:",max_val)
print("Minimum number is:",min_val)
