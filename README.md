# gene_seeker
Gene Seeker is a Python script for identifying and extracting gene subsets from gene expression datasets based on predefined biological categories using regular expression matching.

The script searches gene names and groups them into functional categories. Results are exported into a multi-sheet Excel file for further analysis.


  Input Requirements
  Your dataset must be in .xlsx or .csv format and contain a specific column (in the first row) named exactly: 'Gene'. You can change the name to your preferences

* (line 8) file_path = r"input path" - paste between quotes the path to your file (format should be like in the example)
Important: be sure that the first row of your file has "Gene" - name of the columns. In case your column of interest has a different name, you can change this line: gene_column = "Gene" by pasting the name of your column between quotes
Important: file should have comma delimited format (csv)


* gene_categories (line 34)
adjust here the name of the group and particular genes/proteins you are looking for.

Important: between quotes you can find ^ and $ to limit the string you are searching: ^eif - means string should start with exactly "eif"; eif$ - means string should end with exactly "eif"

* line 66 output path - paste path between r" " where the output file should be saved 
