def addition(a, b):
    return a + b

def division(a, b):
    if b == 0:
        raise ValueError("Division by zero!")
    return a / b

if __name__ == "__main__":
    print("Résultat addition :", addition(3, 5))
    print("Résultat division :", division(10, 2))
