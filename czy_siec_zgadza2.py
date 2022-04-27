import ipaddress
import random

oktawa_1_siec = random.randint(0, 256)
oktawa_2_siec = random.randint(0, 256)
oktawa_3_siec = random.randint(0, 256)
oktawa_4_siec = random.randint(0, 256)


jedynki = random.randrange(8, 40, 8)
# print(jedynki)

siec = (f"{oktawa_1_siec}.{+ oktawa_2_siec}.{oktawa_3_siec}.{+ oktawa_4_siec}/{jedynki}")
print(f"adres sieci: {siec}")
ip = input("Podaj poprawny adres ip do sieci: ")
IPsplit = (ip.split("."))
# print(IPsplit)

if jedynki == 8:
    if oktawa_1_siec == int(IPsplit[0]):

       print("poprawna odpowiedz")
    else:
        # print(f"Nie poprawna odpowiedz")    
        # pass
        print(f"Nie poprawna odpowiedz \npoprawna odpowiedz powinna sie zaczynac: {oktawa_1_siec}.0.0.0/{jedynki}")
if jedynki == 16:
    if oktawa_1_siec == int(IPsplit[0]) and oktawa_2_siec == int(IPsplit[1]):
        print("poprawna odpowiedz")
    else:
        print(f"Nie poprawna odpowiedz \npoprawna odpowiedz powinna sie zaczynac: {oktawa_1_siec}. {+ oktawa_2_siec}.0.0/{jedynki}")
if jedynki == 24:
    if oktawa_1_siec == int(IPsplit[0]) and oktawa_2_siec == int(IPsplit[1]) and oktawa_3_siec == int(IPsplit[2]):
        print("poprawna odpowiedz")
    else:
        print(f"Nie poprawna odpowiedz \npoprawna odpowiedz powinna sie zaczynac: {oktawa_1_siec}. {+ oktawa_2_siec}.{oktawa_3_siec}.0/{jedynki}")
if jedynki == 32:
    if oktawa_1_siec == int(IPsplit[0]) and oktawa_2_siec == int(IPsplit[1]) and oktawa_3_siec == int(IPsplit[2]) and oktawa_4_siec == int(IPsplit[3]):
        print("poprawna odpowiedz")
    else:
        print(f"Nie poprawna odpowiedz \npoprawna odpowiedz powinna sie zaczynac: {oktawa_1_siec}. {+ oktawa_2_siec}.{oktawa_3_siec}.{oktawa_4_siec}/{jedynki}")        

# print(oktawa_1_siec, IPsplit[0])
# print(oktawa_2_siec, IPsplit[1])
# print(oktawa_3_siec,IPsplit[2])
# print(oktawa_4_siec, IPsplit[3])
