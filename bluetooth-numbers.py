import os
import sys
import argparse
import yaml

repo_location_variable = 'BLUETOOTH_REPO'
repo_location = None
repo_message = '''
May be specified by environment variable, %s,
or by command line switch --bluetooth-repo.

Bluetooth repo may be downloaded via command,
git clone https://bitbucket.org/bluetooth-SIG/public.git'''%(repo_location_variable)

for i in range(len(sys.argv)) :
    target = '--bluetooth-repo'
    if sys.argv[i].find(target) != 0 : continue
    tokens = sys.argv[i].split('=')
    if len(tokens) == 2 :
        repo_location = tokens[1]
    elif len(tokens) == 1 :
        repo_location = sys.argv[i+1]
    else :
        raise RuntimeError(sys.argv[i])
if None == repo_location :
    repo_location = os.environ.get('BLUETOOTH_REPO')

if None == repo_location :
    print('Bluetooth repo not specified.'+repo_message)
    quit()

if not os.path.exists(repo_location) :
    print('Bluetooth repo specified, but does not exist.'+repo_message)
    quit()

parser = argparse.ArgumentParser()
parser.add_argument('--bluetooth-repo')
parser.add_argument('--verbose',action='store_true')
uuids = parser.add_mutually_exclusive_group(required=True)

options = []
paths = {}
for folder in ['uuids','core','company_identifiers'] :
    path = repo_location+'/assigned_numbers/%s'%(folder)
    files = os.listdir(path)
    for file in files :
        option = file[:-5]
        options.append(option)
        paths[option] = path+'/'+file
        uuids.add_argument('--%s'%(option.replace('_','-')))
args = parser.parse_args()

for option in options :
    arg = args.__dict__.get(option)
    if None != arg :
        break

if None == arg : raise RuntimeError

if 0 == arg.lower().find('0x') :
    value = int(arg[2:],16)
else :
    value = int(arg,10)

filename = paths.get(option)
if args.verbose :print('loading %s'%(filename))
with open(filename,'r') as file :
        db = yaml.safe_load(file)

for key in db :
    records = db[key]
    if list == type(records) :
        rkey = None
        if args.verbose : print('keys:',list(records[0].keys()))
        for skey in records[0] :
            if 'uuid' == skey or 'value' == skey :
                rkey = skey
                if args.verbose : print('rkey: "%s"'%(rkey))
                break
        if None == rkey :
            raise RuntimeError(record)
        found = False
        for record in records :
            if record.get(rkey) == value :
                for skey in record :
                    if skey != rkey :
                        print('%s: %s'%(skey,record.get(skey)))
                found = True
if not found :
    print('No match for %s in %s'%(arg,filename))
