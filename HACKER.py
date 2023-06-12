#!/usr/bin/env python3

 
import os

os.system("clear")
os.system("figlet HACKER")

print("""

gelismis hacker araci

*********************************

1)site haqqinda melumat
2)hizli port tarama
3)version bilgisi
4)sitenin ip adresin bulma
5)pishing tool
6)sqlmap ile sitenin databases cekme

*********************************

yuxaridakilardan birini secin zəhmət olmasa:)

""")

islemno = input("herhangi bir sayi girin: ")

if islemno=="1":
	hedefsite = input("hedef site giriniz: ")
	os.system("whois "+hedefsite)

elif islemno=="2":
	hedefsite = input("hedef site giriniz: ")
	os.system("nmap "+hedefsite)
elif islemno=="3":
	hedefsite = input("hedef site giriniz: ")
	os.system("nmap -sV "+hedefsite)

elif islemno=="4":
	hedefsite = input("hedef site giriniz: ")
	os.system("ping "+hedefsite)

elif islemno=="5":
	hedefsite = input("sadece entere basin: ")
	os.system("zphisher "+hedefsite)
elif islemno=="6":
	hedefsite = input("hedef site girin: ")
	os.system("cd sqlmap && python sqlmap.py -u "+ hedefsite)

else:
	os.system("clear")
	os.system("figlet HATA")
	print("""yanlis secim secdiniz

************************************************
program baglanir.../""")
