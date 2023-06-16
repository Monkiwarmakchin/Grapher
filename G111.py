'''
    Equipo 1
    Cruz Contreras Karen
    Beltrán Orozco Isaac
    Escamilla Sanchez Alejandro
    Carapia González José Ricardo 
'''
#import tkinter
from tkinter import *
import math
import numpy as np 
from matplotlib import pyplot as plt

ventana =Tk()
ventana.title("Graficador")
ventana.geometry('525x170')

titulo=Label(ventana, text="Este es un graficador de funciones",font=("Times New Roman",15))
titulo.grid(column=0,row=0)

'''Funciones'''
tituloF1=Label(ventana, text="Ingrese la primer función",font=("Times New Roman",10))
tituloF1.grid(column=0,row=2)

tituloF2=Label(ventana, text="Ingrese la segunda función",font=("Times New Roman",10))
tituloF2.grid(column=0,row=3)

funcion1=Entry(ventana,width=25)
funcion1.grid(column=1,row=2)

funcion2=Entry(ventana,width=25)
funcion2.grid(column=1,row=3)

'''Rango Inferior'''
tituloRI=Label(ventana, text="Ingrese el rango inferior",font=("Times New Roman",10))
tituloRI.grid(column=0,row=4)

rangoI=Entry(ventana,width=25)
rangoI.grid(column=1,row=4)

'''Rango Superior'''
tituloRS=Label(ventana, text="Ingrese el rango superior",font=("Times New Roman",10))
tituloRS.grid(column=0,row=5)

rangoS=Entry(ventana,width=25)
rangoS.grid(column=1,row=5)

'''Proceso del graficador'''
funciones={"sin":"np.sin","cos":"np.cos","tan":"np.tan","^":"**",
           "pi":"np.pi","sqrt":"np.sqrt","exp":"np.exp"}

def reemplazo(s):
    for i in funciones:
        if i in s: 
            s=s.replace(i, funciones[i])
    return s

def reemplazo_log(s):
    i=s.split(" ")
    for x in i:
        if "log" in x:
            aux=x.split("(")
            aux_b=aux[0]
            aux_n=aux[1]
            if(len(aux_b)!=3):
                base=aux_b[3:]
                num=aux_n[0:-1]
                print("base: "+base)
                print("num: "+num)
                s=s.replace("log"+base+"("+num+")","np.log ("+num+")/np.log("+base+")")
                print(s)
            else:
                s=s.replace("log","np.log")
    return s

def RepresentsInt(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

'''Botton Graficar Todo'''
def clickG():
    plt.cla()

    linf = float(rangoI.get()) 
    lsup = float(rangoS.get())
    texto_orig=funcion1.get(),funcion2.get()
    for cadena in texto_orig:
        if RepresentsInt(cadena):
            texto_orig_m=reemplazo(cadena)
            i_grafica=reemplazo_log(texto_orig_m)
            x=np.arange(linf, lsup, .01)
            y=np.full(len(x),cadena,dtype=float)   
            plt.plot(x, y, label=cadena)
            plt.legend(loc='lower right')
        else:
            texto_orig_m=reemplazo(cadena)
            i_grafica=reemplazo_log(texto_orig_m)
            x=np.arange(linf, lsup, .01)   
            y=eval(i_grafica)
            plt.plot(x, y, label=cadena)
            plt.legend(loc='lower right')

    # Front grafica
    plt.title('Representacion de funciones')
    plt.xlabel('X')
    plt.ylabel('Y') 
                    
    plt.show()

botonG=Button(ventana,text="Graficar Todo",command=clickG)
botonG.grid(column=2,row=7)

'''Botton Limpiar F1'''
def clickF1():
    global i_grafica
    plt.cla()
    #global act_rango
    linf = float(rangoI.get()) 
    lsup = float(rangoS.get())
    texto_orig=funcion2.get()
    if RepresentsInt(texto_orig):
        texto_orig_m=reemplazo(texto_orig)
        i_grafica=reemplazo_log(texto_orig_m)
        x=np.arange(linf, lsup, .01)
        y=np.full(len(x),texto_orig,dtype=float)   
        plt.plot(x, y, label=texto_orig)
        plt.legend(loc='lower right')
    else:
        texto_orig_m=reemplazo(texto_orig)
        i_grafica=reemplazo_log(texto_orig_m)
        x=np.arange(linf, lsup, .01)   
        y=eval(i_grafica)
        plt.plot(x, y, label=texto_orig)
        plt.legend(loc='lower right')
    

    # Front grafica
    plt.title('Representacion de funciones')
    plt.xlabel('X')
    plt.ylabel('Y') 
        
    plt.show()

botonF1=Button(ventana,text="Limpiar F1",command=clickF1)
botonF1.grid(column=0,row=6)

'''Botton Limpiar F2'''
def clickF2():
    global i_grafica
    plt.cla()
    #global act_rango
    linf = float(rangoI.get()) 
    lsup = float(rangoS.get())
    texto_orig=funcion1.get()
    if RepresentsInt(texto_orig):
        texto_orig_m=reemplazo(texto_orig)
        i_grafica=reemplazo_log(texto_orig_m)
        x=np.arange(linf, lsup, .01)
        y=np.full(len(x),texto_orig,dtype=float)   
        plt.plot(x, y, label=texto_orig)
        plt.legend(loc='lower right')
    else:
        texto_orig_m=reemplazo(texto_orig)
        i_grafica=reemplazo_log(texto_orig_m)
        x=np.arange(linf, lsup, .01)   
        y=eval(i_grafica)
        plt.plot(x, y, label=texto_orig)
        plt.legend(loc='lower right')
    

    # Front grafica
    plt.title('Representacion de funciones')
    plt.xlabel('X')
    plt.ylabel('Y') 
        
    plt.show()

botonF2=Button(ventana,text="Limpiar F2",command=clickF2)
botonF2.grid(column=1,row=6)

'''Botton Graficar F1'''
def clickGF1():
    global i_grafica
    
    #global act_rango
    linf = float(rangoI.get()) 
    lsup = float(rangoS.get())
    texto_orig=funcion1.get()
    if RepresentsInt(texto_orig):
        texto_orig_m=reemplazo(texto_orig)
        i_grafica=reemplazo_log(texto_orig_m)
        x=np.arange(linf, lsup, .01)
        y=np.full(len(x),texto_orig,dtype=float)   
        plt.plot(x, y, label=texto_orig)
        plt.legend(loc='lower right')
    else:
        texto_orig_m=reemplazo(texto_orig)
        i_grafica=reemplazo_log(texto_orig_m)
        x=np.arange(linf, lsup, .01)   
        y=eval(i_grafica)
        plt.plot(x, y, label=texto_orig)
        plt.legend(loc='lower right')
    

    # Front grafica
    plt.title('Representacion de funciones')
    plt.xlabel('X')
    plt.ylabel('Y') 
        
    plt.show()

botonGF1=Button(ventana,text="Graficar F1",command=clickGF1)
botonGF1.grid(column=0,row=7)

'''Botton Graficar F2'''
def clickGF2():
    global i_grafica
    
    #global act_rango
    linf = float(rangoI.get()) 
    lsup = float(rangoS.get())
    texto_orig=funcion2.get()
    if RepresentsInt(texto_orig):
        texto_orig_m=reemplazo(texto_orig)
        i_grafica=reemplazo_log(texto_orig_m)
        x=np.arange(linf, lsup, .01)
        y=np.full(len(x),texto_orig,dtype=float)   
        plt.plot(x, y, label=texto_orig)
        plt.legend(loc='lower right')
    else:
        texto_orig_m=reemplazo(texto_orig)
        i_grafica=reemplazo_log(texto_orig_m)
        x=np.arange(linf, lsup, .01)   
        y=eval(i_grafica)
        plt.plot(x, y, label=texto_orig)
        plt.legend(loc='lower right')
    

    # Front grafica
    plt.title('Representacion de funciones')
    plt.xlabel('X')
    plt.ylabel('Y') 
        
    plt.show()

botonGF2=Button(ventana,text="Graficar F2",command=clickGF2)
botonGF2.grid(column=1,row=7)

ventana.mainloop()

#pip intstall pipwin
#pipwin install <package name>