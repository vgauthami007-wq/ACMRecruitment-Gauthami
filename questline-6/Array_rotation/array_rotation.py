l = [1,2,3,4,5,6,7]
n = len(l)

def arrayrotation(k):
    L = [0] * n   
    for i in range(n):
        new= (i + k) % n   
        L[new] = l[i]
    return L


#1
k = 2
print("original array =", l)
print("array when rotated by", k, "=", arrayrotation(k))

#2
k = 4
print("original array =", l)
print("array when rotated by", k, "=", arrayrotation(k))
