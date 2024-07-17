from database import *
from richieste import *
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        print("1. Celle collegate a Persona in una data e ora specifica")
        print("2. Persone collegate a una Cella in una data e ora specifica")
        print("3. Persone entro un certo raggio da una Cella in una data e ora specifica")
        print("4. Esci")
        choice = input("Scegli un'opzione: ")
        
        clear_screen()

        if choice == '1':
            nome = input("Nome Persona: ")
            cognome = input("Cognome Persona: ")
            data = input("Data (YYYY-MM-DD): ")
            ora = input("Ora (HH:MM:SS): ")
            celle = find_cells_by_persona(data, ora, nome, cognome)
            print("Le sim di questa persona si sono collegate alla/e seguenti cella/e:")
            for cella in celle:
                print(f"Cella ID: {cella['c.id']}, Latitudine: {cella['c.latitudine']}, Longitudine: {cella['c.longitudine']}")
            input("\nPremi Invio per continuare...")

        elif choice == '2':
            cella_id = input("ID Cella: ")
            data = input("Data (YYYY-MM-DD): ")
            ora = input("Ora (HH:MM:SS): ")
            persone = find_personas_by_cell(data, ora, cella_id)
            print("Persone collegate alla Cella:")
            for persona in persone:
                print(f"Persona ID: {persona['p.id']}, Nome: {persona['p.nome']}, Cognome: {persona['p.cognome']}")
            input("\nPremi Invio per continuare...")

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
            input("\nPremi Invio per continuare...")

        elif choice == '4':
            break

        else:
            print("Scelta non valida. Riprova.")
            input("\nPremi Invio per continuare...")

if __name__ == "__main__":
    main()