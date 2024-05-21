import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle

class Utente():
    def __init__(self, root):
        self.root = root
        self.root.title("Mensa App - Utente")

        # Creazione etichette e campi di input
        tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Cognome:").grid(row=1, column=0, padx=10, pady=5)
        self.cognome_entry = tk.Entry(root)
        self.cognome_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Matricola:").grid(row=2, column=0, padx=10, pady=5)
        self.matricola_entry = tk.Entry(root)
        self.matricola_entry.grid(row=2, column=1, padx=10, pady=5)

        # Bottone per inviare i dati
        tk.Button(root, text="Invia", command=self.registra_utente).grid(row=3, columnspan=2, padx=10, pady=10)

    def registra_utente(self):
        nome = self.nome_entry.get()
        cognome = self.cognome_entry.get()
        matricola = self.matricola_entry.get()

        # Controllo dei campi vuoti
        if not nome or not cognome or not matricola:
            messagebox.showerror("Errore", "Inserire tutti i campi.")
            return

        # Controllo della matricola
        if not matricola.isdigit() or len(matricola) != 7:
            messagebox.showerror("Errore", "Inserire una matricola valida (7 cifre).")
            return

        # Salvataggio dei dati
        with open('utente.pkl', 'wb') as f:
            pickle.dump({'nome': nome, 'cognome': cognome, 'matricola': matricola}, f)

        # Apertura della finestra per la scelta dei pasti
        self.scelta_pastri()

    def scelta_pastri(self):
        # Qui puoi implementare la finestra per la scelta dei pasti
        pass

class Admin():
    def __init__(self, root):
        self.root = root
        self.root.title("Mensa App - Admin")

        # Creazione del pulsante per il reset dei posti
        tk.Button(root, text="Resetta posti", command=self.reset_posti).pack(pady=10)

    def reset_posti(self):
        posti_int = simpledialog.askinteger("Resetta posti", "Quanti posti vuoi rendere disponibili?")
        if posti_int is not None:
            with open('posti.pkl', 'wb') as posti:
                pickle.dump(posti_int, posti)
            messagebox.showinfo("Successo", "Sono ora disponibili {} posti.".format(posti_int))

class Mensa():
    def __init__(self):
        try:
            with open('posti.pkl', 'rb') as posti:
                self.posti_disponibili = pickle.load(posti)
        except FileNotFoundError:
            # Se il file non esiste, lo crea con un numero predefinito di posti
            self.posti_disponibili = 50
            with open('posti.pkl', 'wb') as posti:
                pickle.dump(self.posti_disponibili, posti)

def login():
    root = tk.Tk()
    root.title("Mensa App - Login")

    tk.Label(root, text="Accedi come:").pack(pady=10)

    def login_utente():
        root.destroy()
        Utente(tk.Tk())

    def login_admin():
        root.destroy()
        Admin(tk.Tk())

    tk.Button(root, text="Utente", command=login_utente).pack(pady=5)
    tk.Button(root, text="Admin", command=login_admin).pack(pady=5)

    root.mainloop()

def main():
    mensa = Mensa()
    login()

if __name__ == "__main__":
    main()
