#!/usr/bin/env/python3

def create_table(cursor):
    """
    This function assumes the user is already connected to the MySQL server and executes the
    necessary commands via the input cursor to create a multitude of tables:
    :param: mysql.connector cursor object
    :output tables:
        proteins
        go_classifications
        additional_info
        biological_functions
        pathways
        metabolites
        gene_properties
        protein_properties
        references
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Proteins (
            accession VARCHAR(255) PRIMARY KEY,
            version VARCHAR(255),
            creation_date VARCHAR(255),
            update_date VARCHAR(255),
            protein_name VARCHAR(255),
            protein_type VARCHAR(255),
            gene_name VARCHAR(255)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Biological_Functions (
            accession VARCHAR(255),
            general_function TEXT,
            specific_function TEXT,
            FOREIGN KEY(accession) REFERENCES Proteins(accession)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pathways (
            accession VARCHAR(255),
            pathway_name VARCHAR(255),
            FOREIGN KEY(accession) REFERENCES Proteins(accession)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Metabolites (
            metabolite_accession VARCHAR(255),
            metabolite_name VARCHAR(255),
            protein_accession VARCHAR(255),
            FOREIGN KEY(protein_accession) REFERENCES Proteins(accession)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Go_Classifications (
            accession VARCHAR(255),
            category VARCHAR(255),
            description VARCHAR(255),
            go_id VARCHAR(255),
            FOREIGN KEY(accession) REFERENCES Proteins(accession)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Gene_Properties (
            accession VARCHAR(255),
            chromosome_location VARCHAR(255),
            locus VARCHAR(255),
            gene_sequence MEDIUMTEXT,
            FOREIGN KEY(accession) REFERENCES Proteins(accession)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Protein_Properties (
            accession VARCHAR(255),
            residue_number INT,
            molecular_weight FLOAT,
            theoretical_pi FLOAT,
            polypeptide_sequence TEXT,
            FOREIGN KEY(accession) REFERENCES Proteins(accession)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Additional_Info (
            accession VARCHAR(255),
            genbank_protein_id VARCHAR(255),
            uniprot_id VARCHAR(255),
            FOREIGN KEY(accession) REFERENCES Proteins(accession)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Literature_References (
            accession VARCHAR(255),
            reference_text TEXT,
            FOREIGN KEY(accession) REFERENCES Proteins(accession)
        );
    """)