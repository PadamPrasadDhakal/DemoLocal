def swap(a,b):
  c=a
  a=b
  b=c
  
  return a,b

a=swap(10,22)

print("a=",a[0])
print("b=",a[1])