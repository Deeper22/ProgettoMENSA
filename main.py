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

    def aggiornaPickle(self, nome_file, vett_pickle):
        with open(nome_file+'.pkl', 'rb+') as nome_file:

            vett_temp = pickle.load(nome_file)
            if len(vett_temp) != len(vett_pickle):
                nome_file.seek(0)   #Si porta il puntatore del file all'inizio per sovrascrivere
                nome_file.truncate()   #Svuota il file
                vett_temp = [0] * len(vett_pickle)
                pickle.dump(vett_temp, nome_file)
            nome_file.seek(0)
            vett_pickle = [x + y for x, y in zip(vett_temp, vett_pickle)]
            pickle.dump(vett_pickle, nome_file)


    #SCELTA DEI PIATTI DA MANGIARE
    def riepilogo_salvataggio(self):

        time.sleep(1)

        vettoreprimi, primo_scelto = self.scelta(menu.primi, menu.contaprimo, 'primo')

        vettoresecondi, secondo_scelto = self.scelta(menu.secondi, menu.contasecondo, 'secondo')

        vettorecontorni, contorno_scelto = self.scelta(menu.contorni, menu.contacontorno, 'contorno')

        print('\nHai scelto: {}, {}, {}.'.format(menu.primi[int(primo_scelto) - 1], menu.secondi[int(secondo_scelto) - 1], menu.contorni[int(contorno_scelto) - 1]))
        conferma = input('\nInviare ordine? (si/no): ')
        while conferma != 'si' and conferma != 'no':
            conferma = input('Risposta non valida. Riprova: ')
        if conferma == 'si':
            print('Ordine inviato!')
            self.aggiornaPickle('primi', vettoreprimi)
            self.aggiornaPickle('secondi', vettoresecondi)
            self.aggiornaPickle('contorni', vettorecontorni)
        else:
            self.riepilogo_salvataggio()


    def scelta(self, pietanza, vettore, tipo):

        print('\nScegli ' +tipo+ ': ')

        for i in range(len(pietanza)):
            print(str(i + 1) + ') ' + pietanza[i])

        piatto_scelto = input('Digita il numero del piatto desiderato: ')
        while not (piatto_scelto.isdigit() and 1 <= int(piatto_scelto) <= len(pietanza)):
            piatto_scelto = input('Piatto non accettato. Riprova: ')

        vettore[int(piatto_scelto)-1] += 1

        print('Hai scelto ' + (pietanza[int(piatto_scelto) - 1]))

        return vettore, piatto_scelto


class Mensa():

    def __init__(self):
        with open('posti.pkl', 'rb') as posti:
            self.posti_disponibili = pickle.load(posti)

    def stampa_ordini(self):
        pasti = ['primi', 'secondi', 'contorni']
        for pasto in pasti:  # Iteriamo sui nomi dei pasti
            file_path = pasto + '.pkl'
            print(f"\nOrdini per i {pasto}:")
            with open(file_path, 'rb') as file_ordine:
                vett_ordini = pickle.load(file_ordine)
                for idx, ordine in enumerate(vett_ordini):
                    print(f"{ordine}x {menu.__dict__[pasto][idx]}")


class Menu():
    def __init__(self):
        self.primi = ['Pasta', 'Zuppa', 'Riso']
        self.secondi = ['Maiale', 'Manzo', 'Mozzarella', 'Funghi', 'Carciofi']
        self.contorni = ['Carote', 'Insalata', 'Finocchi', 'Patate']

        self.contaprimo = [0 for x in self.primi]
        self.contasecondo = [0 for x in self.secondi]
        self.contacontorno = [0 for x in self.contorni]


utente1 = Utente()

mensa = Mensa()

utente1.controlla_posto()

menu = Menu()

utente1.riepilogo_salvataggio()

# print(menu.contaprimo)
# print(menu.contasecondo)
# print(menu.contacontorno)

#
# with open('primi.pkl', 'rb') as file_primi:
#     print(pickle.load(file_primi))
#
# with open('secondi.pkl', 'rb') as file_secondi:
#     print(pickle.load(file_secondi))
#
# with open('contorni.pkl', 'rb') as file_contorni:
#     print(pickle.load(file_contorni))

mensa.stampa_ordini()







