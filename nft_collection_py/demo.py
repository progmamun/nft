while True:
  total_nft = input("\n Enter the number of NFTs you would like to generate. Eg. 1k/3k/5k/10k")

  try:
    total_nft = int(total_nft)
    break

  except ValueError:
    print("\n Please enter a numeric value. The input you entered is not numeric")

var_list=[]

bg_files = listdir("/content/project/background")
var_list.append(bg_files)

face_files = listdir("/content/project/face")
var_list.append(face_files)

eyebrows_files = listdir("/content/project/eyebrows")
var_list.append(eyebrows_files)

eye_files = listdir("/content/project/eyes")
var_list.append(eye_files)

forehead_files = listdir("/content/project/forehead")
var_list.append(forehead_files)

mouth_files = listdir("/content/project/mouth")
var_list.append(mouth_files)

crown_files = listdir("/content/project/crown")
var_list.append(crown_files)

ornaments_files = listdir("/content/project/ornaments")
var_list.append(ornaments_files)

total_combination = 1
for x in var_list:
  total_combination = total_combination*len(x)

print("\n With your attributes and samples given, a total of {} number of NFTs can be generated".format(total_combination))

if total_combination<total_nft:
  print("\n You don't have enough attributes to generate {} NFTs. With all your attributes only {} NFTs can be generated".format(total_nft, total_combination))
  exit


main= []
i= 1
while True:
  bg = random.choice(bg_files)
  face = random.choice(face_files)
  eyebrow = random.choice(eyebrows_files)
  eye = random.choice(eye_files)
  forehead = random.choice(forehead_files)
  mouth = random.choice(mouth_files)
  crown = random.choice(crown_files)
  ornaments = random.choice(ornaments_files)

  img_name = "image+{}+{}+{}+{}+{}+{}+{}+{}".format(bg.split('.')[0],face.split('.')[0],eyebrow.split('.')[0],eye.split('.')[0],forehead.split('.')[0],mouth.split('.')[0],crown.split('.')[0],ornaments.split('.')[0])
  
  if img_name not in main:
    main.append(img_name)
    bg_img = Image.open("project/background/"+bg).convert("RGBA")
    face_img = Image.open("project/face/"+face).convert("RGBA")
    eyebrow_img = Image.open("project/eyebrows/"+eyebrow).convert("RGBA")
    eye_img = Image.open("project/eyes/"+eye).convert("RGBA")
    forehead_img = Image.open("project/forehead/"+forehead).convert("RGBA")
    mouth_img = Image.open("project/mouth/"+mouth).convert("RGBA")
    crown_img = Image.open("project/crown/"+crown).convert("RGBA")
    ornaments_img = Image.open("project/ornaments/"+ornaments).convert("RGBA")
    
    bg_img.paste(face_img,(0,0),face_img)
    bg_img.paste(eyebrow_img,(0,0),eyebrow_img)
    bg_img.paste(eye_img,(0,0),eye_img)
    bg_img.paste(forehead_img,(0,0),forehead_img)
    bg_img.paste(mouth_img,(0,0),mouth_img)
    bg_img.paste(crown_img,(0,0),crown_img)
    bg_img.paste(ornaments_img,(0,0),ornaments_img)

    bg_img.save("project/collection/image{}.png".format(i))
    print("Image{} generated".format(i))

    i=i+1

    if len(main)==total_nft:
      print("{} generation of NFT designs completed. Please check the collection folder to view the designs".format(total_nft))
      break