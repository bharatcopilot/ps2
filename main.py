# Create a function that generate accurate swagger documentation from a .har file
import json
harfile = "home/bharat/Music/har_files/test.har"


def generate_swagger_from_har(har_file):
    har_data = har_to_dict(har_file)
    swagger_data = generate_swagger_from_har_data(har_data)
    print(swagger_data)
    return swagger_data

# create a function har_to_dict that converts a har file to a dictionary
def har_to_dict(har_file):
    with open(har_file, 'r') as f:
        har_data = json.load(f)
    return har_data

#create a function generate_swagger_from_har_data that converts a har file to a swagger file
def generate_swagger_from_har_data(har_data):
    swagger_data = {}
    swagger_data['swagger'] = '2.0'
    swagger_data['info'] = {}
    swagger_data['info']['version'] = '1.0'
    swagger_data['info']['title'] = 'Swagger API'
    swagger_data['info']['description'] = 'Swagger API'
    swagger_data['paths'] = {}
    for entry in har_data['log']['entries']:
        path = entry['request']['url']
        method = entry['request']['method']
        if path not in swagger_data['paths']:
            swagger_data['paths'][path] = {}
        swagger_data['paths'][path][method] = {}
        swagger_data['paths'][path][method]['tags'] = ['api']
        swagger_data['paths'][path][method]['summary'] = 'API'
        swagger_data['paths'][path][method]['description'] = 'API'
        swagger_data['paths'][path][method]['parameters'] = []
        swagger_data['paths'][path][method]['responses'] = {}
