def rev_string(palavra):
    return print(palavra[::-1])

def main():
    usr_input = str(input("Digite uma palavra: \n"))
    print("Aqui está sua palavra invertida: ")
    rev_string(usr_input)

if __name__ == '__main__':
    main()