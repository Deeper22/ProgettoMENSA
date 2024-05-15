import sys
import time
import pickle


class Utente():
    def __init__(self):

        # FUNZIONE CONTROLLO NOME E COGNOME
        def ControlloSTR(stringa):
            while any(char.isdigit() for char in stringa) or len(stringa) == 0:
                print('Errore! Inserire stringa non vuota')
                stringa = input()

        # FUNZIONE CONTROLLO MATRICOLA
        def ControlloMTR(matr):
            while not matr.isdigit() or len(matr) != 7:
                print('Errore! Inserisci numero di 7 cifre')
                matr = input('Inserisci matricola: ')

        # INSERIMENTO E CONTROLLO NOME
        nome = input('Inserisci nome: ')
        ControlloSTR(nome)
        self.nome = nome

        # INSERIMENTO E CONTROLLO COGNOME
        cognome = input('Inserisci cognome: ')
        ControlloSTR(cognome)
        self.cognome = cognome

        # INSERIMENTO E CONTROLLO MATRICOLA
        matricola = input('Inserisci matricola: ')
        ControlloMTR(matricola)
        self.matricola = matricola

    # CONTROLLO DISPONIBILITA POSTI IN MENSA
    def controlla_posto(self):

        time.sleep(1)

        if mensa.posti_disponibili == 0:
            print('\nNessun posto disponibile')
            sys.exit()
        else:

            print('\nPosto disponibile!\nPosti ancora disponibili: ' + str(mensa.posti_disponibili))

    # SCELTA DEI PIATTI DA MANGIARE

    def scelta(self):

        time.sleep(1)
        print('\nScegli primo piatto: ')

        for i in range(len(menu.primo)):
            print(str(i + 1) + ') ' + menu.primo[i])

        time.sleep(1)
        primo_scelto = input('Digita il numero del piatto desiderato: ')
        while not (primo_scelto.isdigit() and 1 <= int(primo_scelto) <= len(menu.primo)):
            primo_scelto = input('Piatto non accettato. Riprova: ')

        print('Hai scelto ' + (menu.primo[int(primo_scelto) - 1]))


class Mensa():

    posti_disponibili = 5
    def __init__(self):

        self.mensa.posti_disponibili = mensa.posti_disponibili - 1




class Menu():
    def __init__(self):
        self.primo = ['Pasta', 'Zuppa', 'Riso', 'Pomodoro', 'Risotto']
        self.secondo = ['Maiale', 'Manzo', 'Mozzarella']
        self.contorno = ['Carote', 'Insalata', 'Finocchi']

        self.contaprimo = [0 for x in self.primo]
        self.contasecondo = [0 for x in self.secondo]
        self.contacontorno = [0 for x in self.contorno]


utente1 = Utente()

mensa = Mensa()

utente1.controlla_posto()

menu = Menu()

utente1.scelta()




