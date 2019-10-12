import yaml

class globalConfig:

def readGlobalConfig:
    with open("/temp/example.yaml", 'r') as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)