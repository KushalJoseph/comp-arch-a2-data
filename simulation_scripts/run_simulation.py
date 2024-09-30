import os
import subprocess

BASE_DIR = "cache_configs"
FOLDERS = ["ass", "size"]

def ensure_output_folder_exists(folder):
    output_dir = os.path.join(folder, "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def get_input_files(folder):
    input_dir = os.path.join(BASE_DIR, folder)
    return [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

def run_cacti_on_file(input_file, input_folder, output_folder):
    input_path = os.path.join(input_folder, input_file)
    output_path = os.path.join(output_folder, input_file)

    command = f"cacti -infile {input_path} > {output_path}"
    subprocess.run(command, shell=True)

def process_folder(folder):
    input_folder = os.path.join(BASE_DIR, folder)
    output_folder = ensure_output_folder_exists(input_folder)
    input_files = get_input_files(folder)
    for input_file in input_files:
        print("Processing: " + str(input_file))
        run_cacti_on_file(input_file, input_folder, output_folder)
    print('\n')

def main():
    for folder in FOLDERS:
        process_folder(folder)

if __name__ == "__main__":
    main()
