#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    printf "\033[0;33m[-] \033[0;37mThis script must be run as root" 
    exit 1
fi

main() {
    printf "\n\033[0;34m[*] \033[0;37mInstalling...\n"
    apt-get install -y osslsigncode python3 python3-pip
    pip install -r requirements.txt
    printf '\n\033[0;32m[+] \033[0;37mInstallation completed!'
}

main