import ipaddress
import random


oktawa_1_siec = random.randint(0, 256)
oktawa_2_siec = random.randint(0, 256)

siec = (f"{oktawa_1_siec}.{+ oktawa_2_siec}.0.0/16")
print(f"adres sieci: {siec}")
ip = input("Podaj poprawny adres ip do sieci: ")

if ip in siec:
    print("poprawna odpowiedz")
else:
    print(f"Nie poprawna odpowiedz \npoprawna odpowiedz miala by w pierwszych oktawach {oktawa_1_siec}. {+ oktawa_2_siec}.")

