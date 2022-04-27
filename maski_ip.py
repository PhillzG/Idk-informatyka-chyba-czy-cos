import ipaddress
import random


siec = ipaddress.IPv4Network('12.12.0.0/16')
print(siec)

# # def ip_generator():
#     numer = random.randint(0,256)
#     return numer

# print(f'IP jest: {ip_generator()}.{ip_generator()}.{ip_generator()}.{ip_generator()}')

# ip = random.randint(0, 4294967295)
ip_liczba = str(ipaddress.ip_address(random.randint(0, 4294967295)))
try:
    ip3 = ipaddress.IPv4Address(ip_liczba)
except ipaddress.AddressValueError:
    print("Nieprawidłowy adres")

print(ip_liczba)    

# ip1 = ipaddress.IPv4Address('255.255.255.255')
# try:
#     ip3 = ipaddress.IPv4Address(ip1)
# except ipaddress.AddressValueError:
#     print("Nieprawidłowy adres")

# ip1_liczba = int(ip1)

# print(ip1_liczba)