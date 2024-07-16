from neo4j import GraphDatabase

def connection():
    URI = "neo4j+s://812006b6.databases.neo4j.io"
    AUTH = ("neo4j", "75iv38TCxoBIwqr32hDK99NVuDEmUDRcRxM87Hs4yZI")

def get_db():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    return driver

def verify_connectivity():
    with get_db() as driver:
        driver.verify_connectivity
        print("Connected to the database successfully.")

def close_db(driver):
    driver.close()