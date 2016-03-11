import math

def checkSquare(n):
    """check square or not

    if square return 1
    if not    return 0
    """
    root = math.sqrt(n)
    
    if root == root//1.0:
        return 1
    
    return 0


print checkSquare(25)

