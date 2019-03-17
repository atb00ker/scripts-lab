import json
import yaml

# with open('netjson.json') as js:
#     data = json.load(js)

# with open('test.yaml', 'w') as yml:
#     yaml.dump(data, yml, default_flow_style=False, allow_unicode=True)

with open('netjson.yml') as yml:
    data = yaml.load(yml)

with open('test.json', 'w') as js:
    js.write(json.dumps(data))
