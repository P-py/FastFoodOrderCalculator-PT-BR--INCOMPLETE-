import time
from tkinter import *
import locale

locale.setlocale(locale.LC_ALL, 'pt-br')

CardápioRoot = Tk()
def botão_reset():
    Cardápio.destroy()
    Cardápio1.destroy()
    Cardápio2.destroy()
    Cardápio3.destroy()
    Cardápio4.destroy()
    Cardápio5.destroy()
    Cardápio6.destroy()
    BotãoReset.destroy()
    BotãoCalcular.pack()
    BotãoVerCardápio.pack()

def CalcularPedido():
    Itens = []
    def CachorroQuente():
        cachorroquentevalor = 5
        Itens.append(cachorroquentevalor)
    def BauruSimples():
        baurusimplesvalor = 6
        Itens.append(baurusimplesvalor)
    def BauruComOvo():
        baurucomovovalor = 6.50
        Itens.append(baurucomovovalor)
    def Hamburger():
        hamburgervalor = 4.50
        Itens.append(hamburgervalor)
    def Cheeseburger():
        cheeseburgervalor = 5
        Itens.append(cheeseburgervalor)
    def Suco():
        sucovalor = 3
        Itens.append(sucovalor)
    def Refrigerante():
        refrivalor = 3.50
        Itens.append(refrivalor)
    def valor_final():
        soma_itens = sum(Itens)
        ValorFinalConta = Label(CardápioRoot, text=f'O valor final do pedido fica em {(locale.currency(soma_itens, grouping=True))}', fg='Red', padx=50, pady=50)
        ValorFinalConta.pack()
    BotãoAdicionarCachorroQuente = Button(CardápioRoot, command=CachorroQuente, text='Adicionar Cachorro Quente', padx=10, pady=5)
    BotãoAdicionarBauru = Button(CardápioRoot, command=BauruSimples, text='Adicionar Bauru Simples', padx=10, pady=5)
    BotãoAdicionarBauruOvo = Button(CardápioRoot, command=BauruComOvo, text='Adicionar Bauru com ovo', padx=10, pady=5)
    BotãoAdicionarHamburguer = Button(CardápioRoot, command=Hamburger, text='Adicionar Hamburguer', padx=10, pady=5)
    BotãoAdicionarCheese = Button(CardápioRoot, command=Cheeseburger, text='Adicionar Cheeseburguer', padx=10, pady=5)
    BotãoAdicionarSuco = Button(CardápioRoot, command=Suco, text='Adicionar Suco', padx=10, pady=5)
    BotãoAdicionarRefri = Button(CardápioRoot, command=Refrigerante, text='Adicionar Refrigerante', padx=10, pady=5)
    BotãoFinalizarpedido = Button(CardápioRoot, command=valor_final, text='Finalizar pedido', padx=30, pady=15)
    BotãoAdicionarCachorroQuente.pack()
    BotãoAdicionarBauru.pack()
    BotãoAdicionarBauruOvo.pack()
    BotãoAdicionarHamburguer.pack()
    BotãoAdicionarCheese.pack()
    BotãoAdicionarSuco.pack()
    BotãoAdicionarRefri.pack()
    BotãoFinalizarpedido.pack()
    
def VerCardápio():
    Cardápio.pack()
    Cardápio1.pack()
    Cardápio2.pack()
    Cardápio3.pack()
    Cardápio4.pack()
    Cardápio5.pack()
    Cardápio6.pack()
    BotãoReset.pack()
    BotãoVerCardápio.destroy()

Canvas = Canvas(CardápioRoot, bg='Grey', height = 1920, width=1080)
Título = Label(Canvas, text='CALCULADORA DE PEDIDO - LANCHONETE', padx=125, pady=35)
BotãoCalcular = Button(Canvas, text='Calcular pedido', command=CalcularPedido, padx=50, pady=25)
BotãoVerCardápio = Button(Canvas, text='Ver cardápio', command=VerCardápio, padx=50, pady=25)
BotãoReset = Button(Canvas, text='Fechar cardápio', command=botão_reset, padx=10, pady=5)
EspaçoEmBranco = Label(Canvas, fg='Grey', text=' ', bg='Grey')
Cardápio = Label(Canvas, fg='Red', text='Cachorro Quente - 1.20')
Cardápio1 = Label(Canvas, fg='Red', text='Bauru Simples - 1.30')
Cardápio2 = Label(Canvas, fg='Red', text='Bauru com Ovo - 1.50')
Cardápio3 = Label(Canvas, fg='Red', text='Hamburguer - 1.20')
Cardápio4 = Label(Canvas, fg='Red', text='Cheeseburguer - 1.70')
Cardápio5 = Label(Canvas, fg='Red', text='Suco - 2.20')
Cardápio6 = Label(Canvas, fg='Red', text='Refrigerante - 1.00')

Canvas.pack()
Título.pack()
BotãoCalcular.pack()
BotãoVerCardápio.pack()
CardápioRoot.mainloop()