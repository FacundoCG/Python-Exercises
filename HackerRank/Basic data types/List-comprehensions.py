""" You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 

Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 0<=i<=x, 0<=j<=y, 0<=k<=z. 

Please use list comprehensions rather than multiple loops, as a learning exercise. """

if __name__ == '__main__':
    x: int = int(input())
    y: int = int(input())
    z: int = int(input())
    n: int = int(input())
    
    aristas_cubo: list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    
    aristas: list = []
    
    for l in aristas_cubo:
        if sum(l)!=n:
            aristas.append(l)
    
    print(aristas)
