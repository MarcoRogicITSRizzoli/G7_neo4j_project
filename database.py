from neo4j import GraphDatabase

URI = "neo4j+s://a8164252.databases.neo4j.io"
AUTH = ("neo4j", "QerPSe8CeH5Lk9VWaD3_VCN-GZX1dkCPEGVl0uYFb8o")

def get_db():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    return driver

def verify_connectivity():
    with get_db() as driver:
        driver.verify_connectivity
        print("Connected to the database successfully.")

def close_db(driver):
    driver.close()