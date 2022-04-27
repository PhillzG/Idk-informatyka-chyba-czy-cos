import ipaddress
import random

# losowanie = (random.randint(0, 4294967295))
# print (int(losowanie))
# print (bin(losowanie))
# ip_liczba = str(ipaddress.ip_address(losowanie))


# for i in range(0,4):
#     i = (random.randint(0, 300))

oktawa1 = (random.randint(0, 350))
oktawa2 = (random.randint(0, 350))
oktawa3 = (random.randint(0, 350))
oktawa4 = (random.randint(0, 350))
adres_ip = f"{oktawa1}.{+ oktawa2}.{+ oktawa3}.{+ oktawa4}"
# adres = oktawa1 + oktawa2 + oktawa3 + oktawa4
# print (adres_ip)
# print(adres)

# ip = str(ipaddress.ip_address(adres))
# print(ip)
# print(int(ip))

zmienna = input(f"czy podany adres jest poprawny: {adres_ip}  ")

if zmienna == "t" or "T" or "tak" or "TAK" or "Tak":
    if oktawa1 < 256 or oktawa2 < 256 or oktawa3 < 256 or oktawa4 < 256:
        print("Nie poprawne")
    else:
        pass

if zmienna == "n" or "N" or "nie" or "NIE" or "Nie":
    if oktawa1 > 256 or oktawa2 > 256 or oktawa3 > 256 or oktawa4 > 256:
        print("poprawne")
    else:
        pass



# pytanie = input(f"Czy podany adress jest poprawny: {ip_liczba}")

# try:
#     ip3 = ipaddress.IPv4Address(ip_liczba)

# except ipaddress.AddressValueError:
#     print("Nieprawidłowy adres")


# print(ip_liczba)    

