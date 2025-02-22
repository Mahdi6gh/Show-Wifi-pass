import subprocess as sp
import re

output = sp.getoutput(f'netsh wlan show profiles name=*')
wifi_name_list = []
for name_index in [m.start() for m in re.finditer('Name', output)]:
    wifi_name_list.append(output[name_index:name_index+output[name_index:].find('Control options')].split(':')[1].strip())

for name in wifi_name_list:
    output = sp.getoutput(f'netsh wlan show profile name="{name}" key=clear')
    output = output[output.find('Key Content'):output.find('Cost settings')]
    output = output[output.find(':')+2:]
    output = output.strip()
    print ("{:<30}|  {:<}".format(name, output))
    f=open("pass.txt","a")
    f.write("{:<30}|  {:<}".format(name, output)+"\n")
    f.close()
    