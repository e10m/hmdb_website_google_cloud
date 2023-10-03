#!/usr/bin/env/python3

import cgi
import mysql.connector
import json
from table_creater import create_table
from xml_parser import parse_xml
from table_populator import populate_tables


def main():
    # connect to database
    conn = mysql.connector.connect(user='root', password='***', host='localhost', database='hmdb')
    cursor = conn.cursor()

    # parse hard coded XML file
    file_path = '/home/ethanmach1998/hmdb_proteins.xml'
    protein_data = parse_xml(file_path)

    # create tables
    create_table(cursor)

    # populate tables
    populate_tables(cursor, protein_data)

    # commit changes
    conn.commit()

    # close database
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
