import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

janela = ctk.CTk()
janela.title('Improving skills')
janela.geometry('600x600')

ctk.CTkLabel(janela, text='Bem vindo').pack()

mensagem = ctk.CTkLabel(janela, text='')
mensagem.pack()

nome_entry = ctk.CTkEntry(janela)
nome_entry.pack()

def botao_do_entry():
    nome = nome_entry.get()
    if not nome:
        messagebox.showerror('ERRO','Você não digitou seu nome')
        return
    mensagem.configure(text=f'Olá {nome}')

ctk.CTkButton(janela, text='Veja seu nome', command=botao_do_entry).pack()

def pressionar_botao():
    messagebox.showinfo('Alerta', 'Programa executado com sucesso')


ctk.CTkButton(janela, text='Clique aqui para ver o alerta', command=pressionar_botao).pack()


janela.mainloop()