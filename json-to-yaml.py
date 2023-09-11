#by default, in a POSIX compliance env, this script will output the formatted file to std out
#use a bash redirection to pipe it to a file. "python3 json-to-yaml.py > output.yaml"
import jason
import yaml
file=open("file.json","r")
python_dict=json.load(file)
yaml_string=yaml.dump(python_dict)
#uncomment the following line to print to std out. 
#print("The YAML file is: " + yaml_string)

