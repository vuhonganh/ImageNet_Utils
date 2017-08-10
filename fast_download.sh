#!/bin/bash

to_download=("$@")

for argu in "${to_download[@]}"; do
    file_img=${argu}.tar
    file_bbox=${argu}.tar.gz
    
    if [ ! -e ${file_img} ]
    then
	echo "downloading image file ${file_img}"
	./downloadutils.py --downloadOriginalImages --wnid ${argu}	
    else
	echo "image file ${file_img} already exists"
    fi
    
    if [ ! -e ${file_bbox} ]
    then
	echo "downloading annotation file ${file_bbox}"
	./downloadutils.py --downloadBoundingBox --wnid ${argu}
    else
	echo "annotation file ${file_bbox} already exists"
    fi
    
done
