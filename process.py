import json

def is_valid(i):
    try:
      float(i['pricing']['eu-west-1']['linux']['ondemand'])
      float(i['ECU'])
      float(i['pricing']['eu-west-1']['linux']['reserved']['yrTerm1Convertible.allUpfront'])
      float(i['pricing']['eu-west-1']['linux']['reserved']['yrTerm3Convertible.allUpfront'])
    except:
        return False
    return i['ECU']!=0

with open('instances.json', 'r') as f:
    data = json.load(f)

for i in data:
    if is_valid(i):
        print(i['instance_type'] + "," + \
        str(float(i['pricing']['eu-west-1']['linux']['ondemand'])/i['ECU']) + "," + \
        str(float(i['pricing']['eu-west-1']['linux']['ondemand'])/i['memory']) + "," + \
        str(float(i['pricing']['eu-west-1']['linux']['ondemand'])/(float(i['pricing']['eu-west-1']['linux']['reserved']['yrTerm1Convertible.allUpfront']))) + "," + \
        str(float(i['pricing']['eu-west-1']['linux']['ondemand'])/(float(i['pricing']['eu-west-1']['linux']['reserved']['yrTerm3Convertible.allUpfront']))))