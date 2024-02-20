import numpy as np;

#creation of the array mxm 1
array_1 = np.array([
    [1,2,3,4],
    [5,5,7,8],
    [9,10,11,12],
    [13,14,15,16]
],int);

print(array_1);

#creation of the array MxM 2
array_2 = np.array([
    [2,5,64,5],
    [5,6,1,0],
    [9,120,23,34],
    [86,90,78,76]
],int);

array_3 = np.array([
    [1,8,-2],
    [0,-1,8],
    [1,2,1],
],int);

array_4 = np.array([1,8,2],int);
array_5 = np.array([1,8,5],int);


print(array_2);
#Addition and Substraction of arrays MxM
#Addition of arrays MxM
Addition_1 = array_1 + array_2;
print("the Addition of the arrays MxM is:");
print(Addition_1);

#Substraction of arrays MxM
Substraction_1 = array_1 - array_2;
print("the Substraction of the arrays MxM is:");
print(Substraction_1);

#Substraction of arrays MxM
Substraction_1 = array_1 - array_2;
print("the Substraction of the arrays MxM is:");
print(Substraction_1);

#Multiplication of arrays MxM
Multiplication_1 = np.dot(array_1,array_2);
print("the Multiplication of the arrays MxM is:");
print(Multiplication_1);

#Multiplication by a scalar
Multiplication_Scalar = 5 * array_1;
print("the Multiplication Scalar of the array 1 MxM is:");
print(Multiplication_Scalar);

#Array transposition
transposition_arrays = [list(row) for row in zip(*array_1)];
print("the Array 1 transposition MxM is:");
print(transposition_arrays);

#Determinant of a array MxM
determinant_array = np.linalg.det(array_3);
print("the Determinant of a arrays 3 MxM is:");
print(determinant_array);

#Inverse of a array MxM
inverse = np.linalg.inv(array_3);
print("the inverse of the array 3 MxM is:");
print(inverse);

#Division of a array 1 by array 2
inverse2 = np.linalg.inv(array_2);
division = np.dot(array_1, inverse2);
print("the division of the array 1 by array 2 MxM is:");
print(division);

#Scalar product
scalar = np.dot(array_4, array_5);
print("the product scalar of the array 4 by array 5 MxM is:");
print(scalar);

#vector product
vectorial = np.cross(array_4, array_5);
print("the vector product of the array 4 by array 5 MxM is:");
print(vectorial);
