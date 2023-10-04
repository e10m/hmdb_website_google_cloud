import cgi
import json
import os
import mysql.connector


def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()

    search_value = form.getvalue('search_term')

    # connecting to MySQL server
    conn = mysql.connector.connect(user='root', password='***', host='localhost', database='hmdb')
    cursor = conn.cursor()

    # initialize the initial query
    qry = """
    SELECT *
    FROM Proteins
    WHERE protein_name LIKE %s
    OR accession LIKE %s
    OR version LIKE %s
    OR creation_date LIKE %s
    OR update_date LIKE %s
    OR gene_name LIKE %s
    """

    new_search_value = "%" + search_value + "%"  # add wildcards
    cursor.execute(qry, (new_search_value, new_search_value, new_search_value, new_search_value, new_search_value,
                         new_search_value, ))

    # initialize JSON object
    results = {'match_count': 0, 'matches': list()}

    for (accession, version, creation_date, update_date, protein_name, protein_type, gene_name) in cursor:
        results['matches'].append({
            'accession': accession,
            'version': version,
            'creation_date': creation_date,
            'update_date': update_date,
            'protein_name': protein_name,
            'protein_type': protein_type,
            'gene_name': gene_name
        })
        results['match_count'] += 1

    conn.close()

    try:
        print(json.dumps(results))

    except mysql.connector.Error as error:
        print(json.dumps({"error": "MySQL error: {}".format(error)}))


if __name__ == '__main__':
    main()
