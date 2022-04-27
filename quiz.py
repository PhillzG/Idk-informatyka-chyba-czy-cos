

#PYTANIE 1

pytanie_1 = str(input("PYTANIE 1: \n Z ilu bitów składa się adres IP? \n A: 12  B: 16  C: 24  D: 32      "))

if pytanie_1 == "D":
    print(True)
else:
    print(False)

#PYTANIE 2 

pytanie_2 = str(input("PYTANIE 2: \n Z ilu bajtów składa się adres IP? \n A: 4  B: 8  C: 16  D: 32      "))

if pytanie_2 == "A":
    print(True)
else:
    print(False)


#PYTANIE 3 

pytanie_3 = str(input("PYTANIE 3: \n Przy pomocy jakiego znaku oddzielamy między sobą oktety w zapisie adresu IP? A: Przecinek  B: Kropka  C: Myślink  D: Spacja      "))

if pytanie_3 == "B":
    print(True)
else:
    print(False)



#PYTANIE 4 

pytanie_4 = str(input("PYTANIE 4: \n W jakim systemie liczbowym zapisany jest adres IP, jeśli jest wysyłany do innego hosta? A: Binarny  B: Ósemkowy  C: Dziesiętny  D: Szesnastkowy      "))

if pytanie_4 == "A":
    print(True)
else:
    print(False)



#PYTANIE 5

pytanie_5 = str(input("PYTANIE 5: \n W której odpowiedzi maska podsieci jest poprawnie zapisana? \n A: 255.255.0.0 B: 255.255.255.0  C: 255.255.255.255  D: 255.0.255.255 )      "))

if pytanie_5 == "B":
    print(True)
else:
    print(False)



#PYTANIE 6

pytanie_6 = str(input("PYTANIE 6: \n Który z podancyh adresów IP nie jest poprawny? \n A: 192.168.1.120 B: 192.168.125.120  C: 192.168.256.120  D: 192.172.221.120 )      "))

if pytanie_6 == "C":
    print(True)
else:
    print(False)



#PYTANIE 7

pytanie_7 = str(input("PYTANIE 7: \n W którym oktecie zapisany jest adres hosta? \n A: Pierwszym B: Drugim  C: Trzecim  D: Czawrtym )      "))

if pytanie_7 == "D":
    print(True)
else:
    print(False)



#PYTANIE 8

pytanie_8 = str(input("PYTANIE 8: \n Ile bitów maksymalnie może zająćadres sieci? \n A: Jeden B: Dwa  C: Trzy  D: Cztery )      "))

if pytanie_8 == "C":
    print(True)
else:
    print(False)



#PYTANIE 9

pytanie_9 = str(input("PYTANIE 9: \n Ile maksymalnie 'jedynek' może zawierać skrócony zapis maski? \n A: 24 B: 22  C: 16  D: 255 )      "))

if pytanie_9 == "A":
    print(True)
else:
    print(False)





#PYTANIE 10

pytanie_10 = str(input("PYTANIE 10: \n Czy zera muszą znajdować się pomiędzy jednykami w zapisie maski? \n A: Tak, muszą. B: Nie, nie mogą.  C: W masce mogą, ale w IP nie.  D: Nie, ale muszą występować parami. )      "))

if pytanie_10 == "B":
    print(True)
else:
    print(False)