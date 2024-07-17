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

def create_posseduta_da(persona_id, sim_id):
    driver = get_db()
    with driver.session() as session:
        session.run(
            "MATCH (p:Persona {id: $persona_id}), (s:Sim {id: $sim_id}) "
            "CREATE (p)-[:POSSIEDE]->(s)",
            persona_id=persona_id, sim_id=sim_id
        )
    driver.close()
    
def create_connessa_a(sim_id, cella_id, datetime):
    driver = get_db()
    with driver.session() as session:
        session.run(
            "MATCH (s:Sim {id: $sim_id}), (c:Cella {id: $cella_id}) "
            "CREATE (s)-[:CONNESSO_A {datetime: $datetime}]->(c)",
            sim_id=sim_id, cella_id=cella_id, datetime=datetime
        )
    driver.close()
def create_dati(session):
    with session.begin_transaction() as tx:
        create_persona(tx, 'Mirko', 'La\'Rocca')
        create_persona(tx, 'Marco', 'Rogic')
        create_persona(tx, 'Michele', 'Potsios')
        create_persona(tx, 'Mario', 'Campana')
        
        create_sim(tx, '11111111')
        create_sim(tx, '22222222')
        create_sim(tx, '33333333')
        create_sim(tx, '44444444')
        
        create_cella(tx, 41.890251, 12.492373,"zona sud" )
        create_cella(tx, 45.464203, 9.189982, "zona est" )
        create_cella(tx, 40.851775, 14.268124,"zona ovest" )
        
        create_posseduta_da(tx, 'Mirko', 'La\'Rocca', '11111111')
        create_posseduta_da(tx, 'Marco', 'Rogic', '22222222')
        create_posseduta_da(tx, 'Michele', 'Potsios', '33333333')
        create_posseduta_da(tx, 'Mario', 'Capana', '44444444')
        
        create_connessa_a(tx, '11111111', 34, '2022-10-04', '12:00:00')
        create_connessa_a(tx, '22222222', 1938234, '2022-10-04', '12:33:00')
        create_connessa_a(tx, '33333333', 1938234, '2022-10-04', '12:33:00')
        create_connessa_a(tx, '44444444', 567890, '2022-10-04', '14:00:00')
def main():
    persona_id = create_persona("Giorgio", "Ciampi")
    sim_id = create_sim("123456789")
    cella_id = create_cella("45.47709", "9.15385", "Zona Centrale")
    create_posseduta_da(persona_id, sim_id)
    create_connessa_a(sim_id, cella_id, "2024-09-15T10:30:00")

if __name__ == "__main__":
    main()