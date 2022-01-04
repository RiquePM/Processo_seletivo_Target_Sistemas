def na_seq_fib(num):
    
    prim_term = 0                                         
    sec_term = 1

    if num == 0 or num == 1:
        print(f"O número {num} pertence à sequência de fibonacci")

    else:
        #print(prim_term, sec_term, end=" ") --> trecho usado para teste
        for i in range(2, num):
            n_term = prim_term + sec_term                           
            #print(n_term, end=" ") --> trecho usado para teste
            prim_term = sec_term
            sec_term = n_term
            if num < sec_term:
                msg = f"\nO número {num} não pertence à sequência de Fibonacci"
                break
            elif num == sec_term:
                msg = f"\nO número {num} pertence à sequência de Fibonacci"
                break 

    return print(msg)

def main():
    usr_input = int(input("Insira um número e veja se ele pertence à sequência de Fibonacci \n"))
    na_seq_fib(usr_input)

if __name__ == '__main__':
    main()
