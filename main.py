class Persona():
    def __init__(self):


        #FUNZIONE CONTROLLO STRINGA
        def ControlloSTR(stringa):
            while any(char.isdigit() for char in stringa) or len(stringa)==0:
                print('Errore! Inserire stringa non vuota')
                stringa = input()


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
        while not matricola.isdigit() or len(matricola)!=7:
            print('Errore! Inserisci numero di 7 cifre')
            matricola = input('Inserisci matricola: ')
        self.matricola = matricola




persona1 = Persona()







