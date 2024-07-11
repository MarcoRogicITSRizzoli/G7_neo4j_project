import datetime

# Simuliamo un database di esempio
database_sim = {
    'Gigi Marraffa': [
        {'data': '2022-10-04', 'cella': 34},
        {'data': '2022-10-05', 'cella': 34},
        # Aggiungere altre entries
    ],
    'Tony Ladroni': [
        {'data': '2022-10-04 12:33:00', 'cella': 1938234, 'numero': '+3902020202'},
        # Aggiungere altre entries
    ],
    'Maria La Truffa': [
        {'data': '2022-10-04 12:33:00', 'cella': 1938234, 'numero': '+393983'},
        # Aggiungere altre entries
    ]
}

# Funzione per localizzare una persona
def localizzare_persona(nome, data_inizio, data_fine):
    if nome in database_sim:
        dati_persona = database_sim[nome]
        result = []
        for entry in dati_persona:
            data_entry = datetime.datetime.strptime(entry['data'], '%Y-%m-%d')
            if data_inizio <= data_entry <= data_fine:
                result.append(entry)
        return result
    else:
        return None

# Funzione per trovare sospetti in una zona
def trovare_sospetti(data_ora, cella):
    result = []
    for nome, dati in database_sim.items():
        for entry in dati:
            if entry.get('cella') == cella and entry.get('data') == data_ora:
                result.append({'nome': nome, 'numero': entry.get('numero')})
    return result

# Funzione per elencare persone nelle vicinanze di un luogo
def persone_nelle_vicinanze(data_ora, coordinate):
    # Supponiamo che coordinate sia una cella per semplicità
    cella_vicina = int(coordinate.replace('.', ''))
    return trovare_sospetti(data_ora, cella_vicina)

# Interfaccia utente
def main():
    print("Applicazione per la Polizia Postale")
    scelta = input("Scegli un'opzione: 1) Localizzare una persona 2) Trovare sospetti in una zona 3) Elencare persone nelle vicinanze di un luogo: ")
    
    if scelta == '1':
        nome = input("Inserisci il nome della persona: ")
        data_inizio = input("Inserisci la data di inizio (YYYY-MM-DD): ")
        data_fine = input("Inserisci la data di fine (YYYY-MM-DD): ")
        data_inizio = datetime.datetime.strptime(data_inizio, '%Y-%m-%d')
        data_fine = datetime.datetime.strptime(data_fine, '%Y-%m-%d')
        risultato = localizzare_persona(nome, data_inizio, data_fine)
        if risultato:
            print(f'Nelle date indicate, le SIM della persona {nome} si sono trovate qui:')
            for r in risultato:
                print(r)
        else:
            print(f'Nessuna informazione trovata per {nome} nel periodo specificato.')
    
    elif scelta == '2':
        cella = input("Inserisci il numero della cella: ")
        data_ora = input("Inserisci la data e ora (YYYY-MM-DD HH:MM:SS): ")
        risultato = trovare_sospetti(data_ora, int(cella))
        if risultato:
            print(f'Le SIM collegate alla cella {cella} sono:')
            for r in risultato:
                print(r)
        else:
            print(f'Nessuna informazione trovata per la cella {cella} al momento specificato.')
    
    elif scelta == '3':
        coordinate = input("Inserisci le coordinate del luogo (Formato: xx.xxN yy.yyW): ")
        data_ora = input("Inserisci la data e ora (YYYY-MM-DD HH:MM:SS): ")
        risultato = persone_nelle_vicinanze(data_ora, coordinate)
        if risultato:
            print(f'Le SIM collegate alle celle più vicine a {coordinate} sono:')
            for r in risultato:
                print(r)
        else:
            print(f'Nessuna informazione trovata per le coordinate {coordinate} al momento specificato.')
    
    else:
        print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
