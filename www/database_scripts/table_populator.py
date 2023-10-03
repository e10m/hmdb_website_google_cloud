#!/usr/bin/env/python3

from xml_parser import parse_xml


def populate_tables(cursor, data):
    """
    This function assumes the user is already connected to the MySQL server and inserts values
    into the SQL tables
    :param cursor: MySQL.connector cursor object
    :param data: Data structure(s) containing the parsed XML data
    """
    # iterate through protein_list
    for metadata in data[0]:
        command = (
            "INSERT INTO Proteins"
            "(accession, version, creation_date, update_date, protein_name, protein_type, gene_name)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )

        cursor.execute(command, (
            metadata[0],
            metadata[1],
            metadata[2],
            metadata[3],
            metadata[4],
            metadata[5],
            metadata[6],
        ))

    # iterate through bio_func_list
    for func in data[1]:
        command = (
            "INSERT INTO Biological_Functions (accession, general_function, specific_function)"
            "VALUES (%s, %s, %s)"
        )

        cursor.execute(command, (func[0], func[1], func[2]))

    # iterate through path_list
    for pathway in data[2]:
        command = (
            "INSERT INTO Pathways (accession, pathway_name)"
            "VALUES (%s, %s)"
        )

        cursor.execute(command, (pathway[0], pathway[1]))

    # iterate through metabolites_list
    for metabolite in data[3]:
        command = (
            "INSERT INTO Metabolites (metabolite_accession, metabolite_name, protein_accession)"
            "VALUES (%s, %s, %s)"
        )

        cursor.execute(command, (metabolite[0], metabolite[1], metabolite[2]))

    # iterate through protein_properties
    for protein_prop in data[4]:
        command = (
            "INSERT INTO Protein_Properties "
            "(accession, residue_number, molecular_weight, theoretical_pi, polypeptide_sequence)"
            "VALUES (%s, %s, %s, %s, %s)"
        )

        cursor.execute(command, (protein_prop[0], protein_prop[1], protein_prop[2], protein_prop[3], protein_prop[4]))

    # iterate through gene_properties
    for gene_prop in data[5]:
        command = (
            "INSERT INTO Gene_Properties (accession, chromosome_location, locus, gene_sequence)"
            "VALUES (%s, %s, %s, %s)"
        )

        cursor.execute(command, (gene_prop[0], gene_prop[1], gene_prop[2], gene_prop[3]))

    # iterate through go_class_list
    for classification in data[6]:
        command = (
            "INSERT INTO Go_Classifications (accession, category, description, go_id)"
            "VALUES (%s, %s, %s, %s)"
        )

        cursor.execute(command, (classification[0], classification[1], classification[2], classification[3]))

    # iterate through extra_info_list
    for info in data[7]:
        command = (
            "INSERT INTO Additional_Info (accession, genbank_protein_id, uniprot_id)"
            "VALUES (%s, %s, %s)"
        )

        cursor.execute(command, (info[0], info[1], info[2]))

    # iterate through references_list
    for ref in data[8]:
        command = (
            "INSERT INTO Literature_References (accession, reference_text)"
            "VALUES (%s, %s)"
        )

        cursor.execute(command, (ref[0], ref[1]))