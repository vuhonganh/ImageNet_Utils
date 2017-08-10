#!/usr/bin/env python
from __future__ import print_function
from nltk.corpus import wordnet
import os

list_dir = os.listdir('./')
list_dir = [e for e in list_dir if e[0] == 'n']
set_synset = set()

for e in list_dir:
    idx_to_first_dot = e.find('.tar')
    if idx_to_first_dot != -1:
        wnid = e[:idx_to_first_dot]
        set_synset.add(wnid)
    
for e in set_synset:
    try:
        id = int (e[1:])  # ignore the letter n at begin of synset
        synset = wordnet.synset_from_pos_and_offset('n', id)
        syn_name = synset.name().split('.')[0]
        print('%-15s %-20s %-20s' % (e, syn_name, synset))
    except ValueError as e:
        pass

