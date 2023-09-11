import json
import yaml
file=open("0-exercise.json","r")
python_dict=json.load(file)
yaml_string=yaml.dump(python_dict)
#send to std out, but using > to write to file_name.yaml
print(yaml_string)
