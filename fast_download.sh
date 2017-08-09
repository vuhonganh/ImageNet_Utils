#!/bin/bash

to_download=("$@")

for argu in "${to_download[@]}"; do
    if [ ! -d ${argu} ]
    then
	echo "downloading ${argu}"
	./downloadutils.py --downloadOriginalImages --downloadBoundingBox --wnid ${argu}
    else
	echo "folder ${argu} already exists"
    fi

done
