def ordenamiento(vector):
    men = len(vector)
    for i in range(men-1):
        for j in range(men-1):
            if vector[j] > vector[j+1]:
                prueba = vector[j]
                vector[j] = vector[j+1]
                vector[j+1]= prueba
                
    print(vector)
    return vector
def vector():
    vector = []
    for i in range(1,8+1):
        num = int(input(f'Dame el numero {i}: '))
        vector.append(num)
    return vector
        
ni= vector()
ordenamiento(ni)

