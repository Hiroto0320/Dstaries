import glob, os

path = './diary_images/*.png'
i = 1
fileli = glob.glob(path)
print(fileli)

for file in fileli:
    os.rename(file, './rediary_images/' + str(i*2) + '.png')
    i+=1

fileli_after = glob.glob(path)
print(fileli_after)