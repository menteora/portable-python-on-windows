import os
import importlib.util
import sys
import argparse

def import_library(dir, name):
    spec = importlib.util.spec_from_file_location(name, dir + "/" + name +".py")
    library = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(library)
    return library

parser = argparse.ArgumentParser(description='Run script class with command line')
parser.add_argument('--module', action='store', dest='module_name',
                    help='Store a module name, if omitted is set equal to class')
parser.add_argument('--method', action='store', dest='method_name',
                    help='Store a method name')
parser.add_argument('--config', action='store', dest='config_name',
                    help='Store a config name')
requiredGroup = parser.add_argument_group('required named arguments')
requiredGroup.add_argument('--class', action='store', dest='class_name',
                    help='Store a class name', required=True)
args = parser.parse_args()

if not args.module_name:
    args.module_name = args.class_name

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)  
core_directory = os.path.join(parent_directory, 'core') 

ClassModule = import_library(core_directory, args.module_name)

# not tested yet
if args.config_name:
    ClassInstance = getattr(ClassModule, args.class_name)(args.config_name)
else:
    ClassInstance = getattr(ClassModule, args.class_name)()

# not tested yet
if args.method_name:
    result = getattr(ClassInstance, args.method_name)()
