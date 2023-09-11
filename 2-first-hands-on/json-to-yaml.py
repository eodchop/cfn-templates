#usage prints to standard out by default
#use bash redirection to pipe to an output file "python3 json-to-yaml.py > output_file.yaml"
import json
import yaml
file=open("0-exercise.json","r")
python_dict=json.load(file)
yaml_string=yaml.dump(python_dict)
#uncomment to send to std out, but using > to write to file_name.yaml
#print(yaml_string)
