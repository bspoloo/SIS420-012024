from math import inf
superficies = [150,200,500,550,320,300,800,210,180,350];
precios = [4500,12000, 130000, 35000,190000,200000,160000,50000,75000,210000];

parametros_a = [];
parametros_b = [];

for ix, x in enumerate(superficies):
    mejor_deferencia = inf;
    mejor_a = 0;
    mejor_b = 0;
    
    for a in range(-100000,10,100):
        for b in range(-100000, 10, 100):
            y_hat = a + b*x;
            #print(y_hat);
            diferencia_actual = abs(y_hat - precios[ix]);
            
            if diferencia_actual < mejor_deferencia:
                mejor_deferencia = diferencia_actual;
                mejor_a = a;
                mejor_b = b;
print(f"Los mejores coheficiente en la encuacion de la linea recta, para x={x}, son: para a: {mejor_a} y para b: {mejor_b}");

parametros_a.append(mejor_a);
parametros_b.append(mejor_b);

# Imprimir los resultados finales
print("Resultados finales:")
print("Mejores valores para a:", parametros_a)
print("Mejores valores para b:", parametros_b)