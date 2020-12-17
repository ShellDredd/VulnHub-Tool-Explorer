#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Autor: Alexandre Varela Sixto
# Apodo: || ShellDredd || 
# Twitter: @ShellDredd

#Importación de Liberías y requirimientos:
import requests, subprocess, time, feedparser, re
from bs4 import BeautifulSoup
from subprocess import call

#Definición de paleta de colores:
cs_color='\033[0;m'
def charizar(skk): print("\x1b[1;91m {}\033[01m" .format(skk) + cs_color)
def bulbasur(skk): print("\x1b[1;32m {}\033[01m" .format(skk) + cs_color)
verde="\x1b[1;32m"
rojo="\x1b[1;91m"
moradito="\x1b[1;35m"

#Cabecera cargando:
print (moradito + "\/\/\/\/" + verde + "····  🅻🅾🅰🅳🅸🅽🅶 ····" + moradito + "\/\/\/\/\/\/")
time.sleep(0.5)
print (moradito + "  \/\/\/\/" + verde + "··············" + moradito + "\/\/\/\/\/\/")
time.sleep(0.5)
print (moradito + "    \/\/\/\/\/" + verde + "·······" + moradito + "\/\/\/\/\/\/\/")

#Instalación requirimientos y librerias:
call("apt-get install python3 && apt install -y python3-pip && pip3 install requests && pip3 install beautifulsoup4 && pip3 install feedparser", shell=True)
call("clear")

#Cabecera Iniciando:
print (moradito + "\/\/\/\/" + verde + "····· 🆂🆃🅰🆁🆃🅸🅽🅶 ·····" + moradito + "\/\/\/\/\/\/")
time.sleep(0.5)
print (moradito + "  \/\/\/\/" + verde + "················" + moradito + "\/\/\/\/\/\/")
time.sleep(0.5)
print (moradito + "    \/\/\/\/\/" + verde + "········" + moradito + "\/\/\/\/\/\/")

#Variables del programa:
url = 'https://www.vulnhub.com/feeds/added/rss/'
url_torrent = 'https://www.vulnhub.com/feeds/torrent/rss/'
feed = feedparser.parse(url)
feed_torrent = feedparser.parse(url_torrent)
url_inicio = 'https://www.vulnhub.com'
page = requests.get(url_inicio)
soup = BeautifulSoup(page.content, 'html.parser', on_duplicate_attribute='delete')
time = subprocess.check_output(['date'])
descripcion = "🅼🅰🅲🅷🅸🅽🅴 🅳🅴🆂🅲🆁🅸🅿🆃🅸🅾🅽 :\n"

#Eliminación de impurezas en la salida de datos:
def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value)

#Búsqueda de torrents en el feed:
def torrent():
    for link in feed_torrent.entries:
        print ("Torrent link: " + link.link)

# |Inicio Programa|
call("clear")

#Cabecera:
print("")
charizar ('     ✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪')
charizar ('꧁              🆂🅷🅴🅻🅻🅳🆁🅴🅳🅳  🆂🅾🅲🅸🅴🆃🆈               ꧂  ')
charizar ('         #Updated list of VulnHub machines.    ')
charizar ('     ✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪')

#Funciones:
print ('')
print (moradito + '🅳🅰🆃🅴 🅰🅽🅳 🆃🅸🅼🅴 🅾🅵 🆃🅷🅴 🅻🅸🆂🆃 : ' + cs_color + verde + str(time).split("b'")[-1].rsplit("n'")[0], sep="")
print ('')

while True:
    print ("🅼🅴🅽🆄")
    print(verde + "❰1❱ " + rojo + "🅽🅴🆆 🅼🅰🅲🅷🅸🅽🅴🆂 🅻🅸🆂🆃\t" + verde + "❰2❱ " + rojo + "🅼🅰🅲🅷🅸🅽🅴🆂 🅳🅴🆂🅲🆁🅸🅿🆃🅸🅾🅽 🅻🅸🆂🆃\n\n" + verde +
     "\t❰3❱ " + rojo + "🆃🅾🆁🆁🅴🅽🆃 🅻🅸🆂🆃 🅾🅵 🅼🅰🅲🅷🅸🅽🅴🆂\t" + verde + "❰4❱ " + rojo + "🅴🆇🅸🆃 🅿🆁🅾🅶🆁🅰🅼 " +cs_color)
    opcion = input(verde + "\n" + "➭➭➭ " + cs_color)

    if opcion == "1":
        print ("")
        charizar ("$" + moradito + "🆃🅷🅴🆂🅴 🅰🆁🅴 🆃🅷🅴 🅽🅴🆆 🅼🅰🅲🅷🅸🅽🅴🆂 :")
        print ("")

        for link in soup.find_all(class_ = 'card-title'):
            print (rojo + '          ❖' + verde, *link.get_text('').strip(), sep = "")
        
        print ("")

    if opcion == "2":
        print (moradito + "🅼🅰🅲🅷🅸🅽🅴🆂 🅳🅴🆂🅲🆁🅸🅿🆃🅸🅾🅽 🅻🅸🆂🆃 :\n" + cs_color)
        for post in feed.entries:
            print(rojo + '🅼🅰🅲🅷🅸🅽🅴 ❖' + rojo + post.title + ": \n" + moradito + descripcion + verde + strip_tags(post.description)
            + "\n")

    if opcion == "3":
        for post in feed_torrent.entries:
            print(rojo + '❖' + rojo + post.title + ": " + verde + strip_tags(post.link))

    if opcion == "4":

        break


call("clear")
charizar ("🆂🅷🅴🅻🅻🅳🆁🅴🅳🅳 🆂🅰🆈 🅱🆈🅴 🅱🆈🅴")

#FIN...

