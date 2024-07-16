from database import *

def create_persona(nome, cognome):
    driver = get_db()
    with driver.session() as session:
        result = session.run(
            "CREATE (p:Persona {id: apoc.create.uuid(), nome: $nome, cognome: $cognome}) RETURN p.id AS id",
            nome=nome, cognome=cognome)
        persona_id = result.single()["id"]
    driver.close()
    return persona_id

def create_sim(numero):
    driver = get_db()
    with driver.session() as session:
        result = session.run(
            "CREATE (s:Sim {id: apoc.create.uuid(), numero: $numero}) RETURN s.id AS id",
            numero=numero)
        sim_id = result.single()["id"]
    driver.close()
    return sim_id
    
def create_cella(latitudine, longitudine, nome):
    driver = get_db()
    with driver.session() as session:
        result = session.run(
            "CREATE (c:Cella {id: apoc.create.uuid(), latitudine: $latitudine, longitudine: $longitudine, nome: $nome}) RETURN c.id AS id",
            latitudine=latitudine, longitudine=longitudine, nome=nome)
        cella_id = result.single()["id"]
    driver.close()
    return cella_id

def create_possiede_rel(persona_id, sim_id):
    driver = get_db()
    with driver.session() as session:
        session.run(
            "MATCH (p:Persona {id: $persona_id}), (s:Sim {id: $sim_id}) "
            "CREATE (p)-[:POSSIEDE]->(s)",
            persona_id=persona_id, sim_id=sim_id
        )
    driver.close()
    
def create_connesso_rel(sim_id, cella_id, datetime):
    driver = get_db()
    with driver.session() as session:
        session.run(
            "MATCH (s:Sim {id: $sim_id}), (c:Cella {id: $cella_id}) "
            "CREATE (s)-[:CONNESSO_A {datetime: $datetime}]->(c)",
            sim_id=sim_id, cella_id=cella_id, datetime=datetime
        )
    driver.close()

def main():
    persona_id = create_persona("Giorgio", "Ciampi")
    sim_id = create_sim("123456789")
    cella_id = create_cella("45.47709", "9.15385", "Zona Centrale")
    create_possiede_rel(persona_id, sim_id)
    create_connesso_rel(sim_id, cella_id, "2024-09-15T10:30:00")

if __name__ == "__main__":
    main()