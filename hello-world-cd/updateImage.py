import yaml
import sys

fname = "values.yaml"

stream = open(fname, 'r')
data = yaml.load(stream,Loader=yaml.SafeLoader)

#data['image'] = 'lakshitsainiceligo/qa:HelloWorld_1.0.0.13.0'
newVersion = sys.argv[1]
data['image'] = newVersion

with open(fname, 'w') as yaml_file:
    yaml_file.write( yaml.dump(data, default_flow_style=False))
