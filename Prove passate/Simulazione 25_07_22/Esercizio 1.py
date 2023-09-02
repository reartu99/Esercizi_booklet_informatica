""""
Scrivere una funzione Python “ToDecimal” che converte una stringa binaria in un numero decimale. 
Se la stringa non contiene solo zeri e uni bisogna lanciare un’eccezione. 
Inoltre, scrivere una funzione Python “DivisibleByTwoAndThree” che dato un numero decimale N restituisce 
se è divisibile per 2 e per 3. Infine, scrivere un breve main che legge una stringa di zeri e uni da tastiera, 
la converte in un numero decimale e stampa a video se questo numero è divisibile per 2 e per 3.
"""""


def todecimal(stri):
    sums = 0
    count = 0
    for item in stri:
        if int(item) != 0 and int(item) != 1:
            raise Exception("Non binario")

    for item in stri[::-1]:
        sums += (2*int(item))**count
        count += 1

    print(sums)
    return sums


def divs(n):
    if n % 2 == 0 and n % 3 == 0:
        return True
    return False
