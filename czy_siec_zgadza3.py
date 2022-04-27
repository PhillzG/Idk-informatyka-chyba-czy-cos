import ipaddress
import random

siec = str(ipaddress.ip_network(random.randint(0, 4294967295)))
print(siec)

ip = input("Podaj poprawny adres ip do sieci: ")

if ip in siec:
    print("poprawna odpowiedz")
else:
    print(f"Nie poprawna odpowiedz")