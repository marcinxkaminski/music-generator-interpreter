#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]
        then
                if brew &>/dev/null
                    then
                            /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
                            brew install sox
                else
                    if ! brew ls --versions sox &>/dev/null
                    then
                              brew install sox
                    fi
                fi
else
        if [[ $(dpkg-query -W -f='${Status}' sox 2>/dev/null | grep -c "ok installed") -eq 0 ]]
                then
                        apt-get install sox
        fi
fi

python3.6 -m pip install -r requirements.txt
python3.6 app.py "$1"
