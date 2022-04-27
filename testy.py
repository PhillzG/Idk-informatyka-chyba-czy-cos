import random
import ipaddress
# cos = secrets.randbelow(10)
# print(cos)

siec = int(ipaddress.IPv4Network('12.34.256.10/32'))
# siec = input("podaj siec ")
try:
    siec2 = ipaddress.IPv4Network(siec)
except ipaddress.AddressValueError:
    print("Nieprawidlowa wartosc bitow sieci")
except ValueError:
    print("Nieprawidłowa ilosc jedynek sieci")

print(siec)   

# ip = str(ipaddress.IPv4Address('12.256.12.12'))
# # ip = input("Podaj adres IP: ")
# try:
#     ip3 = ipaddress.IPv4Address(ip)
# except ipaddress.AddressValueError:
#     print("Nieprawidłowy adres")
# print (ip)
