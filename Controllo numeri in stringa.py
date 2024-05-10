self.Nome = Nome
        Nome = input()
        while any(char.isdigit() for char in Nome):
            print('Errore! Inserire stringa')
            Nome = input()
