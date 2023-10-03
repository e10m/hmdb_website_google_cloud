#!/usr/bin/env/python3

import lxml.etree as ET


def parse_xml(file_path):
    """
    This function takes an XML file and parses it into numerous lists

    :param file_path: The pathway to a file
        eg: ./hmdb_proteins.xml
    :return: tuple containing lists
    (protein_list, bio_func_list, path_list, metabolites_list,
        protein_properties, gene_properties, go_class_list, extra_info_list, references_list)
    """
    with open(file_path, "rb") as file:
        # parse file via lxml library and get the root object
        tree = ET.parse(file)
        root = tree.getroot()

        # variable to save namespace
        # referenced https://lxml.de/3.2/tutorial.html#namespaces
        namespace = {'hmdb': 'http://www.hmdb.ca'}

        # initialize empty lists for each SQL table
        protein_list = []
        bio_func_list = []
        path_list = []
        metabolites_list = []
        protein_properties = []
        gene_properties = []
        go_class_list = []
        extra_info_list = []
        references_list = []

        for protein in root.findall('hmdb:protein', namespace):
            protein_accession = protein.find('hmdb:accession', namespace).text

            # parsing for proteins table
            protein_list.append((
                protein_accession,
                protein.find('hmdb:version', namespace).text,
                protein.find('hmdb:creation_date', namespace).text,
                protein.find('hmdb:update_date', namespace).text,
                protein.find('hmdb:name', namespace).text,
                protein.find('hmdb:protein_type', namespace).text,
                protein.find('hmdb:gene_name', namespace).text))

            # parsing for biological functions table
            bio_func_list.append((
                protein_accession,
                protein.find('hmdb:general_function', namespace).text,
                protein.find('hmdb:specific_function', namespace).text
            ))

            # parsing for pathways table:
            for pathway in protein.findall('hmdb:pathways/hmdb:pathway', namespace):
                pathway_name = pathway.find('hmdb:name', namespace).text
                path_list.append([protein_accession, pathway_name])

            # parsing for metabolites table:
            for metabolite in protein.findall('hmdb:metabolite_associations/hmdb:metabolite', namespace):
                metabolites_list.append([
                     metabolite.find('hmdb:accession', namespace).text,
                     metabolite.find('hmdb:name', namespace).text,
                     protein_accession
                     ])

            # parsing for classifications table
            for go_class in protein.findall('hmdb:go_classifications/hmdb:go_class', namespace):
                go_class_list.append([
                    protein_accession,
                    go_class.find('hmdb:category', namespace).text,
                    go_class.find('hmdb:description', namespace).text,
                    go_class.find('hmdb:go_id', namespace).text
                ])

            # parsing for gene properties table
            for property in protein.findall('hmdb:gene_properties', namespace):
                gene_properties.append([
                    protein_accession,
                    property.find('hmdb:chromosome_location', namespace).text,
                    property.find('hmdb:locus', namespace).text,
                    property.find('hmdb:gene_sequence', namespace).text
                ])

            # parsing for protein properties table
            for prop in protein.findall('hmdb:protein_properties', namespace):
                protein_properties.append([
                    protein_accession,
                    prop.find('hmdb:residue_number', namespace).text,
                    prop.find('hmdb:molecular_weight', namespace).text,
                    prop.find('hmdb:theoretical_pi', namespace).text,
                    prop.find('hmdb:polypeptide_sequence', namespace).text
                ])

            # parsing additional_info table
            extra_info_list.append([
                protein_accession,
                protein.find('hmdb:genbank_protein_id', namespace).text,
                protein.find('hmdb:uniprot_id', namespace).text,
            ])

            # parsing for reference table
            for reference in protein.findall('hmdb:general_references/hmdb:reference', namespace):
                references_list.append([
                    protein_accession,
                    reference.find('hmdb:reference_text', namespace).text
                ])

        return protein_list, bio_func_list, path_list, metabolites_list, protein_properties, gene_properties, \
            go_class_list, extra_info_list, references_list


if __name__ == "__main__":
    windows_path = "C:\\Users\\Ethan Mach\\Desktop\\final_source_data\\hmdb_proteins.xml"
    unix_path = "/Users/ethanmach/Downloads/hmdb_proteins.xml"
    parse_xml(unix_path)