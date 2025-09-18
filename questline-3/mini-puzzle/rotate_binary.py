def rotatebinary(b,k):
    k=k%(len(b))
    final=b[-k:]+b[:-k]
    return int(final,2)



#usage example
binary='1011'
k=2
print(rotatebinary(binary,k))

#example2
binary='101001'
k=8
print(rotatebinary(binary,k))
