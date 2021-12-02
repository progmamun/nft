from PIL import Image

number_of_bg=8
number_of_body=8
number_of_cap=6
number_of_eye=6
number_of_mouth=6

for a in range(1,number_of_bg+1):
  for b in range(1,number_of_body+1):
    for c in range(1,number_of_cap+1):
      for d in range(1,number_of_eye+1):
        for e in range(1,number_of_mouth+1):
          bg = Image.open(("background/bg{}.png".format(a))).convert("RGBA")
          body=Image.open(("body/body{}.png".format(b))).convert("RGBA")
          cap = Image.open(("eye/eye{}.png".format(c))).convert("RGBA")
          eye = Image.open(("eye/eye{}.png".format(d))).convert("RGBA")
          mouth = Image.open(("mouth/mouth{}.png".format(e))).convert("RGBA")

          bg.paste(body,(0,0),body)
          bg.paste(cap,(0,0),cap)
          bg.paste(eye,(0,0),eye)
          bg.paste(mouth,(0,0),mouth)
          bg.save("result/duck{}+{}+{}+{}+{}.png".format(a,b,c,d,e))