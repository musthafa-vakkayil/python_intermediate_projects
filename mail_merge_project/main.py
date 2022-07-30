#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

save_name = "letter_for_name.txt"

with open("./input/Letters/starting_letter.txt", mode="r") as file:
    contents = file.readlines()

with open("./input/Names/invited_names.txt", mode="r") as file:
    name = file.readlines()

for i in name:
    # Creating File Name
    file_name = save_name.replace("name", i).replace("\n", "")

    # Creating File Content
    file_content = contents[0].replace("[name]",i).replace("\n", "")
    for i in contents[1::]:
        file_content += i

    with open(f"./Output/ReadyToSend/{file_name}", mode="w") as file:
        file.write(file_content)








