def localizzare_persona(session, nome, data_inizio, data_fine):
    with session.begin_transaction() as tx:
        query = (
            "MATCH (p:Persona {nome: $nome})-[:POSSEDUTA_DA]->(s:Sim)-[r:CONNESSA_A]->(c:CellaTelefonica) "
            "WHERE r.data >= $data_inizio AND r.data <= $data_fine "
            "RETURN p.nome, s.numero, c.id, r.data, r.orario"
        )
        result = tx.run(query, nome=nome, data_inizio=data_inizio, data_fine=data_fine)
        for record in result:
            print(record)

def trovare_sospetti(session, data_ora, cella):
    with session.begin_transaction() as tx:
        query = (
            "MATCH (p:Persona)-[:POSSEDUTA_DA]->(s:Sim)-[r:CONNESSA_A]->(c:CellaTelefonica {id: $cella}) "
            "WHERE r.data = $data_ora "
            "RETURN p.nome, s.numero, c.id, r.data, r.orario"
        )
        result = tx.run(query, data_ora=data_ora, cella=cella)
        for record in result:
            print(record)

def persone_nelle_vicinanze(session, data_ora, latitudine, longitudine, raggio):
    with session.begin_transaction() as tx:
        query = (
            "MATCH (p:Persona)-[:POSSEDUTA_DA]->(s:Sim)-[r:CONNESSA_A]->(c:CellaTelefonica) "
            "WHERE point.distance(point({latitude: c.latitudine, longitudine: c.longitudine}), point({latitudine: $latitudine, longitudine: $longitudine})) <= $raggio "
            "AND r.data = $data_ora "
            "RETURN p.nome, s.numero, c.id, r.data, r.orario"
        )
        result = tx.run(query, data_ora=data_ora, latitudine=latitudine, longitudine=longitudine, raggio=raggio)
        for record in result:
            print(record)
