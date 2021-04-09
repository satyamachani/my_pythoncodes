x=int(input('number of num to be read'))
s= [None]*x
print("Enter the elements:")
for i in range(0,x):
    s[i]= int(input('Enter {0} element'.format(i+1)))
for i in range(0,x):
    print(s[i])
    
