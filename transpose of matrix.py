X = [[10,11,12],  
    [13,14,15],  
    [16,17,18]];  
result = [[0,0,0],  
         [0,0,0],  
         [0,0,0]];  
for i in range(len(X)):  
    for j in range(len(X[0])):  
        result[i][j] = X[j][i]  
for r in result:  
    print(r);  
