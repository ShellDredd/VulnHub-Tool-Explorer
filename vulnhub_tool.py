#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: ShellDredd
# Nick: Shelly
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
print (moradito + "\/\/\/\/" + verde + "····" + moradito + "L O A D I N G")
time.sleep(0.5)
print (moradito + "  \/\/\/\/" + verde + "····" + moradito + "J U S T   M O M E N T")
time.sleep(0.5)
print (moradito + "    \/\/\/\/\/" + verde + "····" + moradito + "C O M P L E T E")

#Instalación requirimientos y librerias:
call("apt-get install -y python3 && apt install -y python3-venv python3-pip && pip3 install requests && pip3 install beautifulsoup4 && pip3 install feedparser", shell=True)
call("clear")

#Variables del programa:
url = 'https://www.vulnhub.com/feeds/added/rss/'
url_torrent = 'https://www.vulnhub.com/feeds/torrent/rss/'
feed = feedparser.parse(url)
feed_torrent = feedparser.parse(url_torrent)
url_inicio = 'https://www.vulnhub.com'
page = requests.get(url_inicio)
soup = BeautifulSoup(page.content, 'html.parser', on_duplicate_attribute='delete')
time = subprocess.check_output(['date'])
descripcion = "MACHINE DESCRIPTION :\n"

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
charizar ('               RED PURPLE      ---      @SHELLDREDD           ')
charizar ('               #Auto-Updated list of VulnHub machines.    ')
charizar ('     ✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪✪')

#Funciones:
print ('')
print (moradito + 'SCRIPT TIME UPDATE : ' + cs_color + verde + str(time).split("b'")[-1].rsplit("n'")[0], sep="")
print ('')

while True:
    print ("MENU")
    print(verde + "❰1❱ " + rojo + "NEW MACHINES\t" + verde + "❰2❱ " + rojo + "MACHINE DESCRIPTION\n\n" + verde +
     "\t❰3❱ " + rojo + "TORRENTS MACHINES\t" + verde + "❰4❱ " + rojo + "EXIT PROGRAM " +cs_color)
    opcion = input(verde + "\n" + "➭➭➭ " + cs_color)

    if opcion == "1":
        print ("")
        charizar ("$" + moradito + "THESE AR THE NEW MACHINES :")
        print ("")

        for link in soup.find_all(class_ = 'card-title'):
            print (rojo + '          ❖' + verde, *link.get_text('').strip(), sep = "")
        
        print ("")

    if opcion == "2":
        print (moradito + "MACHINES DESCRIPTION :\n" + cs_color)
        for post in feed.entries:
            print(rojo + 'MACHINE ❖' + rojo + post.title + ": \n" + moradito + descripcion + verde + strip_tags(post.description)
            + "\n")

    if opcion == "3":
        for post in feed_torrent.entries:
            print(rojo + '❖' + rojo + post.title + ": " + verde + strip_tags(post.link))

    if opcion == "4":

        break


call("clear")
charizar ("BYE && SEE YOU LATE")

#FINISH...

