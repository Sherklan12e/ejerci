for i in range(2,101):
    primo = True
    for a in range(2,i):
        if i % a ==0:
            primo= False
            break
    if primo==True:
        print('x: ', i)