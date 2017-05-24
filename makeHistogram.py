'''
helper to make a histogram of the image voxels defined by the mask

Usage: image mask output.pdf
'''

import sys, matplotlib, numpy
import SimpleITK as sitk

def getMaskImageLabels(maskName):
  m = sitk.ReadImage(maskName)
  lstat = sitk.LabelStatisticsImageFilter()
  lstat.Execute(m,m)
  labels = lstat.GetLabels()[1:]
  return labels

def getMaskedImageArray(imageName,maskName,label=None):
  i = sitk.ReadImage(imageName)
  m = sitk.ReadImage(maskName)

  ind = sitk.GetArrayFromImage(i).flatten()
  mnd = sitk.GetArrayFromImage(m).flatten()

  if label is None:
    sel = numpy.select([mnd>0],[ind])
  else:
    sel = numpy.select([mnd==label],[ind])

  sel=sel[sel!=0].flatten()

  return sel

def makeHisto(a,fileName,title):

  import numpy as np
  import matplotlib.mlab as mlab
  import matplotlib.pyplot as plt

  # the histogram of the data
  n, bins, patches = plt.hist(a, bins="auto")

  # add a 'best fit' line
  #y = mlab.normpdf( bins, mu, sigma)
  #l = plt.plot(bins, y, 'r--', linewidth=1)

  plt.xlabel('value')
  plt.ylabel('count')
  plt.title(title)
  plt.grid(True)

  plt.savefig(fileName,format="pdf")
  plt.clf()
  #plt.show()

def main(argv):
  image = argv[1]
  mask = argv[2]
  output = argv[3]

  array = getMaskedImageArray(image,mask)

  makeHisto(array,output)

if __name__ == "__main__":
  main(sys.argv)
