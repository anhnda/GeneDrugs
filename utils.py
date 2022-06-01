import os

def get_insert_dict(d, k, v):
    try:
        v = d[k]
    except:
        d[k] = v
    return v

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)