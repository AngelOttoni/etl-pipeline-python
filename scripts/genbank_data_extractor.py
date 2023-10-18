from Bio import SeqIO
import pandas as pd


def extract_product_values(record):
# Initialize an empty list to store product values
    product_values = []
    
# Loop through features in the record
    for feature in record.features:
        if feature.type in ['misc_RNA', 'rRNA', 'mRNA']:
            # Access qualifiers for the current feature
            qualifiers = feature.qualifiers
            if 'product' in qualifiers:
                # Extend the product_values list with product values
                product_values.extend(qualifiers['product'])
            if 'note' in qualifiers:
                # Extend the product_values list with note values
                product_values.extend(qualifiers['note'])

# Join the product values into a comma-separated string or set to "None" if empty
    return ", ".join(product_values) if product_values else "None"


def extract_sequence_data(record):
# Extract product values using the extract_product_values function
    product = extract_product_values(record)

# Extracts information from a GenBank record and returns it as a dictionary
    sequence_data = {
        "molecule_type": record.features[0].qualifiers.get('mol_type')[0],
        "dna_region": product,
        "accession": record.id,
        "organism_name": record.features[0].qualifiers.get('organism')[0],
        "voucher": record.features[0].qualifiers.get('specimen_voucher', ["Undefined"])[0],
        "country": record.features[0].qualifiers.get('country', ["Undefined"])[0],
        "type_material": record.features[0].qualifiers.get("type_material", ["Undefined"])[0],
        "isolate": record.features[0].qualifiers.get('isolate', ["Undefined"])[0],
        "strain": record.features[0].qualifiers.get('strain', ["Undefined"])[0],
        "isolation_src": record.features[0].qualifiers.get('isolation_source', ["Undefined"])[0],
        "host": record.features[0].qualifiers.get('host', ["Unknown"])[0],
        "collection_date": record.features[0].qualifiers.get('collection_date', ["Undefined"])[0],
        "collected_by": record.features[0].qualifiers.get('collected_by', ["Undefined"])[0],
        "identified_by": record.features[0].qualifiers.get('identified_by', ["Undefined"])[0],
        "taxid": "",
        "title": "",
        "authors": "",
        "journal": "",
        "defline": record.description,
        "length": len(record.seq),
        "sequence": str(record.seq),
    }
    
# Check for references and add them to the dictionary
    if references := record.annotations.get("references", []):
        sequence_data["title"] = references[0].title
        sequence_data["journal"] = references[0].journal
        sequence_data["authors"] = ", ".join(ref.authors for ref in references)

# Extract the taxid from the source feature
    for feature in record.features:
        if feature.type == "source":
            qualifiers = feature.qualifiers
            if "db_xref" in qualifiers:
                for dbxref in qualifiers["db_xref"]:
                    if dbxref.startswith("taxon:"):
                        sequence_data["taxid"] = dbxref.split(":")[1]
    return sequence_data


def main(input_genbank_file, output_csv_file):
    # Extracts data from a GenBank file and saves it as a CSV file
    sequences_data = []

    for record in SeqIO.parse(input_genbank_file, "genbank"):
        sequence_data = extract_sequence_data(record)
        sequences_data.append(sequence_data)
        
# Create a DataFrame and save it as a CSV file
    df = pd.DataFrame(sequences_data)
    df.to_csv(output_csv_file, index=False)
    print(
        f"Your data has been successfully saved as a CSV file: {output_csv_file}")


if __name__ == "__main__":
    input_genbank_file = "/home/angel-ottoni/Documents/etl-python/src/all-seqs-lachnocladium-jun-13-23.gb"
    output_csv_file = "/home/angel-ottoni/Documents/etl-python/data/output_info1.csv"
    main(input_genbank_file, output_csv_file)
