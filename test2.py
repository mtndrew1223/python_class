import arithmetic as a

def multiply(num1, num2):
    product = num1 * num2
    result = a.add(product, product)
    return result
   
def main():
    num1 = 4
    num2 = 3
    answer = multiply(num1, num2)
    print("The answer is", answer)

if __name__ == "__main__":
    main()

def add(x, y):
    z = x + y
    return z