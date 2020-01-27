import json
import yaml

with open('input.json') as js:
    data = json.load(js)

with open('output.yaml', 'w') as yml:
    yaml.dump(data, yml, default_flow_style=False, allow_unicode=True)

with open('input.yml') as yml:
    data = yaml.load(yml)

with open('output.json', 'w') as js:
    js.write(json.dumps(data))
