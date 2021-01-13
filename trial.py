import os

for dirpath, dirs, files in os.walk('/home/threevr/Doctrine/Features'):
  for filename in files:
    fname = os.path.join(dirpath,filename)
    if fname.endswith('.py'):
      print(fname)
