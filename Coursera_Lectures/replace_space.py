#!/usr/bin/env python3

import os, glob, sys
import re
import shutil

files = glob.glob('./wk*/*.pdf')

for fil in files:
    #print (fil)
    fname = fil.split('/')[-1]
    wk = fil.split('/')[1][-1]
    print (fname, wk)
    shutil.move(fil, '0'+wk+'_'+fname)
    #fil_new = re.sub(' ', '_', fil)
    #print (fil_new)
    #shutil.move
    #shutil.copy(fil, fil_new)
    #print ('moving', fil, 'to new file:', fil_new )
    #shutil.move(fil, fil_new)


#aa = re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
#print (aa)
    
