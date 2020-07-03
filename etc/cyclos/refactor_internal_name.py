
import yaml  # PyYAML

from slugify import slugify

def get_internal_name(name):
    name = name.replace('€', 'euro')
    name = name.replace('T!nda', 'tinda')
    return slugify(name, separator='_')

def check_yml_consistency():
    print("internal_names keys:", internal_names.keys())
    print("cyclos_constant keys:", cyclos_constant.keys())

    for cat in internal_names:
        for item in internal_names[cat]:
            if get_internal_name(internal_names[cat][item]) not in cyclos_constant[cat]:
                print("item %s from cat %s mismatch"%(cat, item))

def gen_code_snippet():
    to_dump=""
    for cat in internal_names:
        for item in internal_names[cat]:
            to_dump += "    name = internal_names['"+cat+"']['"+item+"'],\n"
            to_dump += "    internal_name = '"+item+"',\n"
    f = open("name_snippet.py", "w")
    f.write(to_dump)
    f.close()

cyclos_constant = None
with open("/home/matthieu/api/etc/cyclos/cyclos_constants.yml", 'r') as cyclos_stream:
    try:
        cyclos_constant = yaml.full_load(cyclos_stream)
    except yaml.YAMLError as exc:
        assert False, exc

internal_names = None
with open("/home/matthieu/api/etc/cyclos/cyclos_internal_names.yml", 'r') as cyclos_stream:
    try:
        internal_names = yaml.full_load(cyclos_stream)
    except yaml.YAMLError as exc:
        assert False, exc


check_yml_consistency()

gen_code_snippet()
