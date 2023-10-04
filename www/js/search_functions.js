import {create_second_table} from "./table_functions.js";

export function runSearch(selector) {
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $(selector).serialize();

    $.ajax({
        // todo: ../protein_search.cgi
        url: '/protein_search.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                ") and errorThrown: (" + errorThrown + ")");
            console.log(textStatus, errorThrown)
        }
    });
}


// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
export function processJSON( data ) {
    // set the span that lists the match count
    $('#match_count').text( data.match_count + " matches found." );

    // clear table
    $('#first_body').empty();

    // this will be used to keep track of row identifiers
    var next_row_num = 1;

    // iterate over each match and add a row to the result table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'initialTable_row_' + next_row_num++;

        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('#first_body');

        // add columns
        $('<td/>', { "text" : item.protein_name } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : item.gene_name } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : item.protein_type } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : item.accession } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : item.version } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : item.creation_date } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : item.update_date } ).appendTo('#' + this_row_id);

        // trigger events if clicking on the table row
        $('#' + this_row_id).click(function () {
            var saved_row_info = item;
            create_second_table(saved_row_info);

            // toggle second page
            $('#match_count').css('opacity', '0');
            $('#initial_table').toggle();
            $('#second_table').toggle();
            $('#protein_info_buttons').toggle();
            $('#last_page_table_container').toggle();
        })

    })
    if ( $('#results').css('display') === 'none' ) {
        first_search()
    }
}

export function first_search() {
    // jQuery selector actions
    $('#results').toggle();
    $('#title').toggle();
    $('#protein_search').toggle();
    $('#subheader_search_div').toggle();
    if (parseFloat($('.placeholder_div').css('opacity')) === 0) {
        $('.placeholder_div').css('opacity', '1');
    } else {
        $('.placeholder_div').css('opacity', '0');
    }

}