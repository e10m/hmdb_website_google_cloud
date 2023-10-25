# Human Body Protein Search

> NOTE: The 'www' package and README.md is written by Dien Mach (dmach1).

## About:
This is a web-based search engine for obtaining information about specific proteins or enzymes
found within the human body. The website was based off the Human Metabolite Database (HMDB) website in an attempt to 
create a more modern, streamlined, and minimal page for fast information regarding proteins. The source data was obtained from the HMDB which was parsed
using Python, uploaded to a MySQL database, then made accessible to users via JavaScript / HTML / CSS.

This README will instruct users how to use and navigate the website.

This document is written in Markdown.

## Storage and Access
* The live code and protein SQL database is deployed on a Google Cloud instance which can be accessed at http://34.94.137.66/
    * **NOTE**: The URL is http access only, not https

The project directory can be found at:
* https://github.com/e10m/hmdb_website_google_cloud

## Recommended Browsers
* Google Chrome, Firefox, Edge, Safari, and Opera are all recommended browsers
  * The website uses the jQuery API which are best supported by browsers such as Google Chrome 54+, Microsoft Edge 17+, Safari 10+, Firefox 49+, Opera 41+
    * As of 8/13/23 from https://caniuse.com/

* NOTE: Internet Explorer is not supported by this tool

## Main Usage:
1. Input the [URL](http://34.94.137.66/) into your browser
   * **NOTE**: The server is hosted from Monday to Friday 5 AM - 5 PM PST
2. Search for a protein
   * eg: 
     * Glucokinase (protein)
     * HMDBP10676 (HMDB accession number)
     * SRY (gene name)
3. Select the desired protein from the resulting (if any) table that appears
4. Select a category (usually on the left) by clicking on the blue buttons for more specific categorical information about the protein
    * eg:
      * Biological Functions, Literature

## Citations:
For more information about the original database, please visit the [HMDB website](https://hmdb.ca/).
1. Wishart DS, Tzur D, Knox C, et al., HMDB: the Human Metabolome Database. Nucleic Acids Res. 2007 Jan;35(Database issue):D521-6. 17202168
2. Wishart DS, Knox C, Guo AC, et al., HMDB: a knowledgebase for the human metabolome. Nucleic Acids Res. 2009 37(Database issue):D603-610. 18953024
3. Wishart DS, Jewison T, Guo AC, Wilson M, Knox C, et al., HMDB 3.0 — The Human Metabolome Database in 2013. Nucleic Acids Res. 2013. Jan 1;41(D1):D801-7. 23161693
4. Wishart DS, Feunang YD, Marcu A, Guo AC, Liang K, et al., HMDB 4.0 — The Human Metabolome Database for 2018. Nucleic Acids Res. 2018. Jan 4;46(D1):D608-17. 29140435
5. Wishart DS, Guo AC, Oler E, et al., HMDB 5.0: the Human Metabolome Database for 2022. Nucleic Acids Res. 2022. Jan 7;50(D1):D622–31. 34986597

## Author:
**Dien "Ethan" Mach (dmach1)**

* Please feel free to contact me at dmach1@jh.edu for more information regarding the website.
