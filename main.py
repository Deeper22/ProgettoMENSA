import sys


class Utente():
    def __init__(self):


        #FUNZIONE CONTROLLO NOME E COGNOME
        def ControlloSTR(stringa):
            while any(char.isdigit() for char in stringa) or len(stringa)==0:
                print('Errore! Inserire stringa non vuota')
                stringa = input()

        #FUNZIONE CONTROLLO MATRICOLA
        def ControlloMTR(matr):
            while not matr.isdigit() or len(matr)!=7:
                print('Errore! Inserisci numero di 7 cifre')
                matr = input('Inserisci matricola: ')


        #INSERIMENTO E CONTROLLO NOME
        nome = input('Inserisci nome: ')
        ControlloSTR(nome)
        self.nome = nome

        #INSERIMENTO E CONTROLLO COGNOME
        cognome = input('Inserisci cognome: ')
        ControlloSTR(cognome)
        self.cognome = cognome

        #INSERIMENTO E CONTROLLO MATRICOLA
        matricola = input('Inserisci matricola: ')
        ControlloMTR(matricola)
        self.matricola = matricola

    def controlla_posto(self):
        if mensa.posti_disponibili == 0:
            print('Nessun posto disponibile')
            sys.exit()
        else:
            mensa.posti_disponibili -= 1
            print('Posto disponibile!\nPosti ancora disponibili: ' + str(mensa.posti_disponibili))

    #def scelta(self):



class Mensa():
    pass








# class Menu():
#     def __init__(self, primo, secondo, contorno):
#         self.primo = ['Pasta', 'Zuppa', 'Riso']
#         self.secondo = ['Maiale', 'Manzo', 'Mozzarella']
#         self.contorno = ['Carote', 'Insalata', 'Patate']


menu = Menu()

print(menu.primo[1])







