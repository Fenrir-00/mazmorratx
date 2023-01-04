import os, sys, time, io
import random
import platform
from colores import colorverde,colorazul,colorclasic,colormorado,colornaraja,coloramarillo
while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")
  
sistema = platform.system()
limpieza = ""

if sistema == "Linux":
  limpieza = "clear"
elif sistema == "Windows":
  limpieza ="cls"


class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

def incorrecto():
    os.system(f"{limpieza}")
    print(f"""{color.rojo}
 █████╗ ██████╗  █████╗ ██╗ █████╗ ███╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗ ██║
██║  ██║██████╔╝██║  ╚═╝██║██║  ██║██╔██╗██║
██║  ██║██╔═══╝ ██║  ██╗██║██║  ██║██║╚████║
╚█████╔╝██║     ╚█████╔╝██║╚█████╔╝██║ ╚███║
 ╚════╝ ╚═╝      ╚════╝ ╚═╝ ╚════╝ ╚═╝  ╚══╝
██╗███╗  ██╗ █████╗  █████╗ ██████╗ ██████╗
██║████╗ ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║██╔██╗██║██║  ╚═╝██║  ██║██████╔╝██████╔╝
██║██║╚████║██║  ██╗██║  ██║██╔══██╗██╔══██╗
██║██║ ╚███║╚█████╔╝╚█████╔╝██║  ██║██║  ██║
╚═╝╚═╝  ╚══╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
███████╗ █████╗ ████████╗ █████╗
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗
█████╗  ██║  ╚═╝   ██║   ███████║
██╔══╝  ██║  ██╗   ██║   ██╔══██║
███████╗╚█████╔╝   ██║   ██║  ██║
╚══════╝ ╚════╝    ╚═╝   ╚═╝  ╚═╝{color.fin}""")
    time.sleep(4)

def banner():
 os.system(f"{limpieza}")
 print(f"""{color.cyan}
 ██████╗ ██████╗ ██╗   ██╗████████╗ █████╗ ████████╗██╗  ██╗
██╔════╝ ██╔══██╗██║   ██║╚══██╔══╝██╔══██╗╚══██╔══╝╚██╗██╔╝
██║  ██╗ ██████╔╝██║   ██║   ██║   ███████║   ██║    ╚███╔╝
██║  ╚██╗██╔══██╗██║   ██║   ██║   ██╔══██║   ██║    ██╔██╗
╚██████╔╝██║  ██║╚██████╔╝   ██║   ██║  ██║   ██║   ██╔╝╚██╗
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝{color.fin}""")
def contacto():
 
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  2.1                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 if sistema == "Linux":
  lol_py(texto)
 elif sistema == "Windows": 
  suerte = random.randint(0,5)
  if suerte == 0:
    coloramarillo(texto)
  elif suerte == 1:
    colorazul(texto)
  elif suerte == 2 :
    colorclasic(texto)
  elif suerte == 3 :
    colormorado(texto)
  elif suerte == 4 :
    colornaraja(texto)
  elif suerte == 5:
    colorverde(texto)          
  
 
class personajes:
  def __init__(self,nombre,vida,fuerza,velocidad,quemado,envenenado,dormido,escudo):
####atrivutos
    self.nombre = nombre
    self.vida = vida
    self.fuerza = fuerza
    self.velocidad = velocidad

####estados
    self.quemado = quemado
    self.envenenado = envenenado
    self.dormido = dormido
    self.escudo = escudo


def tablero():
   banner()
   contacto()
   var1 = f"{color.morado}1{color.azul}"
   var2 = f"{color.morado}2{color.azul}"
   var3 = f"{color.morado}3{color.azul}"
   var4 = f"{color.morado}4{color.azul}"
   var5 = f"{color.morado}5{color.azul}"
   var6 = f"{color.morado}6{color.azul}"
   var7 = f"{color.morado}7{color.azul}"
   var8 = f"{color.morado}8{color.azul}"
   var9 = f"{color.morado}9{color.azul}"

   if enemigo1.vida <= 0:
    var1  =f"{color.verde}✓{color.azul}"
   if enemigo2.vida <= 0:
    var2  =f"{color.verde}✓{color.azul}"
   if enemigo3.vida <= 0:
    var3  =f"{color.verde}✓{color.azul}"
   if enemigo4.vida <= 0:
    var4  =f"{color.verde}✓{color.azul}"
   if enemigo5.vida <= 0:
    var5  =f"{color.verde}✓{color.azul}"
   if enemigo6.vida <= 0:
    var6  =f"{color.verde}✓{color.azul}"
   if enemigo7.vida <= 0:
    var7  =f"{color.verde}✓{color.azul}"
   if enemigo8.vida <= 0:
    var8  =f"{color.verde}✓{color.azul}"
   if enemigo9.vida <= 0:
    var9  =f"{color.verde}✓{color.azul}"
   if enemigo1.vida <= 0  and enemigo2.vida <= 0 and enemigo3.vida <=0 and enemigo4.vida <= 0 and enemigo5.vida <= 0 and enemigo6.vida <= 0 and enemigo7.vida <= 0 and enemigo8.vida <= 0 and enemigo9.vida <= 0:
    ganar()
   else:




   
    mesa = f"""
+-----------+-----------+-----------+
|           |           |           |
|    {var1}      |     {var2}     |     {var3}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var4}      |     {var5}     |     {var6}     |
|           |           |           |
+-----------+-----------+-----------+
|           |           |           |
|    {var7}      |     {var8}     |     {var9}     |
|           |           |           |
+-----------+-----------+-----------+"""
 
    print(f"{color.azul}",mesa,f"{color.fin}")
    print(f"""{color.verde}
    BIENVENIDO A LA MAZMORRA DE FENRRIR00 """)   
    print()
    eleccion = input(f"{color.cyan}ELIJE UN NUNERO DE MAZMORRA>> {color.fin}")
    if eleccion == "1" and enemigo1.vida >= 0:
     combate(enemigo1)
    elif eleccion == "2" and enemigo2.vida >= 0:
     combate(enemigo2)
    elif eleccion == "3" and enemigo3.vida >= 0:
     combate(enemigo3)
    elif eleccion == "4" and enemigo4.vida >= 0:
     combate(enemigo4)
    elif eleccion == "5" and enemigo5.vida >= 0:
     combate(enemigo5)
    elif eleccion == "6" and enemigo6.vida >= 0:
     combate(enemigo6)
    elif eleccion == "7" and enemigo7.vida >= 0:
     combate(enemigo7)
    elif eleccion == "8" and enemigo8.vida >= 0:
     combate(enemigo8)
    elif eleccion == "9" and enemigo9.vida >= 0:
     combate(enemigo9)
    else:
     incorrecto()
     tablero()

def reset():
 amigo.vida = 600
 amigo.quemado = False
 amigo.envenenado = False
 amigo.dormido = False
 amigo.escudo = False

 enemigo1.vida = 200
 enemigo1.quemado = False
 enemigo1.envenenado = False
 enemigo1.dormido = False
 enemigo1.escudo = False

 enemigo2.vida = 250
 enemigo2.quemado = False
 enemigo2.envenenado = False
 enemigo2.dormido = False
 enemigo2.escudo = False
 
 enemigo3.vida = 300
 enemigo3.quemado = False
 enemigo3.envenenado = False
 enemigo3.dormido = False
 enemigo3.escudo = False

 enemigo4.vida = 350
 enemigo4.quemado = False
 enemigo4.envenenado = False
 enemigo4.dormido = False
 enemigo4.escudo = True

 enemigo5.vida = 400
 enemigo5.quemado = False
 enemigo5.envenenado = False
 enemigo5.dormido = False
 enemigo5.escudo = True

 enemigo6.vida = 500
 enemigo6.quemado = False
 enemigo6.envenenado = False
 enemigo6.dormido = False
 enemigo6.escudo = True

 enemigo7.vida = 600
 enemigo7.quemado = False
 enemigo7.envenenado = False
 enemigo7.dormido = False
 enemigo7.escudo = True

 enemigo8.vida = 750
 enemigo8.quemado = False
 enemigo8.envenenado = False
 enemigo8.dormido = False
 enemigo8.escudo = True

 enemigo9.vida = 900
 enemigo9.quemado = False
 enemigo9.envenenado = False
 enemigo9.dormido = False
 enemigo9.escudo = True

 


###############################################################
amigo = personajes("fenrir",600,25,100,False,False,False,False)
enemigo1 = personajes(1,200,30,25,False,False,False,False)
enemigo2 = personajes(2,250,30,25,False,False,False,False)
enemigo3 = personajes(3,300,35,100,False,False,False,False)
enemigo4 = personajes(4,350,35,100,False,False,False,True)
enemigo5 = personajes(5,400,45,100,False,False,False,True)
enemigo6 = personajes(6,500,45,100,False,False,False,True)
enemigo7 = personajes(7,600,50,100,False,False,False,True)
enemigo8 = personajes(8,750,50,100,False,False,False,True)
enemigo9 = personajes(9,900,50,100,False,False,False,True)
###############################################################

def inicio():
 os.system(f"{limpieza}") 
 banner()
 print(dibujo2)
 print(f"{color.amarillo}")
 print(f"{color.verde}[1]JUGAR")
 print(f"{color.amarillo}[2]AYUDA")
 print(f"{color.rojo}[0]SALIR{color.fin}")
 eleccion = input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if eleccion == "1":
  tablero()
 elif eleccion == "2":
  ayuda()
 elif eleccion =="0":
  os.system(f"{limpieza}")
 else:
  incorrecto()
  inicio()

def perder():
 banner()
 contacto()
 print(f"""{color.rojo}

██████╗ ███████╗██████╗ ██████╗ ██╗ ██████╗████████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔════╝
██████╔╝█████╗  ██████╔╝██║  ██║██║╚█████╗    ██║   █████╗
██╔═══╝ ██╔══╝  ██╔══██╗██║  ██║██║ ╚═══██╗   ██║   ██╔══╝
██║     ███████╗██║  ██║██████╔╝██║██████╔╝   ██║   ███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝    ╚═╝   ╚══════╝{color.fin}
""")
 print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
 print()
 print(f"{color.azul}[1] JUGAR OTRA VEZ")
 print(f"{color.rojo}[2] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  reset()
  inicio()
 elif var == "2":
  exit()
 else:
  incorrecto()
 perder()
  
def ganar():
 banner()
 contacto()
 print(f"""{color.amarillo}

 ██████╗  █████╗ ███╗  ██╗ █████╗  ██████╗████████╗███████╗
██╔════╝ ██╔══██╗████╗ ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██║  ██╗ ███████║██╔██╗██║███████║╚█████╗    ██║   █████╗
██║  ╚██╗██╔══██║██║╚████║██╔══██║ ╚═══██╗   ██║   ██╔══╝
╚██████╔╝██║  ██║██║ ╚███║██║  ██║██████╔╝   ██║   ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚══════╝{color.fin}
""")
 print(f"{color.morado}QUE QUIERES HACER AHORA{color.fin}")
 print()
 print(f"{color.azul}[1] JUGAR OTRA VEZ")
 print(f"{color.rojo}[2] SALIR{color.fin}")
 print()
 var=input(f"{color.cyan}ELIJE UN NUMERO >> {color.fin}")
 if var == "1":
  reset()
  inicio()
 elif var == "2":
  exit()
 else:
  incorrecto()
  ganar()

def ayuda():
 banner()
 contacto()
 print(f"""

  {color.morado}NUESTRO OBJETIVO SERA DERROTAR LAS 9 MAZMORRAS SIN PERECER 
                     EN EL INTENTO.{color.verde}

  VIDA: REPRESENTA NUESTRA VIDA
  VENENO: PERDEREMKS VIDA CADA TURNO
  QUEMADO: PERDEREMOS VIDA CADA TURNO
  ESCUDO: PARAREMOS UN ATAQUE
  DORMIDO: NO ATACAREMOS HASTA DESPERTAR

  ATACAR: HAREMOS DAÑO Y NOS DEDPERTAREMOS
  SANAR:  NOS CURAREMOS
  MAGIA:  PONDREMOS ESTADOS ALTERADOS
""")
 input(f"{color.cyan} PULSA CUALQUIER TECLA PARA CONTINUAR >>>{color.fin}")
 inicio()

####
def combate(enemigo):
 os.system(f"{limpieza}")
 dibujar(enemigo)
 while True:
  if amigo.envenenado == True:
   amigo.vida -=15
  if amigo.quemado == True:
   amigo.vida -=15
  if enemigo.envenenado == True:
   enemigo.vida -=15
  if enemigo.quemado == True:
   enemigo.vida -=15

  if enemigo.vida > 0 and amigo.vida > 0:
   print(f"""{color.morado}                 QUE QUIERES HACER {color.verde}
[1]ATACAR
[2]SANAR
[3]MAGIA{color.rojo}
[0]SALIR""")
   eleccion = input(f"{color.cyan}ELIJE UN NUNERO >> ")
   if eleccion == "1":
    if enemigo.escudo == True and amigo.dormido == False:
     enemigo.escudo = False
     suerte = random.randint(0,9)
     if suerte == 9:
      enemigo.vida -= amigo.fuerza
      dibujar(enemigo)
     else:
      dibujar(enemigo)
    elif  enemigo.escudo == False and amigo.dormido == False:
      enemigo.vida -= amigo.fuerza
      dibujar(enemigo)
      suerte = random.randint(0,9)
      if suerte == 2:
       enemigo.envenenado =True
       dibujar(enemigo)
      if suerte == 3:
       enemigo.quemado =True
       dibujar(enemigo)
    elif amigo.dormido == True:
      suerte = random.randint(0,9)
      if suerte >= 4:
       amigo.dormido = False
       if suerte == 5:
        enemigo.vida -= amigo.fuerza
        dibujar(enemigo)
       else:
        dibujar(enemigo)
      else:
       dibujar(enemigo)
####turno enemiogo########€€
    if amigo.escudo == True and enemigo.dormido == False:  
     amigo.escudo = False
     suerte = random.randint(0,9)
     if suerte >6:
      enemigo.escudo = True
      enemigo.envenenado =False
      enemigo.quemado= False
      dibujar(enemigo)
     if suerte >= 7:
      amigo.quemado =True
      dibujar(enemigo)
    elif amigo.escudo == False and enemigo.dormido == False:
     amigo.vida -= enemigo.fuerza
     dibujar(enemigo)
     suerte = random.randint(0,9)
     if suerte == 2:
       amigo.envenenado =True
       dibujar(enemigo)
     if suerte == 3:
       amigo.quemado =True
       dibujar(enemigo)
     if suerte > 5:
        amigo.vida -= enemigo.fuerza
    elif enemigo.dormido == True:
      suerte = random.randint(0,9)
      if suerte >= 4:
       enemigo.dormido = False
       if suerte == 5:
        amigo.vida -= enemigo.fuerza
        amigo.quenado == True
        dibujar(enemigo)
        
       else:
        dibujar(enemigo)
      else:
       dibujar(enemigo)

###########################
   elif eleccion == "2":
    if enemigo.escudo == True and amigo.dormido == False:
     amigo.quemado = False
     amigo.envenenado = False
     suerte = random.randint(50,200)
     amigo.vida += suerte
     suerte = random.randint(0,4)
     if suerte == 4:
      amigo.dormido= True
      amigo.escudo = True
      dibujar(enemigo)
     else:
      dibujar(enemigo)
    elif  enemigo.escudo == False and amigo.dormido == False:
     amigo.quemado = False
     amigo.envenenado = False
     suerte = random.randint(50,80)
     amigo.vida + suerte
     suerte = random.randint(0,4)
     if suerte == 4:
      amigo.dormido = True
      amigo.escudo = True
      dibujar(enemigo)
    elif amigo.dormido == True:
      suerte = random.randint(0,9)
      if suerte == 4:
       amigo.escudo = True
       dibujar(enemigo)
       
####turno enemiogo########€€
    if enemigo.dormido == False:
     suerte = random.randint(0,9)
     if suerte >6:
      enemigo.escudo = True
      enemigo.vida + 30
      dibujar(enemigo) 
      enemigo.quemado =False
     else:
      enemigo.escudo = True
      amigo.envenenado =True
      dibujar(enemigo)
     if suerte == 6:
      amigo.dormir = True
      amigo.vida -= enemigo.fuerza
    else:
       suerte = random.randint(0,3)
       if  suerte == "3":
        enemigo.dormido = False
        dibujar(enemigo)
       else:
        dibujar(enemigo)








##################################
   elif eleccion == "3":
    if  amigo.dormido == False:
     enemigo.quemado =True
     enemigo.envenenado =True
     dibujar(enemigo)
     suerte = random.randint(0,9)
     if suerte == 9:
      enemigo.dormido =True
      dibujar(enemigo)
     else:
      suerte = random.randint(0,9)
     if suerte >= 4:
      amigo.escudo =True
      dibujar(enemigo)
      if suerte ==9:
       enemigo.quemado =True
       enemigo.envenenado =True
       dibujar(enemigo)
     else:
      dibujar(enemigo) 
####turno enemiogo########€€
    if amigo.escudo == True and enemigo.dormido == False:
     amigo.escudo = False
     suerte = random.randint(0,9)
     if suerte == 9:
      enemigo.escudo = True
      dibujar(enemigo)
    
    elif amigo.escudo == False and enemigo.dormido == False:
     amigo.vida -= enemigo.fuerza
     dibujar(enemigo)
     suerte = random.randint(0,9)
     if suerte == 9:
      enemigo.escudo = True
      dibujar(enemigo)
     if suerte  < 5:
      amigo.quemado = True
      dibujar(enemigo)
    elif enemigo.dormido == True:
      suerte = random.randint(0,9)
      if suerte >= 4:
       enemigo.dormido = False
       if suerte == 5:
        amigo.vida -= enemigo.fuerza
        dibujar(enemigo)
       else:
        dibujar(enemigo)
      else:
       dibujar(enemigo)






####################################
   elif eleccion =="0":
    os.system(f"{limpieza}")
    exit()
    break
   else:
    incorrecto()
    combate(enemigo)



  elif enemigo.vida <= 0 and amigo.vida >= 0:
   if enemigo1.vida <= 0  and enemigo2.vida <= 0 and enemigo3.vida <=0 and enemigo4.vida <= 0 and enemigo5.vida <= 0 and enemigo6.vida <= 0 and enemigo7.vida <= 0 and enemigo8.vida <= 0 and enemigo9.vida <= 0:
    ganar()
    break
   else:
    tablero()
    break
  else:
   perder()
   break
 else:
  tablero()


########################################################
dibujo2 ='''

                               [_]___[_]__[_]___[_]
    |                          [__#__][__I_]__I__#]
   |.|                         [_I_#_I__#[__]__#__]
   |.|                            [_]_#_]__I_#_]
   |.|                            [I_|/ _W_ \|#]
   |:|      __                    [#_||{(")}||_]
 ,_|:|_,   /  )                   [_I||{/~\}||_]
   (Oo    / _I_                   [__]|/\_/\||#]
    +\ \  || __|                  [_I__I#___]__]
       \ \||___|                  [__I_#_I___#_]
         \ /.:.\-/                [#__I____]__I]
          |.:. /-----|            [__I_#__I__[_]
          |___|::oOo::|           [_#_[__#_]__#]
          /   |:<_T_>:|           [__#_I__[#_I_]
         |_____\ ::: /            [_I__]__#_I__]
          | |  \ \:/              [#__I__#_]__I]
          | |   | |               [_I#__I___I_#]
          \ /   | \___            [#__I__]_#___]
          / |   \_____|           [_I__I#__]___]
          `-'                     [__]#___][__#]'''

###############################################################

def dibujar(enemigo):
 os.system(f"{limpieza}")
 if amigo.vida >=1000:
  amigo.vida= 999
 esp=str(amigo.vida)
 if len(esp) == 3:
  esp =""
 if len(esp) == 2:
  esp =" "
 if len(esp) == 1:
  esp =" "
 esp1=str(enemigo.vida)
 if len(esp1) == 3:
  esp1 =""
 if len(esp1) == 2:
  esp1 =" "
 if len(esp1) == 1:
  esp1 =" "

 if amigo.escudo == True:
  var1 = "SI"
 else:
  var1 ="NO"
 if amigo.quemado == True:
  var2 = "SI"
 else:
   var2 ="NO"
 if amigo.envenenado == True:
  var3 = "SI"
 else:
  var3 ="NO"
 if amigo.dormido == True:
  var4 = "SI"
 else:
   var4 ="NO"
###
 if enemigo.escudo == True:
  var5 = "SI"
 else:
  var5 ="NO"
 if enemigo.quemado == True:
  var6 = "SI"
 else:
  var6 ="NO"
 if enemigo.envenenado == True:
  var7 = "SI"
 else:
  var7 ="NO"
 if enemigo.dormido == True:
  var8 = "SI"
 else:
   var8 ="NO"
 if enemigo.nombre == 1:
  nivel = 1
 if enemigo.nombre == 2:
  nivel = 2
 if enemigo.nombre == 3:
  nivel = 3
 if enemigo.nombre == 4:
  nivel = 4
 if enemigo.nombre == 5:
  nivel = 5
 if enemigo.nombre == 6:
  nivel = 6
 if enemigo.nombre == 7:
  nivel = 7
 if enemigo.nombre == 8:
  nivel = 8
 if enemigo.nombre == 9:
  nivel = 9





 dibujo =f"""{color.azul}
   |
  |.|
  |.|
  |.|            {color.rojo}MAZMORRA NIVEL:{nivel}{color.azul}
  |:|      __
,_|:|_,   /  )          {color.fin}         .-.{color.azul}
  (Oo    / _I_    {color.fin}              (o.o){color.azul}
   +\ \  || __|     {color.fin}             |=|{color.azul}
      \ \||___|      {color.fin}           __|__{color.azul}
       \ /.:.\-/     {color.fin}         | .=|=. |{color.azul}
         |.:. /-----| {color.fin}        | .=|=. |{color.azul}
         |___|::oOo::| {color.fin}       \ .=|=. /{color.azul}
         /   |:<_T_>:|  {color.fin}       \(_=_)//{color.azul}
        |_____\ ::: /    {color.fin}      (:| |:){color.azul}
         | |  \ \:/      {color.fin}       || ||{color.azul}
         | |   | |       {color.fin}       () (){color.azul}
         \ /   | \___    {color.fin}       || ||{color.azul}
         / |   \_____|   {color.fin}       || ||{color.azul}
         `-'             {color.fin}      ==' '=={color.verde}
#######################{color.cyan}GUERRERO{color.verde}######################
#{color.amarillo}VIDA:{color.morado}{amigo.vida}{color.amarillo}{esp} ESCUDO {color.morado}{var1}{color.amarillo} QUEMADO {color.morado}{var2}{color.amarillo} VENENO  {color.morado}{var3}{color.amarillo} DORMIDO {color.morado}{var4}{color.verde}#
#{color.fin}######################{color.rojo}ENEMIGO{color.fin}######################{color.verde}#
#{color.amarillo}VIDA:{color.morado}{enemigo.vida}{esp1} {color.amarillo}ESCUDO {color.morado}{var5} {color.amarillo}QUEMADO {color.morado}{var6} {color.amarillo}VENENO {color.morado} {var7}{color.amarillo} DORMIDO{color.morado} {var8}{color.verde}#
#####################################################"""
 print(dibujo)

inicio()

