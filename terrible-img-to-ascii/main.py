from PIL import Image
import numpy as np
import string
import imgpro.image as imgpro
img = Image.open('img.png', 'r')
array = np.array(img)
pixels = array.tolist()
grids = []
imgwidth = 100
wh = 10
counter1 = 0
counter2 = -1
counter3 = wh * -1
Mac = True
for a in pixels:
  counter2 += 1
  counter1 = -1
  if counter2 % (100/wh) == 0:
    for c in range(wh):
      grids.append([])
    counter3 += wh
    counter2 = 0
  for d in range(wh):
    grids[d + counter3].append([])

  
  for h in a:
    number = imgwidth - 1
    counter1 += 1
    counter4 = wh 
    for l in range(wh):
      number -= (100/wh)
      counter4 -= 1
      if counter1 > number:
        break
    grids[counter4 + counter3][counter2].append(h)
apix = Image.open('smallera.png', 'r')
array = np.array(apix)
apix = array.tolist()
bpix = Image.open('smallerb.png', 'r')
array = np.array(bpix)
bpix = array.tolist()
cpix = Image.open('smallerc.png', 'r')
array = np.array(cpix)
cpix = array.tolist()
letterlist = [apix, bpix, cpix]

def compareimg(img1, imglist):
  counter = -1
  counter1 = -1
  counter2 = -1
  counter3 = -1
  best = 0
  bestindx = 0
  for a in imglist:
    counter += 1
    counter1 = -1
    score = 0
    for b in a:
      counter2 = -1
      counter1 +=1
      for c in b:
        counter3 = -1
        counter2 +=1
        correct = True
        for d in c:
          counter3 += 1
          if counter3 > 2:
            continue
          if not(abs(d - img1[counter1][counter2][counter3]) < 40):
            correct = False
        if correct == True:
          score += 1
    if score > best:
      best = score
      bestindx = counter
  return bestindx

gridnum = 38

imgpro.main(grids[gridnum], Mac)
listchar = []
for a in grids:
  best = compareimg(a, letterlist)
  listchar.append(["a", "b", "c"][best])
counter = 0
text = ""
print("\n\n")
if listchar[gridnum] == "a":
  imgpro.main(apix, Mac)
if listchar[gridnum] == "b":
  imgpro.main(bpix, Mac)
if listchar[gridnum] == "c":
  imgpro.main(cpix, Mac)
print("\n\n")
for a in listchar:
  counter += 1
  text += a + " "
  if counter == 10:
    print(text)
    text = ""
    counter = 0
print(text)





chars = []
for a in string.ascii_letters + string.digits + "!@()+-=|%$#&":
  chars.append(a)
#print(chars)