import json

"""
  Import configuration from file, and expose it to python modules. 
"""

with open('config.json', 'r') as f:
    loaded = json.load(f)
    magic = loaded['magic']
    server_port = loaded['server_port']
    server_host = loaded['server_host']
