result= 0;
parameters =[];

def findAandB(min, max, feacture, label):
    a = 0;
    b= 0;
    for i in range(min,max):
        
        for j in range(min,max):
            
            valor = j + (i*feacture)
            if valor <= label:
                result = valor;
                a=j;
                b=i;
    return [a,b];

print("the result is: ");
print(findAandB(-1000,1000,2104,460));
