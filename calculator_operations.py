# Importing all files / modules required for this file

import random
import main
import doctest
from decimal import Decimal, getcontext

def operationRandom(value):
    """(str) -> str
    The functions takes in a number in the type string and returns a randomly
    generated number between 1 to the number in the string. If the string
    isn't a number the function returns a string, "INVALID".
    """
    
    # Checking if 'value' is a positive integer

    if value.isnumeric():
    
        # Converting value from a str to an integer
        value = int(value)
        
        # Generating a random number between 1 - value 
        randomNumber = random.randint(1, value)
        
        # returning randomly generated number as a string
        return str(randomNumber)
    
    # Pathway if 'value' is not a positive integer
    else:
        
        # Plays an error noise
        main.invalidInput()
        
        # Alerting the user that their selection is invalid
        return "INVALID INPUT"

def operationSquared(value):
    """ (str) -> str
    The purpose of this function is to take in a positive integer
    in the type 'string' and to return a string of the number 
    raised to the power of two. 
    """

    # A try and except block to ensure that the 
    # string contains a positive integer
    try:
        
        # Converting the string to a float and raising it to the power of two
        squared = str(float(value) ** 2)
        
        # Removing the decimal points from the answer
        # if its an integer
        if squared[-2:] == ".0":
                
        # Indexing a new total without the decimal
            squared = squared[:-2]

        # Returning the answer
        return squared

    except:

        # Plays an error noise
        main.invalidInput()

        # Alerting the user that their selection is invalid
        return "INVALID INPUT"

def sortingLists(value):
    """(str) -> str, list, list
    The purpose of this function is to sort out
    all the numbers into a list labelled 'numbers' and
    to sort their signs into a list labelled 'signs'.
    """

    # Assigning lists to the following variables
    numbers = []
    signs = ["null"]
    
    # Looping through each character in the inputted number 
    # and sorting them into either of the two lists, 
    # numbers or signs
    for char in value:
        
        # Checking if the current character is
        # a sign
        if char in ["+", "–", "÷", "×"] or not value[0]:
            
            # Recognizing the index of the sign
            charIndex = value.index(char)
            
            # Appending the sign to its respective list
            signs.append(value[charIndex])

            # Obtaining the number using indexing and 
            # appending it to its respective list
            numbers.append(value[:charIndex])
            
            # Updating value
            value = value[charIndex+1:]

    # Appending the last remaining number after the
    # loop to the list 'numbers'.
    numbers.append(value)

    # Returning values
    return value, signs, numbers

def initialOperation(num_index, sign_index, total, numbers, signs):
    """(int, int, str, list, list) -> int, int, str, list, list
    This function is the first step in calculating the answer of
    any given problem and is used to assign the variable 'total'
    with a number value in the type string.
    """
    
    # Try and except block in order to ensure there are 
    # no mathematical errors in the typed problem 
    try:
        
        # The lists 'numbers' and 'signs' will have all the numbers
        # and signs designated respectively. With both num_index and 
        # sign_index accumulators ensuring that no syntax errors arise
        # due to list index being out of range
        if num_index < (len(numbers)) and sign_index < (len(signs)):

            # Sets context for the module Decimal allowing the calculator
            # to do decimal calculations without encountering issues with
            # a floating point problem caused by using float. 
            getcontext().prec = 12

            # If Block for addition
            if signs[sign_index] == "+":
                total += str(float(Decimal(float(numbers[num_index])) + \
                Decimal(float(numbers[num_index+1]))))

            # Elif block for subtraction
            elif signs[sign_index] == "–":
                total += str(float(Decimal(float(numbers[num_index])) - \
                Decimal(float(numbers[num_index+1]))))

            # Elif block for multiplication
            elif signs[sign_index] == "×":
                total += str(float(Decimal(float(numbers[num_index])) * \
                Decimal(float(numbers[num_index+1]))))


            # Elif block for division
            elif signs[sign_index] == "÷":
                total += str(float(Decimal(float(numbers[num_index])) / \
                Decimal(float(numbers[num_index+1]))))

        # Updating the accumulators
        num_index += 1
        sign_index += 1

        # Returning the updated values for the function
        # operationEquals(value, num_index, sign_index, total)
        return num_index, sign_index, total, numbers, signs

    except:
        
        # Plays an error noise
        main.invalidInput()

        # Returns a string alerting the user that their input is invalid
        return "INVALID INPUT"

def operationAdd(total, num_index, numbers):
    """(str, int, list) -> str
    The purpose of this function is to add the next number to the
    pre-existing total.
    """
    # Adding the total as a float with the following 
    # number and returning as a string
    addition = str(float(Decimal(float(total)) \
             + Decimal(float(numbers[num_index+1]))))
    return addition

def operationSubtract(total, num_index, numbers):
    """(str, int, list) -> str
    The purpose of this function is to subtract the number
    following the pre-existing total.
    """
    
    # Subtracting the following number from the total
    # as a float and returning the answer as a string
    subtraction = str(float(Decimal(float(total)) \
                - Decimal(float(numbers[num_index+1]))))
    return subtraction

def operationMultiply(total, num_index, numbers):
    """(str, int, list) -> str
    The purpose of this function is to multiply the number next to the
    pre-existing total. 
    """
    # Multiplying the current total as a float with the
    # following number and returning the answer as a string
    multiplication = str(float(Decimal(float(total)) \
                   * Decimal(float(numbers[num_index+1]))))
    return multiplication

def operationDivide(total, num_index, numbers):
    """(str, int, list) -> str
    The purpose of this function is to divide the pre-existing total
    by the next number.
    """
    
    # Dividing the total as a float by the following number
    # and returning the answer as a string
    division = str(float(total) / float(numbers[num_index+1]))
    return division

def operationEquals(value, num_index, sign_index, total):
    """(str, int, int, str) -> str
    The purpose of this function is to execute all
    operations inputted by the user and return an 
    answer.
    """
    
    # Implementing a try and except block to ensure that
    # the program doesn't crash due to user-end errors
    try: 
        # Sorting the signs and numbers from the input into
        # lists named signs and numbers
        value, signs, numbers = sortingLists(value)

    except:
        # Plays an error noise
        main.invalidInput()
        # Alerts the user that their input is invalid
        return "INVALID INPUT"

    # Implementing a Try and except block in order to ensure
    # there are no mathematical errors in the input
    try:
        
        # Completing the first step in calculating the total
        # by using the function 'initialOperation(num_index, sign_index, 
        # total, numbers, signs)'
        num_index, sign_index, total, numbers, signs = \
        initialOperation(num_index, sign_index, total, numbers, signs)
    

    except:
        
        # Plays an error noise
        main.invalidInput()

        # Alerts the user that their input is invalid
        return "INVALID INPUT"

    # Setting the condition for the loop to 'True'.
    loopCondition = True

    # Starting a while loop to execute all operations
    while loopCondition:
        
        # Try and except block in order to ensure there are no 
        # mathematical errors in the input
        try:
            
            # Ensuring that there is a operation to be done and 
            # avoiding a 'index out of range' error.
            if num_index < (len(numbers)) and sign_index < (len(signs)):

                # If block for addition
                if signs[sign_index] == "+":
                    total = operationAdd(total, num_index, numbers)

                # Elif block for subtraction
                elif signs[sign_index] == "–":
                    total = operationSubtract(total, num_index, numbers)

                # Elif block for multiplication
                elif signs[sign_index] == "×":
                    total = operationMultiply(total, num_index, numbers)

                # Elif block for multiplication
                elif signs[sign_index] == "÷":
                    total = operationDivide(total, num_index, numbers)

            # Updating the accumulators
            num_index += 1
            sign_index += 1            

            # Checking if all operations are done and the grand total
            # is ready to be returned
            if num_index > (len(numbers)-1) and sign_index > (len(signs)-1):
                
                # Removing the decimal points from the answer
                # if its an integer
                if total[-2:] == ".0":
                
                    # Indexing a new total without the decimal
                    total = total[:-2]

                # Returning the answer
                return str(total)
         
        except:
            
            # Plays an error noise
            main.invalidInput()
            
            # Alerts the user that their input is invalid
            return "INVALID INPUT"