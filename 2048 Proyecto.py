import random
from random import randint
from tkinter import *



#funcion para poner la matriz en vertical
def vertical(m):
    i=0
    print(m[i])
    print(m[i+1])
    print(m[i+2])
    print(m[i+3])
    

m1=[[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]


#analizar el caso ganador
def win(i,j,m1):
    if(i==3):
        if(j==3):
            if(m1[i][j]==2048):
                print("¡Ganaste!")
                sys.exit(0)
            else:
                ""
        else:
            return (i,j+1,m1)
    elif(j==3):
        if(m1[i][j]==2048):
                print("¡Ganaste!")
        else:
            return win(i+1,0,m1)
    else:
        if(m1[i][j]==2048):
                print("¡Ganaste!")
        else:
            return win(i,j+1,m1)
    
    
#ver si la matriz esta llena
def llena(i,j,m1):
    if(i==3):
        if(j==3):
            if(m1[i][j]!=0):
                print("Fin de la Partida")
                
                sys.exit(0)
            else:
                return rand(m1)
        else:
            return llena(i,j+1,m1)
    elif(j==3):
        if(m1[i][j]!=0):
                return llena(i+1,0,m1)
        else:
            return rand(m1)
    

        
    elif(m1[i][j]!=0):
        return llena(i,j+1,m1)
    else:
        return rand(m1)


#Funcion para los movimientos con las teclas





def direction():
    tk=Tk()
    colorfondo="#00CCCC"
    tk.bind_all('<KeyPress-Left>',teclas)
    tk.bind_all('<KeyPress-Right>',teclas)
    tk.bind_all('<KeyPress-Up>',teclas)
    tk.bind_all('<KeyPress-Down>',teclas)
    tk.title("2048 teclado")
    tk.geometry("300x100")
    tk.configure(background=colorfondo)
    Bl=Button(tk,text="⬅",width=4,height=2).place(x=20,y=30)
    Ll=Label(tk,text="Left").place(x=23,y=5)
    Br=Button(tk,text="➡",width=4,height=2).place(x=90,y=30)
    Lr=Label(tk,text="Right").place(x=93,y=5)
    Bu=Button(tk,text="⬆",width=4,height=2).place(x=160,y=30)
    Lu=Label(tk,text="Up").place(x=166,y=5)
    Bd=Button(tk,text="⬇",width=4,height=2).place(x=230,y=30)
    Ld=Label(tk,text="Down").place(x=233,y=5)
    tk.focus()

        
def teclas(event):

    if (event.keysym=='Left'):
        print('\n')
        mDec(0,0,m1)
        win(0,0,m1)
        izquierda(0,3,m1)

    elif(event.keysym=='Right'):
        print('\n')
        mDec(0,0,m1)
        win(0,0,m1)
        derecha(0,0,m1)
            
    elif(event.keysym=='Up'):
        print('\n')
        mDec(0,0,m1)
        win(0,0,m1)
        up(3,0,m1)
            
    elif(event.keysym=='Down'):
        print('\n')
        mDec(0,0,m1)
        win(0,0,m1)
        down(0,0,m1)
            
    else:
        return direction()


#para generar un numero en cada movimiento
def rand(m1):
    i3=randint(0,3)
    j3=randint(0,3)
    
    if(m1[i3][j3]!=0):
        i3=randint(0,3)
        j3=randint(0,3)
        return rand(m1)
    else:
        matriz=[2]
        r3=random.choice(matriz)
        m1[i3][j3]=r3
        return(m1)
    
        
        
    
    
#para crear una matriz con dos numeros (2 o 4) ubicados al azar
def matriz():
    #numero random entre 2 y 4
    matriz=[2,4]
    r1=random.choice(matriz)
    r2=random.choice(matriz)
    #numero random en la matriz
    i1=randint(0,3)
    j1=randint(0,3)
    i2=randint(0,3)
    j2=randint(0,3)
    m1[i1][j1]=r1
    m1[i2][j2]=r2
    igual(i1,i2,j1,j2,r1,r2,m1,b)

    
    
#para verificar que no sea la misma posicion
def igual(i1,i2,j1,j2,r1,r2,m1,b):

    if(i1==i2 and j1==j2):
        i2=randint(0,3)
        return igual(i1,i2,j1,j2,r1,r2,m1,b)
    else:
        m1[i1][j1]=r1
        m1[i2][j2]=r2
        print('\n')
        print('START'+'\n')
        print("***Abra la ventana '2048 teclado' para jugar***")
        base(b,m1)
        
        

    
#movimiento hacia la izquierda
def izquierda(i,j,m1):
        if(i==3):
            if(j==0):
                llena(0,0,m1)
                base(b,m1)

            elif(m1[i][j]==0):
                return izquierda(i,j-1,m1)
            
            elif(m1[i][j-1]==0 and m1[i][j]!=0):
                m1[i][j-1]=m1[i][j]
                m1[i][j]=0
                llena(0,0,m1)
                base(b,m1)
            
            elif(m1[i][j]==m1[i][j-1]):
                r=m1[i][j]+m1[i][j-1]
                m1[i][j-1]=r
                m1[i][j]=0
                llena(0,0,m1)
                base(b,m1)
            
            else:
                return izquierda(i,j-1,m1)
            
        elif(j==0):
            return izquierda(i+1,3,m1)
        
        elif(m1[i][j]==0):
            return izquierda(i,j-1,m1)
            
        elif(m1[i][j-1]==0 and m1[i][j]!=0):
            m1[i][j-1]=m1[i][j]
            m1[i][j]=0
            return izquierda(i+1,3,m1)
            
            return izquierda(i+1,3,m1)
        
        elif(m1[i][j]==m1[i][j-1]):
            r=m1[i][j]+m1[i][j-1]
            m1[i][j-1]=r
            m1[i][j]=0
            return izquierda(i+1,3,m1)
        
        else:
            return izquierda(i,j-1,m1)

    
#movimiento hacia la derecha
def derecha(i,j,m1):
        if(i==3):
            if(j==3):
                llena(0,0,m1)
                base(b,m1)

            elif(m1[i][j]==0):
                return derecha(i,j+1,m1)
                
            elif(m1[i][j+1]==0 and m1[i][j]!=0):
                m1[i][j+1]=m1[i][j]
                m1[i][j]=0
                llena(0,0,m1)
                base(b,m1)
            
            elif(m1[i][j]==m1[i][j+1]):
                r=m1[i][j]+m1[i][j+1]
                m1[i][j+1]=r
                m1[i][j]=0
                llena(0,0,m1)
                base(b,m1)
            
            else:
                return derecha(i,j+1,m1)
            
        elif(j==3):
            return derecha(i+1,0,m1)   
            
        elif(m1[i][j]==0):
            return derecha(i,j+1,m1)
            
        elif(m1[i][j+1]==0 and m1[i][j]!=0):
            m1[i][j+1]=m1[i][j]
            m1[i][j]=0
            return derecha(i+1,0,m1)
        
        elif(m1[i][j]==m1[i][j+1]):
            r=m1[i][j] + m1[i][j+1]
            m1[i][j+1]=r
            m1[i][j]=0
            return derecha(i+1,0,m1)
        
        else:
            return derecha(i,j+1,m1)

#movimiento hacia abajo
def down(i,j,m1):
        if(j==3):
            if(i==3):
                llena(0,0,m1)
                base(b,m1)

            elif(m1[i][j]==0):
                return down(i+1,j,m1)
                
            elif(m1[i+1][j]==0 and m1[i][j]!=0):
                m1[i+1][j]=m1[i][j]
                m1[i][j]=0
                llena(0,0,m1)
                base(b,m1)
                #print(pts)
            
            elif(m1[i][j]==m1[i+1][j]):
                r=m1[i][j]+m1[i+1][j]
                #pts=pts+r
                m1[i+1][j]=r
                m1[i][j]=0
                llena(0,0,m1)
                base(b,m1)
                #print(pts)
            
            else:
                return down(i+1,j,m1)
            
        elif(i==3):
            return down(0,j+1,m1)   
            
        elif(m1[i][j]==0):
            return down(i+1,j,m1)
            
        elif(m1[i+1][j]==0 and m1[i][j]!=0):
            m1[i+1][j]=m1[i][j]
            m1[i][j]=0
            return down(0,j+1,m1)
        
        elif(m1[i][j]==m1[i+1][j]):
            r=m1[i][j]+m1[i+1][j]
            #pts=pts+r
            m1[i+1][j]=r
            m1[i][j]=0
            return down(0,j+1,m1)
        
        else:
            return down(i+1,j,m1)

#movimiento hacia arriba
def up(i,j,m1):
        if(j==3):
            if(i==0):
                llena(0,0,m1)
                base(b,m1)
                print(pts)

            elif(m1[i][j]==0):
                return up(i-1,j,m1)
                
            elif(m1[i-1][j]==0 and m1[i][j]!=0):
                m1[i-1][j]=m1[i][j]
                m1[i][j]=0
                llena(0,0,m1)
                base(b,m1)
                print(pts)
            
            elif(m1[i][j]==m1[i-1][j]):
                r=m1[i][j]+m1[i-1][j]
                #pts=pts+r
                m1[i-1][j]=r
                m1[i][j]=0
                llena(0,0,m1)
                base(b,m1)
                print(pts)
            
            else:
                return down(i-1,j,m1)
            
        elif(i==0):
            return up(3,j+1,m1)   
            
        elif(m1[i][j]==0):
            return up(i-1,j,m1)
            
        elif(m1[i-1][j]==0 and m1[i][j]!=0):
            m1[i-1][j]=m1[i][j]
            m1[i][j]=0
            return up(3,j+1,m1)
        
        elif(m1[i][j]==m1[i-1][j]):
            r=m1[i][j]+m1[i-1][j]
            #pts=pts+r
            m1[i-1][j]=r
            m1[i][j]=0
            return up(3,j+1,m1)
        
        else:
            return up(i-1,j,m1)

        
#cambiar la matriz de decimal a x base
def base(b,m1):
    Bin=2
    Dec=10
    Oct=8
    Hex=16
    
    if(b==2):
        mBin(0,0,m1)
    elif(b==10):
        #si esta en decimal no hay cambios
        print(vertical(m1))
    elif(b==8):
        mOct(0,0,m1)
    elif(b==16):
        mHex(0,0,m1)
    else:
        print("Base invalida")
        

#cambiar de la base a decimal para operar
def base_a_dec(x,i,j,m1):
    Bin=2
    Dec=10
    Oct=8
    Hex=16
    
    if(b==2):
        Bin_a_Dec(x,i,j,m1)
        
    elif(b==10):
        ""
        
    elif(b==8):
        Oct_a_Dec(x,i,j,m1)
        
    elif(b==16):
        Hex_a_Dec(str(x),i,j,m1)
    else:
        print("Base invalida")
    


#Decimal a Binario
def mBin(i,j,m1):
    if(i==3):
        if(j==3):
            convBin(m1[j][i],i,j,m1)
            print (vertical(m1))
        else:
            convBin(m1[i][j],i,j,m1)
            
            return mBin(i,j+1,m1)
    elif(j==3):
        convBin(m1[i][j],i,j,m1)
        return mBin(i+1,0,m1)
    else:
        convBin(m1[i][j],i,j,m1)
        return mBin(i,j+1,m1)
        

def convBin(x,i,j,m1):
    if(x==0):
        m1[i][j]=("0000")
    elif(x==2):
        m1[i][j]=("0010")
    elif(x==4):
        m1[i][j]=("0100")
    elif(x==8):
        m1[i][j]=("1000")
    elif(x==16):
        m1[i][j]=("10000")
    elif(x==32):
        m1[i][j]=("100000")
    elif(x==64):
        m1[i][j]=("1000000")
    elif(x==128):
        m1[i][j]=("10000000")
    elif(x==256):
        m1[i][j]=("100000000")
    elif(x==512):
        m1[i][j]=("1000000000")
    elif(x==1024):
        m1[i][j]=("10000000000")
    elif(x==2048):
        m1[i][j]=("100000000000")
                     
        
#Binario a Decimal

def mDec(i,j,m1):
    if(i==3):
        if(j==3):
            #Bin_a_Dec(m1[i][j],i,j,m1)
            base_a_dec(m1[i][j],i,j,m1)
            return(m1)
            print(m1)
        else:
            #Bin_a_Dec(m1[i][j],i,j,m1)
            base_a_dec(m1[i][j],i,j,m1)
            mDec(i,j+1,m1)
            
    elif(j==3):
        #Bin_a_Dec(m1[i][j],i,j,m1)
        base_a_dec(m1[i][j],i,j,m1)
        mDec(i+1,0,m1)
    else:
        #Bin_a_Dec(m1[i][j],i,j,m1)
        base_a_dec(m1[i][j],i,j,m1)
        mDec(i,j+1,m1)
        
def Bin_a_Dec(x,i,j,m1):
     m1[i][j]=(int(str(x),2))

#Decimal a Octal
def mOct(i,j,m1):
    if(i==3):
        if(j==3):
            convOct(m1[j][i],i,j,m1)
            print (vertical(m1))
        else:
            convOct(m1[i][j],i,j,m1)
            
            return mOct(i,j+1,m1)
    elif(j==3):
        convOct(m1[i][j],i,j,m1)
        return mOct(i+1,0,m1)
    else:
        convOct(m1[i][j],i,j,m1)
        return mOct(i,j+1,m1)

def convOct(x,i,j,m1):
    if(x==0):
        m1[i][j]=(0)
    elif(x==2):
        m1[i][j]=(2)
    elif(x==4):
        m1[i][j]=(4)
    elif(x==8):
        m1[i][j]=(10)
    elif(x==16):
        m1[i][j]=(20)
    elif(x==32):
        m1[i][j]=(40)
    elif(x==64):
        m1[i][j]=(100)
    elif(x==128):
        m1[i][j]=(200)
    elif(x==256):
        m1[i][j]=(400)
    elif(x==512):
        m1[i][j]=(1000)
    elif(x==1024):
        m1[i][j]=(2000)
    elif(x==2048):
        m1[i][j]=(4000)


#Octal a Decimal
    
def Oct_a_Dec(x,i,j,m1):
    x=str(x)
    m1[i][j]= int(str(int(x, 8)))

#Decimal a Hexadecimal
def mHex(i,j,m1):
    if(i==3):
        if(j==3):
            convHex(m1[j][i],i,j,m1)
            print (vertical(m1))
        else:
            convHex(m1[i][j],i,j,m1)
            
            return mHex(i,j+1,m1)
    elif(j==3):
        convHex(m1[i][j],i,j,m1)
        return mHex(i+1,0,m1)
    else:
        convHex(m1[i][j],i,j,m1)
        return mHex(i,j+1,m1)

def convHex(x,i,j,m1):
    if(x==0):
        m1[i][j]=(0)
    elif(x==2):
        m1[i][j]=(2)
    elif(x==4):
        m1[i][j]=(4)
    elif(x==8):
        m1[i][j]=(8)
    elif(x==16):
        m1[i][j]=(10)
    elif(x==32):
        m1[i][j]=(20)
    elif(x==64):
        m1[i][j]=(40)
    elif(x==128):
        m1[i][j]=(80)
    elif(x==256):
        m1[i][j]=(100)
    elif(x==512):
        m1[i][j]=(200)
    elif(x==1024):
        m1[i][j]=(400)
    elif(x==2048):
        m1[i][j]=(800)

#Hexadecimal a Decimal
def Hex_a_Dec(x,i,j,m1):
    m1[i][j]= int(x, 16)
        

#INICIO(Menu)
    
lista=[]
def play(nombre):
    samename(lista,nombre,0)
    

def samename(lista,nombre,i):
    if(nombre==""):
        
        print("Usuario invalido","El nombre de usuario no ha sido definido correctamente")

    elif(lista==[]):
        
        print("Welcome","Su usario ha sido registrado con exito ¡Bienvenido al juego!")
        escribir(nombre)
        leaderboard(nombre,0)
        
    elif(i==len(lista)-1):
        if(nombre!=lista[i]):
            
           print("Welcome","Su usario ha sido registrado con exito ¡Bienvenido al juego!")
           escribir(nombre)
           leaderboard()

        else:
            lista.append([])
            print("Welcome","Bienvenido de nuevo")
    else:            
        if(nombre!=lista[i]):
            return samename(lista,nombre,i+1)
        else:
            lista.append([])
            print("Welcome","Bienvenido de nuevo")
            
    
def abrirnota():
    nota=open("playerlist.txt","a")
    nota.close()
    
def cargar():
    nota=open("playerlist.txt","r")
    linea=nota.readline()
    if linea:
        if (linea[-1]=="\n"):
            linea=linea[:-1]
            lista.append(linea)
            linea=nota.readline()
        else:
            linea=linea
            lista.append(linea)
            linea=nota.readline()
    nota.close()
    
def escribir(nombre):
    nota=open("playerlist.txt","a")
    if(nombre!=""):
        nota.write(nombre+'\t'+str(pts)+"\n")
    else:
        return False
    nota.close()

def leaderboard(nombre,p):
    print('\n')
    print('[Leaderboard]  [Puntuacion]'+'\n')
    print(nombre+'='+ str(pts))
    print('\n')



def baseint():
       
    print("***Bases Numerales***")
    print("2 = 01-Binario-01")    
    print("10 = 2-Base Decimal-4")
    print("8 = 8-Octal-8")
    print("16 = 16-Hexadecimal-16")
    
print("<<< 2048+ >>>")
nombre=str(input('Ingrese su usuario:'))
play(nombre)    
baseint()  
b=int(input('Codigo de la base numeral elegida: '))
matriz()
direction()


