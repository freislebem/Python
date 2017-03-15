from random import randint

count = 1
jogo = input("QUAL JOGO DESEJA CRIAR?: ")

while jogo.upper() == "MEGA":
    
    if jogo.upper() == "MEGA":
        while count <= 6:
            numGerado = randint(1,60);

            if count == 2:
                n2 = numGerado
                if numGerado == n1: count -= 1

            if count == 3:
                n3 = numGerado
                if numGerado == n2 or numGerado == n1: count -= 1

            if count == 4:
                n4 = numGerado
                if numGerado == n3 or numGerado == n2 or numGerado == n1: count -= 1

            if count == 5:
                n5 = numGerado
                if numGerado == n4 or numGerado == n3 or numGerado == n2 or numGerado == n1: count -= 1

            if count == 6:
                n6 = numGerado
                if numGerado == n5 or numGerado == n4 or numGerado == n3 or numGerado == n2 or numGerado == n1: count -= 1
                    
            if count == 1:
                n1 = numGerado

            count += 1            

    if count != 1:
        Lista = [n1,n2,n3,n4,n5,n6]
        print("Numeros gerados: ", sorted(Lista))
        count = 1
        
    jogo = input("QUAL JOGO DESEJA CRIAR?: ")            



