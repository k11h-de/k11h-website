#!/bin/bash

# assuming this script is only run from the folder it is stored in
# if this is not the case uncomment and adapt next line
cd ~/k11h-website

if [[ $(git pull |& wc -l) > 1 ]]; then
  make publish > /dev/null
fi
