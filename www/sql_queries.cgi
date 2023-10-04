#!/usr/bin/python3


import cgi
import json
import os
import mysql.connector


def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    sql_table = form.getvalue('sql_table')
    accession = form.getvalue('accession')

    # connecting to MySQL server
    conn = mysql.connector.connect(user='root', password='***', host='localhost', database='hmdb')
    cursor = conn.cursor()

    # --- SQL QUERIES --- #
    if sql_table == 'Biological_Functions':
        qry = """
        SELECT general_function, specific_function
        FROM Proteins
        Join Biological_Functions on Proteins.accession=Biological_Functions.accession
        WHERE Proteins.accession=%s
        """

    elif sql_table == "Protein_Properties":
        qry = """
        SELECT residue_number, molecular_weight, theoretical_pi, polypeptide_sequence
        FROM Proteins
        JOIN Protein_Properties on Proteins.accession=Protein_Properties.accession
        WHERE Proteins.accession=%s;
        """

    elif sql_table == "Gene_Properties":
        qry = """
        SELECT chromosome_location, locus, gene_sequence
        FROM Proteins
        JOIN Gene_Properties on Proteins.accession=Gene_Properties.accession
        WHERE Proteins.accession=%s
        """

    elif sql_table == "Pathways":
        qry = """
        SELECT pathway_name
        FROM Proteins
        JOIN Pathways on Proteins.accession=Pathways.accession
        WHERE Proteins.accession=%s
        """

    elif sql_table == "Metabolites":
        qry = """
        SELECT metabolite_accession, metabolite_name
        FROM Proteins
        JOIN Metabolites on Proteins.accession = Metabolites.protein_accession
        WHERE Proteins.accession=%s
        """

    elif sql_table == "Go_Classifications":
        qry = """
        SELECT category, description, go_id
        FROM Proteins
        JOIN Go_Classifications on Proteins.accession=Go_Classifications.accession
        WHERE Proteins.accession=%s
        """

    elif sql_table == "Additional_Info":
        qry = """
        SELECT genbank_protein_id, uniprot_id
        FROM Proteins
        JOIN Additional_Info on Proteins.accession=Additional_Info.accession
        WHERE Proteins.accession=%s
        """

    elif sql_table == "Literature_References":
        qry = """
        SELECT reference_text
        FROM Proteins
        JOIN Literature_References on Proteins.accession=Literature_References.accession
        WHERE Proteins.accession=%s
        """

    # --- END OF SQL QUERIES --- #

    # execute the query
    cursor.execute(qry, (accession, ))

    # initialize JSON object
    results = {'match_count': 0, 'matches': list()}

    # --- ITERATE THROUGH DIFFERENT QUERIES --- #
    if sql_table == "Biological_Functions":
        for (general_function, specific_function) in cursor:
            results['matches'].append({
                'general_function': general_function,
                'specific_function': specific_function
            })
        results['match_count'] += 1

    if sql_table == "Protein_Properties":
        for (residue_number, molecular_weight, theoretical_pi, polypeptide_sequence) in cursor:
            results['matches'].append({
                'residue_number': residue_number,
                'molecular_weight': molecular_weight,
                'theoretical_pi': theoretical_pi,
                'polypeptide_sequence': polypeptide_sequence
            })

    if sql_table == "Gene_Properties":
        for ( chromosome_location, locus, gene_sequence) in cursor:
            results['matches'].append({
                'chromosome_location': chromosome_location,
                'locus': locus,
                'gene_sequence': gene_sequence
            })

    if sql_table == "Pathways":
        for (pathway_name,) in cursor:
            results['matches'].append({
                'pathway_name': pathway_name
            })

    if sql_table == "Metabolites":
        for (metabolite_accession, metabolite_name) in cursor:
            results['matches'].append({
                'metabolite_accession': metabolite_accession,
                'metabolite_name': metabolite_name
            })

    if sql_table == "Go_Classifications":
        for (category, description, go_id) in cursor:
            results['matches'].append({
                'category': category,
                'description': description,
                'go_id': go_id
            })

    if sql_table == "Additional_Info":
        for (genbank_protein_id, uniprot_id) in cursor:
            results['matches'].append({
                'genbank_protein_id': genbank_protein_id,
                'uniprot_id': uniprot_id
            })

    if sql_table == "Literature_References":
        for (reference_text,) in cursor:
            results['matches'].append({
                'reference_text': reference_text
            })

    # --- END OF ITERATIONS --- #

    conn.close()

    try:
        print(json.dumps(results))

    except mysql.connector.Error as error:
        print(json.dumps({"error": "MySQL error: {}".format(error)}))


if __name__ == '__main__':
    main()
