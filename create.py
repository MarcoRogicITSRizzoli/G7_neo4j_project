from database import *

def create_nodes():
    query = ("CREATE (p:Person {name: 'Giorgio Ciampi'})-[:Possiede]->(s:Sim {number: '+39333333333'})-[:Connesso]->(c:Telefono {id: '1', data: '2024-07-30})")
    tx.run(query)
    
if __name__=="__main__":