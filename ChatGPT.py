import tkinter as tk

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
            print("Dati inseriti:")
            print("Nome:", persona.nome)
            print("Cognome:", persona.cognome)
            print("Matricola:", persona.matricola)
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

class Persona:
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonaApp(root)
    root.mainloop()
