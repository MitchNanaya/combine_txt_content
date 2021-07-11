import sys
import pathlib
import io
import os
def get_file_names(full_path):
    return list(pathlib.Path(full_path).glob("*.txt"))

def load_file_and_write_to_output(list_file,output_file):
    write_file = open(output_file,"a", encoding="utf-8") #open file on append mode
    for file in list_file:
        read_file = open(file,"r", encoding="utf-8")
        lines = read_file.readlines()
        write_file.writelines(lines)
        read_file.close()
    write_file.close()

def main():
    args = sys.argv[1:]
    input_folder_name = args[0]
    print("You are input " + input_folder_name)
    if len(args)>1:
        output_file_name = os.path.join(args[0],args[1])
        print("You are output " + output_file_name)
    files = get_file_names(input_folder_name)
    for f in files:
        print(f)
    load_file_and_write_to_output(files,output_file_name)

if __name__ == "__main__":
    main() 
