import os
import re
import sys
path = sys.argv[-1]

d = {}

stability_txt = os.path.join(path, "Stability", "Stability_results.txt")
repro_info_txt = os.path.join(path, "Collect", "CafeFiles", "repro_info.txt")
archsim_txt = os.path.join(path, "Archsim", "Archsim_results.txt")

if 'QA' in path:
    latest_bios_ini = os.path.join(path, "Collect", "BiosPackage.ini")
else:
    latest_bios_ini = os.path.join(path, "Collect", "latest_bios.ini")
for file in os.listdir(os.path.join(path, "Collect")):
    if file.endswith("_params.ini"):
        params_ini = os.path.join(path, "Collect", file)
        break
for file in os.listdir(os.path.join(path, "Collect")):
    if file.endswith("_ParsedErrorInfoLog.txt"):
        errorlog_txt = os.path.join(path, "Collect", file)
        break

# Read VP info
with open(params_ini, 'r') as file:
    for line in file.readlines():
        # print(line.rstrip().split("=")[-1])
        if "=" in line:
            d[line.replace(' ', '').split("=")[0]] = line.replace(' ', '').split("=")[-1]
        else: pass

# Read BIOS
with open(latest_bios_ini, 'r') as file:
    if 'QA' in latest_bios_ini:
        for line in file.readlines():
            if "IFWI " in line:
                d["bios"] = line.replace(' ', '').split("=")[-1]
                break
    else:
        for line in file.readlines():
            d["bios"] = line
            break

# Read Cafe/Archsim info
with open(repro_info_txt, 'r') as file:
    for line in file.readlines():
        # print(line.rstrip().split("=")[-1])
        if "=" in line:
            d[line.replace(' ', '').split("=")[0]] = line.replace(' ', '').split("=")[-1]
        else: pass

# Read stability result
with open(stability_txt, 'r') as file:
    for line in file.readlines():
        # print(line.rstrip().split("=")[-1])
        if "=" in line:
            d[line.replace(' ', '').split("=")[0]] = line.replace(' ', '').split("=")[-1]
        else: pass

# Read Archsim result
with open(archsim_txt, 'r') as file:
    for line in file.readlines():
        # print(line.rstrip().split("=")[-1])
        if "=" in line:
            d[line.replace(' ', '').split("=")[0]] = line.replace(' ', '').split("=")[-1]
        else: pass

# Read Error Block
with open(errorlog_txt, 'r') as file:
    input_data =file.read()
    # print(line.rstrip().split("=")[-1])
    result = re.search(r'.*Error_Block:\s*(.*)$', input_data, re.DOTALL)
    error_block = result.group(1)

# print(d)
print('Failure Path = {}'.format(d["RemoteDir"]).rstrip())
print('Failure ID = {}')
print('VP = {}'.format(d['VP'].rstrip()))
print('Failing Host = {}'.format(d["OriginalHost"]).rstrip())
print('\nIFWI/BIOS = {}'.format(d["bios"]))
print('Cafe Version = {}'.format(d["CafeVersion"].rstrip()))
print('Built-in Arhcsim Version = {}'.format(d["Built-inArchsimVersion"].rstrip()))
print('\nFail_Percent = {}'.format(d["Fail_Percent"].rstrip()))
print('Fail_Count = {}'.format(d["Fail_Count"].rstrip()))
print('Fail_Reproduced = {}'.format(d["Fail_Reproduced"].rstrip()))
print('FAILED_MAX_LOOPS = {}'.format(d["FAILED_MAX_LOOPS"].rstrip()))
print('Test_Failed_On_Archsim = {}\n'.format(d["Test_Failed_On_Archsim"].rstrip()))
print('Error_Block:\n\n\t{}'.format(error_block))