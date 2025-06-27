def fibonacci(a):
	if a == 0: return  0
	elif a == 1: return  1 
	else:
		return fibonacci(a-1) + fibonacci(a-2)

for i in range(10):
    print(f"fibonacci({i}) = {fibonacci(i)}")
