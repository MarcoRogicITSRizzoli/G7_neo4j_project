from neo4j import GraphDatabase

def connection():
    URI = "neo4j+s://812006b6.databases.neo4j.io"
    AUTH = ("neo4j", "75iv38TCxoBIwqr32hDK99NVuDEmUDRcRxM87Hs4yZI")

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()