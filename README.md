# Bluetooth Numbers

A simple Python script to resolve various Bluetooth SIG defined numbers to the names.

A while back Bluetooth SIG released a [repo](https://bitbucket.org/bluetooth-SIG/public.git) of assigned numbers.  The script currently builds a command line from some of my favorite folders in the repo to resolve various categories of defined numbers.  The repo sould be cloned somewhere and reference by either the environment variable, BLUETOOTH_REPO, or via the switch --bluetooth-repo.

## By way of example
### No parameters
Since the CLI is built from the repo content, there is an initial simple CLI handling only the repo location. 
<pre>
$ python3 bluetooth-numbers.py                                               
Bluetooth repo not specified.
May be specified by environment variable, BLUETOOTH_REPO,
or by command line switch --bluetooth-repo.

Bluetooth repo may be downloaded via command,
git clone https://bitbucket.org/bluetooth-SIG/public.git
</pre>

### Clone repo
<pre>
$ git clone https://bitbucket.org/bluetooth-SIG/public.git
Cloning into 'public'...
Receiving objects: 100% (5665/5665), 7.24 MiB | 10.26 MiB/s, done.
Resolving deltas: 100% (4021/4021), done.
</pre>

#### Specify repo location via CLI
Editied for readability
<pre>
$ python3 bluetooth-numbers.py --bluetooth-repo public                       
usage: bluetooth-numbers.py [-h] [--bluetooth-repo BLUETOOTH_REPO] [--verbose]
                            (--browse-group-identifiers BROWSE_GROUP_IDENTIFIERS | 
  --characteristic-uuids CHARACTERISTIC_UUIDS | --declarations DECLARATIONS | --descriptors DESCRIPTORS |
  --member-uuids MEMBER_UUIDS | --mesh-profile-uuids MESH_PROFILE_UUIDS | --object-types OBJECT_TYPES | 
  --protocol-identifiers PROTOCOL_IDENTIFIERS | --sdo-uuids SDO_UUIDS | --service-class SERVICE_CLASS |
  --service-uuids SERVICE_UUIDS | --units UNITS | --ad-types AD_TYPES | --amp AMP | 
  --appearance-values APPEARANCE_VALUES | --class-of-device CLASS_OF_DEVICE | 
  --coding-format CODING_FORMAT | --core-version CORE_VERSION | --diacs DIACS | 
  --formattypes FORMATTYPES | --mws-channel-type MWS_CHANNEL_TYPE | --namespace NAMESPACE | 
  --namespaces NAMESPACES | --pcm-data-format PCM_DATA_FORMAT | --psm PSM |
  --sdp-base-uuid SDP_BASE_UUID | --transport-layers TRANSPORT_LAYERS | --uri-schemes URI_SCHEMES |
  --company-identifiers COMPANY_IDENTIFIERS)
bluetooth-numbers.py: error: one of the arguments --browse-group-identifiers --characteristic-uuids
  --declarations --descriptors --member-uuids --mesh-profile-uuids --object-types --protocol-identifiers
  --sdo-uuids --service-class --service-uuids --units --ad-types --amp --appearance-values 
  --class-of-device --coding-format --core-version --diacs --formattypes --mws-channel-type
  --namespace --namespaces --pcm-data-format --psm --sdp-base-uuid --transport-layers --uri-schemes
  --company-identifiers is required
</pre>

### Specify repo location by environment variable
<pre>
$ export BLUETOOTH_REPO=${PWD}/public 
</pre>
### Lookup AD type
See [Bluetooth Advertising Data Basics](https://docs.silabs.com/bluetooth/9.1.1/bluetooth-fundamentals-advertising-scanning/advertising-data-basics)
<pre>
$ python3 bluetooth-numbers.py --ad-types 9            
name: Complete Local Name
reference: Core Specification Supplement, Part A, Section 1.2

$ python3 bluetooth-numbers.py --ad-types 0xff
name: Manufacturer Specific Data
reference: Core Specification Supplement, Part A, Section 1.4
</pre>

### Look up company identifier
As used in Manufacturer Specific Data
<pre>
$ python3 bluetooth-numbers.py --company-identifiers 0x2ff
name: Silicon Laboratories
</pre>

### Lookup Service UUID
<pre>
$ python3 bluetooth-numbers.py --service-uuids 0x1809
name: Health Thermometer
id: org.bluetooth.service.health_thermometer
</pre>

### Lookup Core version
As used in LL_VERSION_IND
<pre>
$ bluetooth-numbers --core-version 6
name: Bluetooth® Core Specification 4.0 (Withdrawn)

$ bluetooth-numbers --core-version 0xb
name: Bluetooth® Core Specification 5.2
</pre>
