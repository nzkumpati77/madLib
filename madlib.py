#PROGRAM START
# This part of the program assigns each input the user gives to a variable that can be refrenced later in the code
print("Hello! Welcome to the adlib generator!\nFill out the prompts to create your madlib!")
Animal = input("Enter an animal:: ")
Emotion = input("Enter an emotion:: ")
Limb = input("Enter a human limb:: ")
Emotion2 = input("Enter a different emotion:: ")
Verb = input("Enter a verb(remove the 'ing' if present):: ")
Vehicle = input("Enter a vehicle:: ")
Location = input("Enter a location:: ")
#This code segment holds the input genre, which allows the user to choose what genre they want their madlib in
genre = input("Finally, Enter a genre for your madlib! (Adventure, Comedy, and Horror):: ")
'''
This is the madLib_list and its purpose is to hold all strings that are in the madlib into one container, 
that way there is no need to retype all text statements that are in the main madlib
for each genre when outputting the madlib to the user

'''
madLib_List = ["I traveled the rainforest and I was stunned to see a ", ". The animal looked ", ". I pet the ", 
" with my ", ". It became ", ". So I started to ", ". Luckily, my friend found me with his ", ". And we escaped, heading towards "]
# This code segment is a function where each input by the user is inserted into the madLib_list at a specific location in the list
def createStory():
    madLib_List.insert(1, Animal)
    madLib_List.insert(3, Emotion)
    madLib_List.insert(5, Animal)
    madLib_List.insert(7, Limb)
    madLib_List.insert(9, Emotion2)
    madLib_List.insert(11, Verb)
    madLib_List.insert(13, Vehicle)
    madLib_List.insert(15, Location)
#This is the main function in the program creating the madlib using the genre as a parameter, giving different madlibs based on the parameter
def createMadlib(genre):
    # This long selection statement(if, elif, elif, else) is to give a madlib based on the genre parameter
    if genre == "Adventure" or genre == "adventure":
        print("Here is your " + genre + " madlib")
        createStory()
        #After checking both the genre and inserting the inputs through the createStory function, the entire list is printed out which holds the madlib, using a for loop
        for i in range(len(madLib_List)):
            print(madLib_List[i], end="")
    elif genre == "Comedy" or genre == "comedy":
        print("Here is your " + genre + " madlib")
        madLib_List[5] = ". I began to "
        madLib_List[6] = ", suddenly, I felt a hippo on my bottom. I was in no need of a "
        createStory()
        for i in range(len(madLib_List)):
            print(madLib_List[i], end="")
    elif genre == "Horror" or genre == "horror":
        print("Here is your " + genre + " madlib")
        madLib_List[5] = ". I fell. I tried to "
        madLib_List[6] = " and my eyes were still set on the "
        createStory()
        for i in range(len(madLib_List)):
            print(madLib_List[i], end="")
    else:
        print("Make sure you chose one of the three genres given being case sensitive. Run the game again to start over!")
#This is when the function is called
createMadlib(genre)
