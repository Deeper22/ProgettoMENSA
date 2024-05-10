import tkinter as tk
from tkinter import ttk

class PersonaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inserimento Persona")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.nome_label = tk.Label(self.frame, text="Nome:")
        self.nome_label.grid(row=0, column=0, padx=5, pady=5)
        self.nome_entry = tk.Entry(self.frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        self.cognome_label = tk.Label(self.frame, text="Cognome:")
        self.cognome_label.grid(row=1, column=0, padx=5, pady=5)
        self.cognome_entry = tk.Entry(self.frame)
        self.cognome_entry.grid(row=1, column=1, padx=5, pady=5)

        self.matricola_label = tk.Label(self.frame, text="Matricola (senza S):")
        self.matricola_label.grid(row=2, column=0, padx=5, pady=5)
        self.matricola_entry = tk.Entry(self.frame)
        self.matricola_entry.grid(row=2, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(self.frame, text="Salva", command=self.salva_persona)
        self.submit_button.grid(row=3, columnspan=2, padx=5, pady=10)

    def salva_persona(self):
        nome = self.nome_entry.get()
        cognome = self.cognome_entry.get()
        matricola = self.matricola_entry.get()

        if self.verifica_nome_cognome(nome, cognome) and self.verifica_matricola(matricola):
            persona = Persona(nome, cognome, matricola)
            self.crea_menu(persona)
        else:
            print("Inserimento non valido. Riprova.")

    def verifica_nome_cognome(self, nome, cognome):
        if not nome.replace(" ", "").isalpha() or not cognome.replace(" ", "").isalpha():
            return False
        return True

    def verifica_matricola(self, matricola):
        if not matricola.isdigit() or len(matricola) != 7:
            return False
        return True

    def crea_menu(self, persona):
        self.menu_window = tk.Toplevel(self.root)
        self.menu_window.title("Selezione Menu")

        piatti_primo = ["Pasta", "Riso", "Zuppa"]
        piatti_secondo = ["Pollo", "Pesce", "Manzo"]
        contorni = ["Insalata", "Verdure Grigliate", "Patate"]

        primo_label = tk.Label(self.menu_window, text="Primo Piatto:")
        primo_label.grid(row=0, column=0, padx=5, pady=5)
        self.primo_combobox = ttk.Combobox(self.menu_window, values=piatti_primo)
        self.primo_combobox.grid(row=0, column=1, padx=5, pady=5)

        secondo_label = tk.Label(self.menu_window, text="Secondo Piatto:")
        secondo_label.grid(row=1, column=0, padx=5, pady=5)
        self.secondo_combobox = ttk.Combobox(self.menu_window, values=piatti_secondo)
        self.secondo_combobox.grid(row=1, column=1, padx=5, pady=5)

        contorno_label = tk.Label(self.menu_window, text="Contorno:")
        contorno_label.grid(row=2, column=0, padx=5, pady=5)
        self.contorno_combobox = ttk.Combobox(self.menu_window, values=contorni)
        self.contorno_combobox.grid(row=2, column=1, padx=5, pady=5)

        conferma_button = tk.Button(self.menu_window, text="Conferma", command=lambda: self.stampa_ordine(persona))
        conferma_button.grid(row=3, columnspan=2, padx=5, pady=10)

    def stampa_ordine(self, persona):
        primo_piatto = self.primo_combobox.get()
        secondo_piatto = self.secondo_combobox.get()
        contorno = self.contorno_combobox.get()

        print("Ordine per", persona.nome, persona.cognome)
        print("Primo Piatto:", primo_piatto)
        print("Secondo Piatto:", secondo_piatto)
        print("Contorno:", contorno)

class Persona:
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonaApp(root)
    root.mainloop()
