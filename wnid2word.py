#!/usr/bin/env python
from __future__ import print_function
from nltk.corpus import wordnet
import os

list_dir = os.listdir('./')
list_dir = [e for e in list_dir if e[0] == 'n']

for e in list_dir:
    id = int (e[1:])
    synset = wordnet.synset_from_pos_and_offset('n', id)
    syn_name = synset.name().split('.')[0]
    print('%-15s %-20s %-20s' % (e, syn_name, synset))


