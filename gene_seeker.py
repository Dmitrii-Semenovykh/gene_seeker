import pandas as pd
import os


# Loading excel/csv files
file_path = r"input path"  # Paste a path in the file explorer to your file

# Make sure you installed openpyxl to open xlsx
if file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path, engine="openpyxl")
elif file_path.endswith(".csv"):
    df = pd.read_csv(file_path, encoding='utf-8-sig')
else:
    raise ValueError("Unsupported file type")

# Clean column names
df.columns = [c.strip() for c in df.columns]

print("Columns detected:", df.columns.tolist())

# Check the existence of the "Gene" column in the file. You can change it based on your needs.

gene_column = "Gene"  # be sure the column with list of genes has exactly this name

if gene_column not in df.columns:
    raise ValueError(f"{gene_column} column not found. Check column names.")

df[gene_column] = df[gene_column].astype(str)

# Define the category and exact genes we are looking for (like here in the example)

gene_categories = {
    "elongation_factors": [
        r"^eef2$", r"^eef2k$", r"^eef1", r"^eif"
    ],

    "ribosomal_proteins": [
        r"^rpl", r"^rps"
    ],

    "calcium_signaling": [
        r"itpr", r"atp2a", r"mcu", r"calm", r"camk", r"ryr"
    ],

    "phosphatases": [
        r"ppp1", r"ppp2", r"ppm"
    ]
}


# Searching genes

def find_genes_by_category(df, gene_column, patterns):
    mask = df[gene_column].str.lower().str.contains(
        "|".join(patterns),
        regex=True,
        na=False
    )
    return df[mask]


# Extract genes per category
results = {}

output_path = r"output path"
with pd.ExcelWriter(output_path) as writer:
    for category, patterns in gene_categories.items():
        matches = find_genes_by_category(df, gene_column, patterns)
        results[category] = matches

        print(f"\n=== {category.upper()} ===")
        print(f"Found {len(matches)} genes")

        if len(matches) > 0:
            matches.to_excel(writer, sheet_name=category, index=False)

print("All results were succesfully saved")

