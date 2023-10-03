export function create_second_table(data) {
    /*
    This function receives and saves information about the single protein selected, then creates the
    second table containing a single row about the selected protein.

    :input data: The selected protein's metadata
    */
    $('#second_body').empty();

    // create row and assign id #
    $('<tr/>', { "id" : "secondTable_row_1" } ).appendTo('#second_body');
    $('<tr/>', { "id" : "secondTable_row_2" } ).appendTo('#second_body');
    $('<tr/>', { "id" : "secondTable_row_3" } ).appendTo('#second_body');
    $('<tr/>', { "id" : "secondTable_row_4" } ).appendTo('#second_body');
    $('<tr/>', { "id" : "secondTable_row_5" } ).appendTo('#second_body');
    $('<tr/>', { "id" : "secondTable_row_6" } ).appendTo('#second_body');
    $('<tr/>', { "id" : "secondTable_row_7" } ).appendTo('#second_body');

    // create columns
    $('<td/>', { "text" : "Name" } ).appendTo('#secondTable_row_1');
    $('<td/>', { "text" : "Gene Name" } ).appendTo('#secondTable_row_2');
    $('<td/>', { "text" : "Type" } ).appendTo('#secondTable_row_3');
    $('<td/>', { "text" : "Accession" } ).appendTo('#secondTable_row_4');
    $('<td/>', { "text" : "Version" } ).appendTo('#secondTable_row_5');
    $('<td/>', { "text" : "Creation Date" } ).appendTo('#secondTable_row_6');
    $('<td/>', { "text" : "Last Modified" } ).appendTo('#secondTable_row_7');

    $('<td/>', { "text" : data.protein_name } ).appendTo('#secondTable_row_1');
    $('<td/>', { "text" : data.gene_name } ).appendTo('#secondTable_row_2');
    $('<td/>', { "text" : data.protein_type } ).appendTo('#secondTable_row_3');
    $('<td/>', { "text" : data.accession } ).appendTo('#secondTable_row_4');
    $('<td/>', { "text" : data.version } ).appendTo('#secondTable_row_5');
    $('<td/>', { "text" : data.creation_date } ).appendTo('#secondTable_row_6');
    $('<td/>', { "text" : data.update_date } ).appendTo('#secondTable_row_7');
}

export function perform_queries( sql_table ) {
    /*
    This function saves information about the single protein selected from the initial table, then sends
    the information to a CGI script via AJAX call which performs SQL queries.
     */

    // info to be sent to CGI script (sql table name and accession number)
    var clicked_accession = $('#secondTable_row_4 td:nth-child(2)').text();

    // sends information to CGI script
    $.ajax({
            url: '../sql_queries.cgi',
            method: 'POST',
            data: {'sql_table': sql_table, 'accession': clicked_accession},
            dataType: 'json',
            success: function (data) {
                // empty table
                $('#protein_info_table thead tr').empty();
                $('#protein_info_table tbody').empty();

                // hide or show table
                if ($("#protein_info_container").is(':visible')) {
                    $('#protein_info_container').hide();
                } else {
                    $("#protein_info_container").show();
                }

                console.log(data)

                let row_count = 1

                // iterate over each match and add a row to the result table for each
                $.each(data.matches, function (i, item) {
                    var this_row_id = 'info_row_' + row_count++;

                    // create row and assign id
                    $('<tr id=' + this_row_id + '></tr>').appendTo('#protein_info_table tbody')

                    // --- create table columns based on which button clicked --- //
                    if (sql_table === "Biological_Functions") {
                        if (i === 0) {
                            $('<td>General Function</td>').appendTo('#protein_info_table thead tr')
                            $('<td>Specific Function</td>').appendTo('#protein_info_table thead tr')
                        }
                        $('<td/>', {"text": item.general_function}).appendTo('#' + this_row_id)
                        $('<td/>', {"text": item.specific_function}).appendTo('#' + this_row_id)
                    }
                    if (sql_table === "Protein_Properties") {
                        if (i === 0) {
                            $('<td>Residue Number</td>').appendTo('#protein_info_table thead tr')
                            $('<td>Molecular Weight</td>').appendTo('#protein_info_table thead tr')
                            $('<td>Theoretical Isoelectric Point (pI)</td>').appendTo('#protein_info_table thead tr')
                            $('<td>Polypeptide Sequence</td>').appendTo('#protein_info_table thead tr')
                        }
                        $('<td/>', {"text": item.residue_number}).appendTo('#' + this_row_id)
                        $('<td/>', {"text": item.molecular_weight}).appendTo('#' + this_row_id)
                        $('<td/>', {"text": item.theoretical_pi}).appendTo('#' + this_row_id)
                        $('<td/>', {"text": item.polypeptide_sequence}).appendTo('#' + this_row_id)
                    }
                    if (sql_table === "Gene_Properties") {
                        if (i === 0) {
                            $('<td>Chromosome Location</td>').appendTo('#protein_info_table thead tr')
                            $('<td>Locus</td>').appendTo('#protein_info_table thead tr')
                            $('<td>Gene Sequence</td>').appendTo('#protein_info_table thead tr')
                        }
                        $('<td/>', {"text": item.chromosome_location}).appendTo('#' + this_row_id)
                        $('<td/>', {"text": item.locus}).appendTo('#' + this_row_id)
                        $('<td/>', {"text": item.gene_sequence}).appendTo('#' + this_row_id)
                    }
                    if (sql_table === "Metabolites") {
                        if (i === 0) {
                            $('<td>Metabolite Accession #</td>').appendTo('#protein_info_table thead tr')
                            $('<td>Name</td>').appendTo('#protein_info_table thead tr')
                        }
                        $('<td/>', {"text": item.metabolite_accession}).appendTo('#' + this_row_id)
                        $('<td/>', {"text": item.metabolite_name}).appendTo('#' + this_row_id)
                    }
                    if (sql_table === "Pathways") {
                        if (i === 0) {
                            $('<td>Pathway</td>').appendTo('#protein_info_table thead tr')
                        }
                        $('<td/>', {"text": item.pathway_name}).appendTo('#' + this_row_id)
                    }
                    if (sql_table === "Go_Classifications") {
                        if (i === 0) {
                            $('<td>Category</td>').appendTo('#protein_info_table thead tr')
                            $('<td>Description</td>').appendTo('#protein_info_table thead tr')
                            $('<td>Go ID</td>').appendTo('#protein_info_table thead tr')
                        }
                        $('<td/>', {"text": item.category}).appendTo('#' + this_row_id)
                        $('<td/>', {"text": item.description}).appendTo('#' + this_row_id)
                        $('<td/>', {"text": item.go_id}).appendTo('#' + this_row_id)
                    }
                    if (sql_table === "Additional_Info") {
                        if (i === 0) {
                            $('<td>Genbank ID</td>').appendTo('#protein_info_table thead tr')
                            $('<td>UniProt ID</td>').appendTo('#protein_info_table thead tr')
                        }
                        $('<td/>', {"text": item.genbank_protein_id}).appendTo('#' + this_row_id)
                        $('<td/>', {"text": item.uniprot_id}).appendTo('#' + this_row_id)
                    }
                    if (sql_table === "Literature_References") {
                        if (i === 0) {
                            $('<td>Reference</td>').appendTo('#protein_info_table thead tr')
                        }
                        $('<td/>', {"text": item.reference_text}).appendTo('#' + this_row_id)
                    }
                });
            },
            error: function (jqXHR, textStatus, errorThrown) {
                alert("Failed to perform gene search! textStatus: (" + textStatus +
                    ") and errorThrown: (" + errorThrown + ")"
                );
            }
        }
    )
}