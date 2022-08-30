import hashlib
import json
from os.path import exists
from functools import wraps

def cached(func):

    def store_cache(filepath, something):
        with open(filepath, 'w') as json_file:
            json.dumps(something, json_file)
    
    def read_cache(filepath):
        if not exists(filepath):
            return False
        with open(filepath, 'r') as myfile:
            data = myfile.read()
        something = json.loads(data)
        return something
    
    @wraps
    def wrapper(*args, **kwargs):
        m = hashlib.sha256()
        for arg in args[1:]:
            m.update(bytes(str(arg), 'utf-8'))
        
        key_parts = [func.__name__] + [m.hexdigest()]
        filepath = "mocks/" + '-'.join(key_parts) + ".json"
        print(filepath)
        result = read_cache(filepath)

        if result:
            return result
        else:
            result = func(*args, **kwargs)
            store_cache(filepath, result)
        return result
    return wrapper