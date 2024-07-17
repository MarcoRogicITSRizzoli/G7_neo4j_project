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
            latitudine=float(latitudine), longitudine=float(longitudine), nome=nome)
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
    
def create_connessa_a(sim_id, cella_id, data, ora):
    driver = get_db()
    with driver.session() as session:
        session.run(
            "MATCH (s:Sim {id: $sim_id}), (c:Cella {id: $cella_id})"
            "CREATE (s)-[:CONNESSO_A {date: $data, time: $ora}]->(c)",
            sim_id=sim_id, cella_id=cella_id, data=data, ora=ora
        )
    driver.close()

def main():
    persona_id = create_persona("Giorgio", "Ciampi")
    sim_id = create_sim("123456789")
    cella_id = create_cella(45.47709, 9.15385, "Zona Centrale")
    create_posseduta_da(persona_id, sim_id)
    create_connessa_a(sim_id, cella_id, "2024-09-15", "10:30:00")
    
    persona_id1 = create_persona('Mirko', 'La\'Rocca')
    persona_id2 = create_persona('Marco', 'Rogic')
    persona_id3 = create_persona('Michele', 'Potsios')
    persona_id4 = create_persona('Mario', 'Campana')
    
    sim_id1 = create_sim('11111111')
    sim_id2 = create_sim('22222222')
    sim_id3 = create_sim('33333333')
    sim_id4 = create_sim('44444444')
    
    cella_id1 = create_cella(41.890251, 12.492373,"zona sud" )
    cella_id2 = create_cella(45.464203, 9.189982, "zona est" )
    cella_id3 = create_cella(40.851775, 14.268124,"zona ovest" )
    
    create_posseduta_da(persona_id1, sim_id1)
    create_posseduta_da(persona_id2, sim_id2)
    create_posseduta_da(persona_id3, sim_id3)
    create_posseduta_da(persona_id4, sim_id4)
    
    create_connessa_a(sim_id1, cella_id1, '2024-10-04', '12:00:00')
    create_connessa_a(sim_id2, cella_id2, '2024-10-04', '12:33:00')
    create_connessa_a(sim_id3, cella_id3, '2024-10-04', '12:33:00')
    create_connessa_a(sim_id4, cella_id2, '2024-10-04', '14:00:00')

if __name__ == "__main__":
    main()