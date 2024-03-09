import os
import json
import jsonschema


__configSchema = {
  "type":"object",
  "properties":{
    "OAUTH":{
      "type":"object",
      "properties":{
        "clientID":{"type":"string"},
        "clientSecret":{"type":"string"},
        "redirectURI":{"type":"string"},
      },
      "required":["clientID", "clientSecret", "redirectURI"]
    },
  },
  "required":["OAUTH"]
}

def __readConfig(path:str = os.path.join(os.getcwd(), "config.json")):
  if not os.path.exists(path):
    raise FileNotFoundError("could not locate config.json file!")

  with open(path) as f:
    d = json.load(f)
    f.close()

  try:
    jsonschema.validate(d,__configSchema)
  except jsonschema.ValidationError as e:
    e.message = "Invalid config.json file!\n" + e.message
    raise e

  return d


config = __readConfig()


