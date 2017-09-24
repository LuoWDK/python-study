#!/usr/bin/env python
# -*- coding: utf-8 -*-

from astropy.io import fits
from astropy import wcs
import numpy as np
import os
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

# Get file path
fitsfile = os.path.join(wcs.__path__[0], 'out1.fits')

# Open fits file, then a HDUList object is returned.
hdulist = fits.open(fitsfile)

# Get image data
# hdulist[0] is the primary HDU, its data is an image.
data = hdulist[0].data

# Get image header
# A fits header consists of 80 byte "cards".
header = hdulist[0].header

# use "cards" to constructs image coords
# x naxis
nx = header['NAXIS1']
crvalx = header['CRVAL1']
cdeltax = header['CDELT1']
crpixx = header['CRPIX1']
x = np.arange(-crpixx*cdeltax+crvalx, (nx-crpixx)*cdeltax+crvalx, cdeltax)

# y naxis
ny = header['NAXIS2']
crvaly = header['CRVAL2']
cdeltay = header['CDELT2']
crpixy = header['CRPIX2']
y = np.arange(-crpixy*cdeltay+crvaly, (ny-crpixy)*cdeltay+crvaly, cdeltay)

# mesh grid
xy_x, xy_y = np.meshgrid(x, y)

# close fits file
hdulist.close()

plt.figure()

# regard image as scatter, where one coords pair has one image data
plt.scatter(xy_x, xy_y, c=data, edgecolors='none', cmap='gray')

# set axis label
plt.xlabel(header['CTYPE1']+' / '+header['CUNIT1'], fontsize=15)
plt.ylabel(header['CTYPE2']+' / '+header['CUNIT2'], fontsize=15)

# set start and end location of axis
plt.xlim(np.amin(xy_x), np.amax(xy_x))
plt.ylim(np.amin(xy_y), np.amax(xy_y))

# set color bar
plt.colorbar()

# set image tight in the figure
plt.tight_layout()

plt.show()
