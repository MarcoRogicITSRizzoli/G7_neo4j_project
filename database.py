from neo4j import GraphDatabase

URI = "neo4j+s://b1bb3ceb.databases.neo4j.io"
AUTH = ("", "<Password>")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()