def toString(List): 
	return ''.join(List) 

def combinations(a, l, r): 
	if l == r: 
		print(toString(a)) 
	else: 
		for i in range(l, r + 1): 
			a[l], a[i] = a[i], a[l] 
			combinations(a, l + 1, r) 
			a[l], a[i] = a[i], a[l]

string = "JOHN"
n = len(string) 
a = list(string) 
combinations(a, 0, n-1) 