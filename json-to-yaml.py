import jason
import yaml
file=open("file.json","r")
python_dict=json.load(file)
yaml_string=yaml.dump(python_dict)
print("The YAML file is: " + yaml_string)

