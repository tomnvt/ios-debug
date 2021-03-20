import re
from collections import namedtuple


def get_protocols_to_protocol_functions_dict(repository_protocols, path_to_content_map):
    Function = namedtuple('Function', 'name, params, return_type')
    protocol_to_protocol_functions = {}
    for protocol in repository_protocols:
        for path in path_to_content_map:
            if 'protocol ' + protocol in path_to_content_map[path]:
                content = path_to_content_map[path]
                function_instances = []
                protocol_definition = re.findall('protocol ' + protocol + ' {([\s\S]*?)\n}', content)[0]
                functions = protocol_definition.split('func ')
                functions = [func for func in functions if 'typealias ' not in func and 'var ' not in func]
                functions = [function.strip() for function in functions]
                functions = [function for function in functions if function]
                functions = [function.replace('\n', '') for function in functions]
                functions = [' '.join(function.split()) for function in functions]
                print('- ' * 40)
                print('Found functions for protocol', protocol + ':')
                print()
                for func in functions:
                    function_name = re.findall('(\w+)', func)[0]
                    params_part = re.findall('[\w+<>]\((.*?)\)', func)[0]
                    print(params_part)
                    params = params_part.split(', ')
                    return_type = re.findall('-> (.*)', func)
                    if params[0] == '':
                        params = None
                    if return_type:
                        return_type = return_type[0]
                    else:
                        return_type = None

                    print('func', func)
                    print('- name:', function_name)
                    print('- params:', params)
                    print('- return type:', return_type)
                    function_instances.append(Function(function_name, params, return_type))
                    print()
                print('- ' * 40)
                protocol_to_protocol_functions[protocol] = function_instances
                print()
    return protocol_to_protocol_functions
