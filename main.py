from neo4j import GraphDatabase
from richieste import localizzare_persona, trovare_sospetti, persone_nelle_vicinanze

def main():
    while True:
        print("1. Lv 1: Celle collegate a Persona in una data e ora specifica")
        print("2. Lv 2: Persone collegate a una Cella in una data e ora specifica")
        print("3. Lv 3: Persone entro un certo raggio da una Cella in una data e ora specifica")
        print("4. Esci")
        choice = input("Scegli un'opzione: ")

        if choice == '1':
            nome = input("Nome Persona: ")
            cognome = input("Cognome Persona: ")
            data = input("Data (YYYY-MM-DD): ")
            ora = input("Ora (HH:MM:SS): ")
            celle = find_cells_by_persona(data, ora, nome, cognome)
            print("Le sim di questa persona si sono collegate alla/e seguenti cella/e:")
            for cella in celle:
                print(f"Cella ID: {cella['c.id']}, Latitudine: {cella['c.latitudine']}, Longitudine: {cella['c.longitudine']}")

        elif choice == '2':
            cella_id = input("ID Cella: ")
            data = input("Data (YYYY-MM-DD): ")
            ora = input("Ora (HH:MM:SS): ")
            persone = find_personas_by_cell(data, ora, cella_id)
            print("Persone collegate alla Cella:")
            for persona in persone:
                print(f"Persona ID: {persona['p.id']}, Nome: {persona['p.nome']}, Cognome: {persona['p.cognome']}")

        elif choice == '3':
            latitudine = float(input("Latitudine: "))
            longitudine = float(input("Longitudine: "))
            raggio = float(input("Raggio (in metri): "))
            data = input("Data (YYYY-MM-DD): ")
            ora = input("Ora (HH:MM:SS): ")
            persone = find_personas_by_radius(data, ora, latitudine, longitudine, raggio)
            print("Persone entro il raggio specificato:")
            for persona in persone:
                print(f"Persona ID: {persona['p.id']}, Nome: {persona['p.nome']}, Cognome: {persona['p.cognome']}")

        elif choice == '4':
            break

        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()