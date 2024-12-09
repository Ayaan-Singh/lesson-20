
def palin(r):
 s = len(r)-1
 e = 0
 while (e<s):
  if (r[s] != r[e]):
   return False
  s -=1
  e +=1
 return True


r = (9,5,4,3,7,2,5,3,4)
print (palin(r))

