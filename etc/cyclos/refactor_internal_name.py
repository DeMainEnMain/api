
import yaml  # PyYAML

from slugify import slugify
import re

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

def gen_constant_internal():

    constants_file = open('/home/matthieu/api/etc/cyclos/cyclos_constants_internal.yml', 'w')
    correspondance_file = open('/home/matthieu/api/etc/cyclos/cyclos_internal_correpondance.yml', 'w')
    for category in sorted(internal_names.keys()):
        correspondance_file.write(category + ':\n')
        for i_name in sorted(internal_names[category].keys()):
            name = internal_names[category][i_name]
            try:
                old_i_name = get_internal_name(name)
                cst_id = cyclos_constant[category][old_i_name]
                constants_file.write("%s: '%d'\n"%(i_name, cst_id))
                correspondance_file.write("  %s: '%s'\n"%(old_i_name, i_name))
            except:
                print("skipping " + i_name)

def refactor_api():
    file_to_refactor = ['../../src/api/bdc_cyclos/views.py']
    p = re.compile("[str\(]*settings.CYCLOS_CONSTANTS\['([\w_-]*)'\]\['([\w_-]*)'\][\)]*")
    p2 = re.compile("settings.CYCLOS_CONSTANTS\[")
    q = re.compile("\['field'\]\['internalName'\] == '([\w_-]*)'")
    for fn in file_to_refactor:
        f = open(fn, 'r')
        content = f.readlines()
        f.close()
        nb_replace = 0
        nb_occurence = 0
        for index, l in enumerate(content):
            result = p2.search(l)
            if result != None:
                nb_occurence += 1

            result = p.search(l)
            if result != None:
                replace_str = r"cyclos.id['%s']"%correpondance[result.group(1)][result.group(2)]
                #print(result.group(0), replace_str)#result.group(1), r.group(2))
                l = p.sub(replace_str, l)
                content[index] = l
                nb_replace += 1

            result = q.search(l)
            if result != None:
                replace_str = r"['field']['internalName'] == '%s'"%correpondance['transaction_custom_fields'][result.group(1)]
                l = q.sub(replace_str, l)
                content[index] = l
                nb_replace += 1
                nb_occurence += 1

        print("%d occurences in %s, %d replacements => %d remaining manual changes"%(nb_occurence,
            fn, nb_replace, nb_occurence-nb_replace))

        f = open(fn, 'w')
        f.write("".join(content))
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

correpondance = None
with open("/home/matthieu/api/etc/cyclos/cyclos_internal_correpondance.yml", 'r') as cyclos_stream:
    try:
        correpondance = yaml.full_load(cyclos_stream)
    except yaml.YAMLError as exc:
        assert False, exc


#check_yml_consistency()
#
#gen_code_snippet()
#
gen_constant_internal()

refactor_api()
