import os
os.chdir('./media/')
it = 0
for f in os.listdir():
    filename,filext = os.path.splitext(f)
    if filext == ".png" or filext == ".jpg" or filext == "jpeg":
        print(filename, filext, "~image")
        newName = "img_" + str(it) + filext
        print(newName)
        os.rename(f, newName)
        it += 1
