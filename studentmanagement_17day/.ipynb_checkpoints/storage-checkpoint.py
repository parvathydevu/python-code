import json
import os
 
class Storage(object):  #class name 
 
    def __init__(self, filepath='students.json'):
        self.filepath = filepath
 
    def save(self, stds):
        with open(self.filepath, 'w') as f:
            json.dump(stds, f, indent=4)
 
    def load(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath) as f:
            return json.load(f)