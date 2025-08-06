persona={
    "nome":"Salvatore",
    "Cognome":"Ferraro",
    "eta":27
}

operazioni=("aggiungere","modificare","eliminare","leggere","0","DS")

def start():
    print("Operazioni disponibili: aggiungere, modificare, eliminare, leggere, 0 (per uscire),visualizzare i dati come Serie (DS)")
    operazione=input("Cosa vuoi fare ?: ")
    if operazione == operazioni[4]:    
        raise Exception("Arresto del programma")
    try:
        if operazione == operazioni[0]:
            x = input("Aggiungi coppia chiave:valore separati da una virgola: ")
            aggiungi(x.split(","))
        elif operazione == operazioni[1]:
            x = input("Scrivi la chiave con il nuovo valore separato da una virgola:  ")  
            modifica(x.split(","))
        elif operazione == operazioni[2]:
            x = input("Scrivi la chiave da eliminare: ")
            del persona[x]
            print(persona)   
        elif operazione == operazioni[3]:
            x = input("Scrivi la chiave da leggere: ")
            print(persona[x])
        elif operazione == operazioni[5]:
            df=pd.Series(persona)
            print(df)  
    except:
        pass            

def aggiungi(param):
    if len(param) <= 2:
        chiave = param[0]
        valore = param[1]
        persona[chiave] = valore
        print(persona)
    else:
        chiave = param[0]
        valore = str(param[1:])
        persona[chiave] = valore
        print(persona)

def modifica(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)

while True:
    try: 
        start()
    except Exception as stop:
        print("Programma terminato")  
        break
