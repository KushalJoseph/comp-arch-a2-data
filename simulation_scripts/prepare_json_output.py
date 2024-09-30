import os
import json

BASE_DIR = "cache_configs"
FOLDERS = ["ass", "size"]

LINES_OF_INTEREST = [
    "Cache size",
    "Associativity",
    "Access time (ns)",
    "Total dynamic read energy per access (nJ)",
    "Data array: Area (mm2)"
]

def extract_value_from_line(line):
    try:
        value = line.split(":")[-1].strip()
        return float(value)
    except ValueError:
        return None

def parse_output_file(file_path):
    global_map = {}

    with open(file_path, 'r') as file:
        for line in file:
            for phrase in LINES_OF_INTEREST:
                if phrase in line:
                    value = extract_value_from_line(line)
                    if value is not None:
                        global_map[phrase] = value

    return global_map

def write_json(output_data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)
    print(f"JSON file created: {output_file}")

def process_folder(folder):
    output_folder = os.path.join(BASE_DIR, folder, "output")

    if not os.path.exists(output_folder):
        print(f"ERROR: Output folder not found: {output_folder}")
        return

    output_files = [f for f in os.listdir(output_folder)]

    for output_file in output_files:
        output_file_path = os.path.join(output_folder, output_file)
        data = parse_output_file(output_file_path)
        json_file_path = os.path.join(output_folder, os.path.splitext(output_file)[0] + ".json")
        write_json(data, json_file_path)

def main():
    for folder in FOLDERS:
        process_folder(folder)

if __name__ == "__main__":
    main()
