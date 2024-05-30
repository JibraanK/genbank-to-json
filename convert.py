from Bio import SeqIO
import json

def genbank_to_json(genbank_file, json_file):
    with open(genbank_file, "r") as gb_file:
        record = SeqIO.read(gb_file, "genbank")
        
        # Convert SeqRecord to dictionary
        record_dict = {
            "name": record.name,
            "sequence": str(record.seq),
            "features": []
        }

        for feature in record.features:
            feature_dict = {
                "name": feature.qualifiers.get("label", [""])[0],
                "start": int(feature.location.start),
                "stop": int(feature.location.end),
                "legend": feature.type,
                "source": "json-feature",
                "visible": True,
                "strand": feature.location.strand,
                "tags": feature.qualifiers.get("label", [""])[0]
            }
            record_dict["features"].append(feature_dict)

        # Write to JSON file
        with open(json_file, "w") as j_file:
            json.dump(record_dict, j_file, indent=4)

# Path to the input and output files
genbank_file = "/Users/jibk/Desktop/gbk to json/gbk std.gb"  # Replace with the actual path to your .gb file
json_file = "/Users/jibk/Desktop/gbk to json/plasmid.json"   # Replace with the desired output path for the JSON file

# Convert GenBank to JSON
genbank_to_json(genbank_file, json_file)
