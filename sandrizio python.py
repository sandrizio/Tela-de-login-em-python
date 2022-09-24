
from tkinter import *
from tkinter import Tk, ttk, messagebox
import getpass



#cores ------------------------------

co0 = '#f0f3f5' #preto
co1 = '#836FFF' #ROXO CLARO
co2 =  '#FF00FF' #rosa
co3= '#38576b' #valor
co4= '#403d3d' #letra

credenciais=['sandrizio', '123456']
#funçao de validaçao de senha

def verificar_senha():
    nome=e_nome.get()
    senha= e_pass.get()

    if nome=="admin" and nome== 'adimin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin')
    elif     credenciais [0]==nome and credenciais [1]==senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta '+ credenciais[0]  +'!!!')
    else:
        messagebox.showerror('Erro', 'Verifique o nome e senha digitados')
#criando janela -----------------------
janela= Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)

#dividindo a janela----------------------
Frame_cima=Frame(janela,width=310,height=50, bg=co1, relief='flat')
Frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo=Frame(janela,width=310,height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1,padx=0,sticky=NSEW)


# configurando o frame cima
l_nome=Label(Frame_cima, text='LOGIN',anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5 , y=5)

l_linha = Label(Frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2,fg=co4)
l_linha.place(x=10,y=45)

#configurar o frame baixo
l_nome_b= Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome_b.place(x=10,y=20)

e_nome=Entry(frame_baixo, width=25, justify='left',font=('',15), highlightthickness=1, relief='solid'  )
e_nome.place(x=14,y=50)

l_pass=Label(frame_baixo, text='senha *' , anchor=NW, font=('Ivy 10'), bg=co1 , fg=co4 )
l_pass.place(x=10,y=95)

e_pass=Entry(frame_baixo,show='*', width=25, justify='left',font=('',15), highlightthickness=1, relief='solid',  )

e_pass.place(x=14,y=130)

b_confirmar=Button(frame_baixo, command=verificar_senha, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED,overrelief=RIDGE)
b_confirmar.place(x=15,y=180)

janela.mainloop()

