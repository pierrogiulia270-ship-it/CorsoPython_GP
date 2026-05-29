print("\n=======Ciao Benvenuto =======")
# Chiediamo all'utente di inserire i suoi dati
nome = input ("Inserisci tuo nome: ")
cognome = input(f"Inserisci tuo cognome {nome}: ")
eta = int(input (f" Quanti annni hai? "))
altezza = float (input ("Quanto sei alto? "))

# Stampa i dati inseriti
print(f"ciao {nome} {cognome}, hai {eta} anni e sei alto {altezza} metri.")