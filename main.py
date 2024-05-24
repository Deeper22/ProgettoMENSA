import sys
import time
import pickle

class Utente():

    def ControlloSTR(self, stringa):
        while any(lettera.isdigit() for lettera in stringa) or len(stringa)==0:
            print('Errore! Inserire stringa non vuota')
            stringa = input()


    def ControlloMTR(self, matr):
        while not matr.isdigit() or len(matr)!=7:
            print('Errore! Inserisci numero di 7 cifre')
            matr = input('Inserisci matricola: ')

    def __init__(self):

        #INSERIMENTO E CONTROLLO NOME
        nome = input('Inserisci nome: ')
        self.ControlloSTR(nome)
        self.nome = nome

        #INSERIMENTO E CONTROLLO COGNOME
        cognome = input('Inserisci cognome: ')
        self.ControlloSTR(cognome)
        self.cognome = cognome

        #INSERIMENTO E CONTROLLO MATRICOLA
        matricola = input('Inserisci matricola: ')
        self.ControlloMTR(matricola)
        self.matricola = matricola

        with open('utenti.txt', 'r') as file_utenti:
            for riga in file_utenti:
                if riga.strip() == self.matricola:
                    print('\nPrenotazione gia effetuata!')
                    sys.exit()

        self.controlla_posto()

        with open('utenti.txt', 'a') as file_utenti:
            file_utenti.write(self.matricola + '\n')

        self.riepilogo_salvataggio()


    #CONTROLLO DISPONIBILITA POSTI IN MENSA
    def controlla_posto(self):

        time.sleep(1)

        if mensa.posti_disponibili == 0:

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
            # if len(vett_temp) != len(vett_pickle):
            #     nome_file.seek(0)   #Si porta il puntatore del file all'inizio per sovrascrivere
            #     nome_file.truncate()   #Svuota il file
            #     vett_temp = [0] * len(vett_pickle)
            #     pickle.dump(vett_temp, nome_file)
            nome_file.seek(0)
            vett_pickle = [x + y for x, y in zip(vett_temp, vett_pickle)]
            pickle.dump(vett_pickle, nome_file)


    #SCELTA DEI PIATTI DA MANGIARE
    def riepilogo_salvataggio(self):

        time.sleep(1)
        print('\n\tSCELTA PASTI')

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


class Admin():
    def __init__(self):

        self.password_admin = 'admin'

        password_inserita = input('Inserisci password ADMIN: ')
        while (password_inserita != self.password_admin) or (password_inserita == ''):
            password_inserita = input('Password ERRATA. Riprova: ')

        self.Menu_Admin()

    def Menu_Admin(self):
        print('\n\tMENU ADMIN\n')
        admin_digit = input("1. Reset posti mensa\n2. Cambia menu\n3. Visualizza totale ordini\n4. Reset utenti prenotati\n5. Ritorna al login\n6. Esci dal programma\n\nInserisci numero dell'operazione desiderata: ")
        while admin_digit not in ('1','2','3','4','5','6'):
            admin_digit = input('Inserimento non valido. Riprova: ')
        if admin_digit == '1':
            self.reset_posti()
        elif admin_digit == '2':
            self.cambia_menu()
        elif admin_digit == '3':
            self.visualizza_ordini()
        elif admin_digit == '4':
            self.reset_utenti()
        elif admin_digit == '5':
            Login()
        elif admin_digit == '6':
            sys.exit()

    def reset_posti(self):

        input_posti = input('Quanti posti vuoi rendere disponibili?: ')
        while not input_posti.isdigit():
            input_posti = input('Inserimento non valido. Riprova: ')
        posti_int = int(input_posti)

        with open('posti.pkl', 'wb') as posti:
            pickle.dump(posti_int, posti)
        mensa.posti_disponibili = posti_int
        print('Sono ora disponibili {} posti.'.format(posti_int))

        input('\nPremi invio per tornare al menu')
        self.Menu_Admin()

    def cambia_menu(self):
        print('\n\t  CAMBIO MENU\n(comporta il reset ordini)')
        primi_inseriti = input('\nDigita i primi da inserire, separati da una virgola:\n').split(',')
        secondi_inseriti = input('Digita i secondi da inserire, separati da una virgola:\n').split(',')
        contorni_inseriti = input('Digita i contorni da inserire, separati da una virgola:\n').split(',')

        primi_inseriti = [item.strip() for item in primi_inseriti]
        secondi_inseriti = [item.strip() for item in secondi_inseriti]
        contorni_inseriti = [item.strip() for item in contorni_inseriti]

        menu.primi = primi_inseriti
        menu.secondi = secondi_inseriti
        menu.contorni = contorni_inseriti

        with open('menu.pkl', 'wb') as file_menu:
            menu_agg_pickle = {
                'primi' : menu.primi,
                'secondi' : menu.secondi,
                'contorni' : menu.contorni
            }
            pickle.dump(menu_agg_pickle, file_menu)

        pasti = ['primi', 'secondi', 'contorni']
        for pasto in pasti:
            with open(pasto + '.pkl', 'wb') as file_ordine:
                pickle.dump([0] * len(menu.__dict__[pasto]), file_ordine)

        print('\nMenu aggiornato e ordini resettati con successo!')

        input('\nPremi invio per tornare al menu')
        self.Menu_Admin()


    def visualizza_ordini(self):
        pasti = ['primi', 'secondi', 'contorni']
        for pasto in pasti:
            print("\nOrdini per i {}:".format(pasto))
            with open(pasto + '.pkl', 'rb') as file_ordine:
                vett_ordini = pickle.load(file_ordine)
                for idx, ordine in enumerate(vett_ordini):
                    print("{}: {}".format(menu.__dict__[pasto][idx], ordine))

        input('\nPremi invio per tornare al menu')
        self.Menu_Admin()

    def reset_utenti(self):
        with open('utenti.txt', 'w') as file_utenti:
            file_utenti.write('')
        print('\nLista utenti prenotati svuotata con successo.')
        input('\nPremi invio per tornare al menu')
        self.Menu_Admin()

class Mensa():

    def __init__(self):
        with open('posti.pkl', 'rb') as posti:
            self.posti_disponibili = pickle.load(posti)


class Menu():
    def __init__(self):

        with open('menu.pkl', 'rb') as file_menu:
            menu_pickle = pickle.load(file_menu)
            self.primi = menu_pickle['primi']
            self.secondi = menu_pickle['secondi']
            self.contorni = menu_pickle['contorni']

        # with open('menu.pkl', 'wb') as file_menu:
        #     menu_pickle = {
        #         'primi' : self.primi,
        #         'secondi' : self.secondi,
        #         'contorni' : self.contorni,
        #     }
        #     pickle.dump(menu_pickle, file_menu)


        self.contaprimo = [0 for x in self.primi]
        self.contasecondo = [0 for x in self.secondi]
        self.contacontorno = [0 for x in self.contorni]

mensa = Mensa()
menu = Menu()

def Login():
    login_digit = input('Accedi come:\n1. Utente\n2. Admin\n')
    while (login_digit != '1') and (login_digit != '2'):
        login_digit = input('Inserimento non valido. Riprova: ')

    if login_digit == '1':
        utente1 = Utente()
    elif login_digit == '2':
        admin1 = Admin()


Login()





