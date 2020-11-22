# Author :  Harrison Toppen-Ryan
# Description :  Lab 6, CSCI 141
# Date :  November 15th, 2020

# prompt_user function that defines the type of string and inputs 
def prompt_user(text_input, type_v):
    #If the type is a string
    if type_v == "str":
        return_var = str(input(text_input))
        return return_var
    #if the type is a integer 
    elif type_v == "int":
        return_var = int(input(text_input))
        return return_var
        


# caclulates the room footage if the input is a square or a rectangle 
def calc_room_sqaure_footage(shape):
    #if the shape is a square 
    if shape == "square":
        square_length = prompt_user("What is the length of the wall? ", "int")
        # square the input 
        return square_length ** 2
    #if the shao is a rectangle 
    elif shape == "rectangle":
        rectangle_lengthone = prompt_user("What is the length of the first dimension? ", "int")
        rectangle_lengthtwo = prompt_user("What is the length of the second dimension? ", "int")
        #multiply both inputs 
        return rectangle_lengthone * rectangle_lengthtwo
    

        
   

# main function that asks for number of rooms 
def main():
    room_num = int(input("What is the number of rooms? "))
    running_total_sqft = 0
    #for loop that repeats the number of rooms stated earlier 
    for i in range(0,room_num):
        ask_shape = input("Is the room a square or rectangle? ")
        # calc_room_sqaure_footage(ask_shape) 
        running_total_sqft +=  calc_room_sqaure_footage(ask_shape)
    # final return value for square feet
    print("The house footage is", running_total_sqft, "square feet")
#call the main function
main()

  
    
    

