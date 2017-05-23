'''
helper to make a histogram of the image voxels defined by the mask

Usage: image mask output.pdf
'''

import sys, matplotlib, numpy
import SimpleITK as sitk

def makeHisto(a,fileName):

  import numpy as np
  import matplotlib.mlab as mlab
  import matplotlib.pyplot as plt

  # the histogram of the data
  n, bins, patches = plt.hist(a, 50, normed=1, facecolor='green', alpha=0.75)

  # add a 'best fit' line
  #y = mlab.normpdf( bins, mu, sigma)
  #l = plt.plot(bins, y, 'r--', linewidth=1)

  plt.xlabel('value')
  plt.ylabel('count')
  plt.grid(True)

  plt.savefig(fileName,format="pdf")
  #plt.show()

def main(argv):
  image = argv[1]
  mask = argv[2]
  output = argv[3]

  i = sitk.ReadImage(image)
  m = sitk.ReadImage(mask)

  ind = sitk.GetArrayFromImage(i).flatten()
  mnd = sitk.GetArrayFromImage(m).flatten()

  sel = numpy.select([mnd>0],[ind])
  sel=sel[sel>0].flatten()

  makeHisto(sel,output)

if __name__ == "__main__":
  main(sys.argv)
