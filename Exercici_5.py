def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    resultat = [i for i in state if not i in 'aeiouyAEIOUYé']
    print(resultat)


if __name__ == '__main__':
    main()
