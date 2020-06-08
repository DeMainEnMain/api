
from slugify import slugify

def get_internal_name(name):
    name = name.replace('€', 'euro')
    name = name.replace('T!nda', 'tinda')
    return slugify(name, separator='_')

