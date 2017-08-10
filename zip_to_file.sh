#!/bin/bash
file_zip_name='zip_file.zip'  # default name
file_zip_name=$1
ls | grep tar | zip -@ $1
