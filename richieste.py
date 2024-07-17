from database import get_db

def find_cells_by_persona(data, ora, nome, cognome):
    driver = get_db()
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Persona {nome: $nome, cognome: $cognome})-[:POSSIEDE]->(s:Sim)-[r:CONNESSO_A {data_ora: $data_ora}]->(c:Cella)
            RETURN c.id, c.latitudine, c.longitudine
            """,
            nome=nome, cognome=cognome, data_ora=f"{data}T{ora}"
        )
    driver.close()
    return [record for record in result]

def find_personas_by_cell(data, ora, cella_id):
    driver = get_db()
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Persona)-[:POSSIEDE]->(s:Sim)-[r:CONNESSO_A {data_ora: $data_ora}]->(c:Cella {id: $cella_id})
            RETURN p.id, p.nome, p.cognome
            """,
            cella_id=cella_id, data_ora=f"{data}T{ora}"
        )
    driver.close()
    return [record for record in result]

def find_personas_by_radius(data, ora, latitudine, longitudine, raggio):
    driver = get_db()
    with driver.session() as session:
        result = session.run(
            """
            MATCH (p:Persona)-[:POSSIEDE]->(s:Sim)-[r:CONNESSO_A {data_ora: $data_ora}]->(c:Cella)
            WHERE point.distance(point({latitude: c.latitudine, longitude: c.longitudine}), point({latitude: $latitudine, longitude: $longitudine})) <= $raggio
            RETURN p.id, p.nome, p.cognome
            """,
            data_ora=f"{data}T{ora}", latitudine=latitudine, longitudine=longitudine, raggio=raggio
        )
    driver.close()
    return [record for record in result]