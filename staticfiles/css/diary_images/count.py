import os
dir = '.'
print(sum(os.path.isfile(os.path.join(dir,name)) for name in os.listdir(dir)))
