#! /bin/bash
#
# create_file.sh
# Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#

SPACE=" "
HYPHEN="-"
DATE=$(date +%F)
ASSETS_DIR="assets/"$DATE
FILENAME=$DATE

for ARG in "$@"
do
	FILENAME=$FILENAME-\<${ARG/$SPACE/$HYPHEN}\>
done

FILENAME=$FILENAME.md
touch $FILENAME
mkdir $ASSETS_DIR
