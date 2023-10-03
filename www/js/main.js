import { runSearch, processJSON, first_search } from "./search_functions.js";
import { perform_queries, create_second_table } from "./table_functions.js";


// actions for when page is ready
$(document).ready(function() {
    // main search function
    $('#main_submit').click(function () {
        runSearch('#protein_search');
        return false;
    })

    // post search function
    $('#post_submit').click(function () {
        runSearch('#subheader_search_form')

        if ( $('#initial_table').css('display') === 'none' ) {
            $('#match_count').css('opacity', '1');
            $('#initial_table').toggle();
            $('#protein_info_buttons').toggle();
            $('#second_table').toggle();
            $('#last_page_table_container').toggle();
            $('.protein_info_container').hide();
            $('#prot_info_body td').removeClass('active');
        }

        return false;

    })

    // pressing back button, return to front page without refreshing
    $('#back_button').click( function () {
        if ( $('#second_table').css('display') === 'none' ) {
            first_search()
        }

        if ( $('#initial_table').css('display') === 'none' ) {
            $('#match_count').css('opacity', '1');
            $('#initial_table').toggle();
            $('#protein_info_buttons').toggle();
            $('#second_table').toggle();
            $('#last_page_table_container').toggle();
            $('.protein_info_container').hide();
            $('#prot_info_body td').removeClass('active');
        }

    })

    // click protein info buttons
    $('#prot_info_body tr').click( function () {
        // send proper SQL table name to perform_queries( sql_table_name )
        if ($(this).is('#prot_info_body tr:nth-child(1)')) {
            var sql_table_name = "Biological_Functions"
        }
        if ($(this).is('#prot_info_body tr:nth-child(2)')) {
            var sql_table_name = "Protein_Properties"
        }
        if ($(this).is('#prot_info_body tr:nth-child(3)')) {
            var sql_table_name = "Gene_Properties"
        }
        if ($(this).is('#prot_info_body tr:nth-child(4)')) {
            var sql_table_name = "Pathways"
        }
        if ($(this).is('#prot_info_body tr:nth-child(5)')) {
            var sql_table_name = "Metabolites"
        }
        if ($(this).is('#prot_info_body tr:nth-child(6)')) {
            var sql_table_name = "Go_Classifications"
        }
        if ($(this).is('#prot_info_body tr:nth-child(7)')) {
            var sql_table_name = "Additional_Info"
        }
        if ($(this).is('#prot_info_body tr:nth-child(8)')) {
            var sql_table_name = "Literature_References"
        }

        // toggle opacity
        let this_row = $(this).find('td');

        if ( this_row.hasClass('active') ) {
            // disable opacity (bring back to 60%)
            this_row.removeClass('active');

            // hide tables
            $('.protein_info_container').hide();


        } else {
            // reset and enable opacities
            $('#prot_info_body td').removeClass('active');
            $(this).find('td').addClass('active');

            // show tables
            perform_queries(sql_table_name)
            $('.protein_info_container').show();

        }
    })
})