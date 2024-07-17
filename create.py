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
def create_dati():
    create_persona('Mirko', 'La\'Rocca')
    create_persona('Marco', 'Rogic')
    create_persona('Michele', 'Potsios')
    create_persona('Mario', 'Campana')
    
    create_sim('11111111')
    create_sim('22222222')
    create_sim('33333333')
    create_sim('44444444')
    
    create_cella("41.890251", "12.492373","zona sud" )
    create_cella("45.464203", "9.189982", "zona est" )
    create_cella("40.851775", "14.268124","zona ovest" )
    
    create_posseduta_da('Mirko', 'La\'Rocca', '11111111')
    create_posseduta_da('Marco', 'Rogic', '22222222')
    create_posseduta_da('Michele', 'Potsios', '33333333')
    create_posseduta_da('Mario', 'Capana', '44444444')
    
    create_connessa_a('11111111', '2022-10-04', '12:00:00')
    create_connessa_a('22222222', '2022-10-04', '12:33:00')
    create_connessa_a('33333333', '2022-10-04', '12:33:00')
    create_connessa_a('44444444', '2022-10-04', '14:00:00')
def main():
    persona_id = create_persona("Giorgio", "Ciampi")
    sim_id = create_sim("123456789")
    cella_id = create_cella("45.47709", "9.15385", "Zona Centrale")
    create_posseduta_da(persona_id, sim_id)
    create_connessa_a(sim_id, cella_id, "2024-09-15T10:30:00")
    create_dati()

if __name__ == "__main__":
    main()