import sys
import time
import pickle

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


    #CONTROLLO DISPONIBILITA POSTI IN MENSA
    def controlla_posto(self):

        time.sleep(1)

        if mensa.posti_disponibili == 0:

            # SCOMMENTA PER RESET PICKLE

            # with open('posti.pkl', 'wb') as posti:
            #     pickle.dump(100, posti)
            # mensa.posti_disponibili = 100

            print('\nNessun posto disponibile')
            sys.exit()

        else:
            mensa.posti_disponibili -= 1

            with open('posti.pkl', 'wb') as posti:
                pickle.dump(mensa.posti_disponibili, posti)

            print('\nPosto disponibile!\nPosti ancora disponibili: ' + str(mensa.posti_disponibili))


    #SCELTA DEI PIATTI DA MANGIARE
    def scelta(self):
        # SCELTA DEL PRIMO
        time.sleep(1)

        self.funzione(menu.primo, menu.contaprimo)
        self.funzione(menu.secondo, menu.contasecondo)
        self.funzione(menu.contorno, menu.contacontorno)


    def funzione(self, pietanza, vettore):

        print('\nScegli piatto: ')

        for i in range(len(pietanza)):
            print(str(i + 1) + ') ' + pietanza[i])

        time.sleep(1)
        piatto_scelto = input('Digita il numero del piatto desiderato: ')
        while not (piatto_scelto.isdigit() and 1 <= int(piatto_scelto) <= len(pietanza)):
            piatto_scelto = input('Piatto non accettato. Riprova: ')

        vettore[int(piatto_scelto)-1] += 1

        with open('ordini.pkl', 'ab') as ordini:
            pickle.dump(vettore, ordini)


        print('Hai scelto ' + (pietanza[int(piatto_scelto) - 1]))


class Mensa():

    def __init__(self):
        with open('posti.pkl', 'rb') as posti:
            self.posti_disponibili = pickle.load(posti)


class Menu():
    def __init__(self):
        self.primo = ['Pasta', 'Zuppa', 'Riso','Pomodoro', 'Risotto']
        self.secondo = ['Maiale', 'Manzo', 'Mozzarella', 'Funghi']
        self.contorno = ['Carote', 'Insalata', 'Finocchi']

        self.contaprimo = [0 for x in self.primo]
        self.contasecondo = [0 for x in self.secondo]
        self.contacontorno = [0 for x in self.contorno]


utente1 = Utente()

mensa = Mensa()

utente1.controlla_posto()

menu = Menu()

utente1.scelta()

print(menu.contaprimo)
print(menu.contasecondo)
print(menu.contacontorno)

with open('ordini.pkl', 'rb') as ordini:
    vettore = pickle.load(ordini)
    print(vettore)




