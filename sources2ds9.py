from astroquery.utils import parse_coordinates
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy as np
import csv

sourceFile = 'ItziarCat/sources.csv'
ds9File = sourceFile.replace('.csv', '_ds9.reg')

# read the sources in
s = []
with open(sourceFile) as f:
    reader = csv.reader(f, delimiter=" ")
    for r in reader:
        s.append(r)
s = s[1:]
nSources = len(s)

# kick out the ds9 region file
head1 = "# Region file format: DS9 version 4.1\n"
head2 = 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n'
head3 = 'fk5\n'

with open(ds9File, 'w') as o:
    o.write(head1)
    o.write(head2)
    o.write(head3)
    for source in s:
        c = SkyCoord(float(source[1]), float(source[2]), unit='deg')
        ctxt = c.to_string('hmsdms')
        ctxt = ctxt.replace(' ', ', ')
        ds = 'circle({0:},2.5")\n'.format(ctxt)
        o.write(ds)
