# G7_neo4j_project

Panoramica

Questo progetto è un'applicazione Python che interagisce con un database Neo4j per gestire e interrogare le connessioni tra persone (Persone), SIM e celle telefoniche (Celle). L'applicazione include funzionalità per creare voci nel database e interrogarlo in base a criteri specifici.

File

main.py: Il file principale dell'applicazione che fornisce un'interfaccia a riga di comando per interrogare il database.
create.py: Uno script per popolare il database con dati iniziali.
database.py: Contiene funzioni per connettersi al database Neo4j.
richieste.py: Contiene funzioni per interrogare il database.
Requisiti

Python 3.x
Database Neo4j
Pacchetto Python neo4j (pip install neo4j)
Configurazione

Installare i Pacchetti Python
Assicurati di installare i pacchetti Python richiesti eseguendo:
pip install neo4j

Configurare la Connessione al Database
Assicurati che i dettagli della connessione al database Neo4j in database.py siano corretti

Esecuzione dell'Applicazione

Inizializzare i Dati

Prima di eseguire il file main.py, è necessario popolare il database con dati iniziali. Esegui il file create.py:
python create.py
Questo creerà le voci iniziali nel database necessarie per le interrogazioni.

Eseguire l'Applicazione Principale

Dopo aver popolato il database, esegui il file main.py per avviare l'applicazione principale:

Funzionalità Principali

main.py

Opzione 1: Trova celle collegate a una persona in una data e ora specifica.
Opzione 2: Trova persone collegate a una cella in una data e ora specifica.
Opzione 3: Trova persone entro un certo raggio da una cella in una data e ora specifica.
Opzione 4: Esci dall'applicazione.
create.py

Crea persone, SIM e celle telefoniche nel database.
Stabilisce le relazioni tra persone e SIM e tra SIM e celle telefoniche.
database.py

Connessione al database Neo4j.
Funzione per verificare la connettività al database.
richieste.py

Funzioni per trovare celle collegate a una persona.
Funzioni per trovare persone collegate a una cella.
Funzioni per trovare persone entro un certo raggio da una cella.
Assicurati di eseguire prima create.py per popolare il database, altrimenti le interrogazioni in main.py non restituiranno risultati significativi.