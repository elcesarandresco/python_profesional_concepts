def phone(func):
    def wrapper(*args, **kwags):
        brand: str = input("Escribe la marca de tu teléfono: ")
        ref = func(*args, **kwags)
        print("Tu teléfono es: " + brand + " " + ref)
    return wrapper 

@phone
def reference():
    ref = input("Ecribe la referencia de tu teléfono: ")
    return ref

def run():
    
    reference()


if __name__ == "__main__":
    run()