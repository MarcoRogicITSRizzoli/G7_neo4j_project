from database import *

def find_cells_by_persona(data, ora, nome, cognome):
    driver = get_db()
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Persona {nome: $nome, cognome: $cognome})-[:POSSIEDE]->(s:Sim)-[r:CONNESSO_A {date: $data, time: $ora}]->(c:Cella)
            RETURN c.id, c.latitudine, c.longitudine
            """,
            nome=nome, cognome=cognome, data_ora=f"{data}T{ora}"
        )
        records = [record for record in result]
    driver.close()
    return records

def find_personas_by_cell(data, ora, cella_id):
    driver = get_db()
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Persona)-[:POSSIEDE]->(s:Sim)-[r:CONNESSO_A {date: $data, time: $ora}]->(c:Cella {id: $cella_id})
            RETURN p.id, p.nome, p.cognome
            """,
            cella_id=cella_id, data_ora=f"{data}T{ora}"
        )
        records = [record for record in result]
    driver.close()
    return records

def find_personas_by_radius(data, ora, latitudine, longitudine, raggio):
    driver = get_db()
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Persona)-[:POSSIEDE]->(s:Sim)-[r:CONNESSO_A {date: $data, time: $ora}]->(c:Cella)
            WHERE point.distance(point({latitude: c.latitudine, longitude: c.longitudine}), point({latitude: $latitudine, longitude: $longitudine})) <= $raggio
            RETURN p.id, p.nome, p.cognome
            """,
            data_ora=f"{data}T{ora}", latitudine=latitudine, longitudine=longitudine, raggio=raggio
        )
        records = [record for record in result]
    driver.close()
    return records