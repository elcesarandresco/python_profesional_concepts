# def run():
    
#     def multiplication(x):

#         def multiplicate(n):
#             return x * n

#         return multiplicate

#     time10 = multiplication(10)
#     time4 = multiplication(4)


#     print(time10(4))
#     print(time4(5))
#     print(time10(time4(3)))


# if __name__ == "__main__":
#     run()


# def run():
    
#     def palabra(x: str) -> str:
        
#         def multiplicador(y: int):
#             return x * y
        
#         return multiplicador
    
#     palabra1 = palabra("Platzi")
#     palabra2 = palabra("Hola")

#     print(palabra1(2))
#     print(palabra2(8))

# if __name__ == "__main__":
#     run()


def run():
    
    def multiplicador(n):
        def repeater(string):
            assert type(string) == str, "Usted solo puede ingresar string."
            return n * string
        
        return repeater


    multi1 = multiplicador(8)
    multi2 = multiplicador(3)

    print(multi1("Platzi"))
    print(multi2("Hola"))
    print(multi2(multi1("Su madre")))

if __name__ == "__main__":
    run()

