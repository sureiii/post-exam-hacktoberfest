print("Title of program: Positivity bot")
print()
while True:
  description = input("How are you feeling right now?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("you did your best, keep working hard")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("you should spread your positivity to others")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("you should call your family or friends, tell them how much they mean to you")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("better things are to come! be optimistic")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("Please don't. Close your eyes and count to ten. You might feel better. Tell a friend or family member if you do not and explain the situation.")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("See a doctor. Don't do anything stupid. There is still hope. We'll get over this together.")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("take a break, have a kit kat")
      counter += 1
      
  if counter == 0:
    
      output = "Sorry I don't really understand. Could you use different words please? Thank you!"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
