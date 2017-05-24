import makeHistogram, sys

def main(argv):
  import os
  rootDir = argv[1]
  subjects = os.listdir(rootDir)

  label = "OPT. Ax DWI 13 B VALUES - as a 15 frames MultiVolume by GE.B-value frame 0-label.nrrd"
  maps = ["Slow diff fraction.nrrd","Slow diffusion map.nrrd","Fast diffusion map.nrrd"]

  for s in subjects:
    # ignore .DS_Store on Mac ...
    if s.startswith("."):
      continue
    for m in maps:
      labelFile = os.path.join(rootDir,s,label)
      mapFile = os.path.join(rootDir,s,m)

      labels = makeHistogram.getMaskImageLabels(labelFile)
      print "Labels:",labels

      for l in labels:
        if l == 1:
          labelName = "TumorTZ (label 1)"
        elif l == 3:
          labelName = "NormalTZ (label 3)"
        else:
          labelName = "Label"+str(l)
        labelName = "Label"+str(l)
        histoFile = os.path.join(rootDir,s,m.split(".")[0]+"-histogram-"+labelName+".pdf")
        array = makeHistogram.getMaskedImageArray(mapFile,labelFile,label=l)
        makeHistogram.makeHisto(array,histoFile,title=m.split(".")[0]+" histogram, "+labelName)

        #print m,l," array ",array

if __name__ == "__main__":
  main(sys.argv)
