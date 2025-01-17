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
    
def create_connessa_a(sim_id, cella_id, data_inizio, data_fine, ora_inizio, ora_fine):
    driver = get_db()
    with driver.session() as session:
        session.run(
            "MATCH (s:Sim {id: $sim_id}), (c:Cella {id: $cella_id})"
            "CREATE (s)-[:CONNESSO_A {data_inizio: $data_inizio, data_fine: $data_fine, ora_inizio: $ora_inizio, ora_fine: $ora_fine}]->(c)",
            sim_id=sim_id, cella_id=cella_id, data_inizio=data_inizio, data_fine=data_fine, ora_inizio=ora_inizio, ora_fine=ora_fine
        )
    driver.close()

def main():
    persona_id = create_persona("Giorgio", "Ciampi")
    sim_id = create_sim("123456789")
    cella_id = create_cella(45.47709, 9.226652, "Zona Centrale")
    create_posseduta_da(persona_id, sim_id)
    create_connessa_a(sim_id, cella_id, "2024-10-02", "2024-10-14", "12:00:00", "10:30:00")
    
    persona_id1 = create_persona('Mirko', 'La Rocca')
    persona_id2 = create_persona('Marco', 'Rogic')
    persona_id3 = create_persona('Michele', 'Potsios')
    persona_id4 = create_persona('Mario', 'Campana')
    
    sim_id1 = create_sim('11111111')
    sim_id2 = create_sim('22222222')
    sim_id3 = create_sim('33333333')
    sim_id4 = create_sim('44444444')
    
    cella_id1 = create_cella(45.487637, 9.154266,"zona sud" )
    cella_id2 = create_cella(45.436214, 9.155479, "zona est" )
    cella_id3 = create_cella(45.437086, 9.228240,"zona ovest" )
    
    create_posseduta_da(persona_id1, sim_id1)
    create_posseduta_da(persona_id2, sim_id2)
    create_posseduta_da(persona_id3, sim_id3)
    create_posseduta_da(persona_id4, sim_id4)
    
    create_connessa_a(sim_id1, cella_id1, '2024-10-04', '2024-11-04', '12:00:00', '12:00:00')
    create_connessa_a(sim_id2, cella_id2, '2024-10-04', '2024-11-04', '12:00:00', '12:00:00')
    create_connessa_a(sim_id3, cella_id3, '2024-10-04', '2024-11-04', '12:00:00', '12:00:00')
    create_connessa_a(sim_id4, cella_id2, '2024-10-04', '2024-11-04', '12:00:00', '12:00:00')

if __name__ == "__main__":
    main()