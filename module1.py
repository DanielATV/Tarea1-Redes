#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gonzalo
#
# Created:     02-05-2020
# Copyright:   (c) Gonzalo 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def leer_Cache():
    try:
        arch = open("cache.txt","r")
        l=[]
        a = ""
        name = ""
        cont = 5
        for i in arch:
            if(a == ""):
                name = i
                continue
            if(a=="----------"):
                l.append((name,a))
                a = ""
                name=""
                continue
            a += i
        arch.close()
        return l

    except:
        arch = open("cache.txt","w")
        arch.close()
        l = []
        return l

def escribir_cache(l):
    arch = open("cache.txt","w")
    for url,header in l:
        arch.write(url)
        arch.write(header)
        arch.write("----------")
    arch.close()

def limites(l):
    if(len(l)>5):
        return l[len(l)-5:]

lista = [1,2,3,4,5,6,7]
lista = lista[len(lista)-5:]
print(lista)


