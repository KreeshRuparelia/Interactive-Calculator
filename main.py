# Importing all files / modules required for this file
from __future__ import division
import pygame
import datetime
import calculator_operations

# Initializing required PyGame assets
pygame.init()
pygame.mixer.init()

# Setting a title for the Calculator App Window
pygame.display.set_caption("Kreesh's Calculator!")

# Assigning the Calculator App's Dimensions
WIDTH, HEIGHT = 391.2, 787.2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting a FPS Constant in order to limit the 
# number of while loops per second
FPS = 60

# Assigning values to global variables
value = ""
num_index = 0
sign_index = 1
total = ""

# Assigning RGB Color values to constants 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def background():
    """() -> ()
    This function loads the image 'iPhone_Calculator_UI.png' as a background
    for the app.
    """

    # Imports the image
    BACKGROUND_IMAGE = pygame.image.load ('iPhone_Calculator_UI.png')
    
    # Specifies dimensions
    BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
    
    # Applies it to the screen
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND, (0, 0))
    
    # Updates the screen for all the changes made.
    pygame.display.update()

def time():
    """() -> str
    Using the datetime module, this function obtains the current time,
    and returns the time in a 'Hour: Minute' format.
    """
    # Obtaining the current time
    now = datetime.datetime.now()
    
    # Formatting the time in a 'Hour: Minute' format
    current_time = now.strftime("%H: %M")

    # Returning the current time
    return current_time

def clockTime():
    """() -> ()
    This function obtains the current time from the function 'time()'
    and uses it to provide a live real-time clock visible on the
    top left of the screen.
    """
    # Selecting a font and size, and writing the current time
    # using the funtion 'time()'
    font = pygame.font.Font('SFUIDisplay-Bold.ttf', 14)
    text = font.render(time(), True, WHITE, BLACK)
    
    # Setting dimensions wherein the text will be housed
    textRect = text.get_rect()
    textRect.center = (65, 41)
    
    # Implementing the text in the dimensions mention above
    WIN.blit(text, textRect)
    
    # Updates the screen for all the changes made.
    pygame.display.update()

def displayLength():
    """() -> str
    This function ensures that the data displayed on screen
    doesn't go off the phone screen
    """

    # Assigning infomration to the data that will be displayed
    display = value
    
    # Ensuring that the text doesn't overlap the phone's bezels
    if len(display) > 11 and display != "INVALID INPUT":
        display = "..." + value[-11:]

    return display
    
def currentValue():
    """() -> ()
    This functions is embedded in the function 
    'performOperation(posX, posY)' and is used to 
    display whatever is inputted by the user
    on screen.
    """
    
    display = displayLength()
    
    # Selecting a font and size, and displaying the
    # variable 'value' which will be available in 
    # the function 'performOperation(posX, posY)'
    font = pygame.font.Font('SFUIDisplay-Bold.ttf', 40)
    text = font.render(display, True, WHITE, BLACK)

    # Setting dimension wherein the text will be housed
    # and changing alignment
    textRect = text.get_rect()
    textRect.center = (195, 240)
    textRect.right = 340
    textRect.bottom = 275

    # Refreshing the background before implenting changes
    background()

    # Implementing the text in the dimensions specified above
    WIN.blit(text, textRect)

    # Updates the screen for all changes made.
    pygame.display.update()

# Assigning coordinate grid values for each button using 2D Lists
# Explanation: BUTTON_NAME [[X_POS_1, X_POS_2], [Y_POS_1, Y_POS_2]]

ALL_CLEAR = [[38, 105], [305, 372]]
SQUARED = [[120, 187], [305, 372]]
RANDOM = [[203, 270], [305, 372]]
DECIMAL = [[203, 270], [635, 702]]
DIVIDE = [[285, 352], [305, 372]]
MULTIPLY = [[285, 352], [387, 454]]
SUBTRACT = [[285, 352], [469, 536]]
ADD = [[285, 352], [551, 618]]
EQUALS_TO = [[285, 352], [635, 702]]
ONE = [[38, 105], [551, 618]]
TWO = [[120, 187], [551, 618]]
THREE = [[203, 270], [551, 618]]
FOUR = [[38, 105], [469, 536]]
FIVE = [[120, 187], [469, 536]]
SIX = [[203, 270], [469, 536]]
SEVEN = [[38, 105], [387, 454]]
EIGHT = [[120, 187], [387, 454]]
NINE = [[203, 270], [387, 454]]
ZERO = [[38, 187], [635, 702]]

def calculatorClick():
    """() -> ()
    The purpose of this function is to play a quick sound
    which will be heard when a button is pressed.
    """
    Calculator_Click = pygame.mixer.Sound("Calculator_Click.wav")
    pygame.mixer.Sound.play(Calculator_Click)

def invalidInput():
    """() -> ()
    The purpose of this function is to play a rapid noise
    which will alert the user that the selection is invalid.
    """
    Invalid_Input = pygame.mixer.Sound("Invalid_Input.wav")
    pygame.mixer.Sound.play(Invalid_Input)

def mouseButtonPress(posX, posY):
    """(float, float) ->
    The purpose of this function is to obtain the X and Y coordinates
    of the mouse click and compare them with the catalogoue of coordinates
    listed below in order to determine which button is pressed, and to 
    reply with the appropriate response. 
    """

    # Allows for changes to be made to the variable globally 
    # from the function
    global value
    
    # List of operations, used later to verify
    # if a button pressed is a operation
    operations = ["+", "–", "÷", "×"]

    # Verifies if the utton pressed is is: "AC"
    if posX >= ALL_CLEAR[0][0] and posX <= ALL_CLEAR[0][1] \
    and posY >= ALL_CLEAR[1][0] and posY <= ALL_CLEAR[1][1]:
        
        value = ""
    
    # Verifies if the button pressed is: "X^2"
    elif posX >= SQUARED[0][0] and posX <= SQUARED[0][1] \
    and posY >= SQUARED[1][0] and posY <= SQUARED[1][1]:
        
        value = calculator_operations.operationSquared(value)

    # Verifies if the button pressed is: "RANDOM":
    elif posX >= RANDOM[0][0] and posX <= RANDOM[0][1] \
    and posY >= RANDOM[1][0] and posY <= RANDOM[1][1]:
        
        value = calculator_operations.operationRandom(value)

    # Verifies if the button pressed is: "."
    elif posX >= DECIMAL[0][0] and posX <= DECIMAL[0][1] \
    and posY >= DECIMAL[1][0] and posY <= DECIMAL[1][1]:

        # Updates Value
        value += "."

    # Verifies if the button pressed is: "÷"
    elif posX >= DIVIDE[0][0] and posY <= DIVIDE[0][1] \
    and posY >= DIVIDE[1][0] and posY <= DIVIDE[1][1]:
        
        # Ensuring that the first thing typed isn't an operation
        if value == "":
            # Plays an error noise
            invalidInput()
            # Returns nothing to allow the user to try again
            return
        
        # Makes sure that only operation is typed and avoids
        # contradictions
        if value[len(value) - 1] in operations:
            value = value[0:-1]
    
        # Updates Value
        value += "÷"

    # Verifies if the button pressed is: "×"
    elif posX >= MULTIPLY[0][0] and posX <= MULTIPLY[0][1] \
    and posY >= MULTIPLY[1][0] and posY <= MULTIPLY[1][1]:

        # Ensuring that the first thing typed isn't an operation
        if value == "":
            # Plays an error noise
            invalidInput()
            # Returns nothing to allow the user to try again
            return
        
        # Makes sure that only operation is typed and avoids
        # contradictions
        elif value[len(value) - 1] in operations:
            value = value[0:-1]
    
        # Updates Value
        value += "×"

    # Verifies if the button pressed is: "-" 
    elif posX >= SUBTRACT[0][0] and posX <= SUBTRACT[0][1] \
    and posY >= SUBTRACT[1][0] and posY <= SUBTRACT[1][1]:
        
        # Ensuring that the first thing typed isn't an operation
        if value == "":
            # Plays an error noise
            invalidInput()
            # Returns nothing to allow the user to try again
            return

        # Makes sure that only operation is typed and avoids
        # contradictions
        elif value[len(value) - 1] in operations:
            value = value[0:-1]
    
        # Updates Value
        value += "–"

    # Verifies if the button pressed is: "+"
    elif posX >= ADD[0][0] and posX <= ADD[0][1] \
    and posY >= ADD[1][0] and posY <= ADD[1][1]:
        
        # Ensuring that the first thing typed isn't an operation
        if value == "":
            # Plays an error noise
            invalidInput()
            # Returns nothing to allow the user to try again
            return
        
        # Makes sure that only operation is typed and avoids
        # contradictions
        elif value[len(value) - 1] in operations:
            value = value[0:-1]
            
        # Updates Value
        value += "+"

    # Verifies if the button pressed is: "="
    elif posX >= EQUALS_TO[0][0] and posX <= EQUALS_TO[0][1] \
    and posY >= EQUALS_TO[1][0] and posY <= EQUALS_TO[1][1]:
        
        value = calculator_operations.operationEquals(value, \
        num_index, sign_index, total)

    # Verifies if the button pressed is: "1"
    elif posX >= ONE[0][0] and posX <= ONE[0][1] \
    and posY >= ONE[1][0] and posY <= ONE[1][1]:
            
        # Updates Value
        value += "1"
    
    # Verifies if the button pressed is: "2"
    elif posX >= TWO[0][0] and posX <= TWO[0][1] \
    and posY >= TWO[1][0] and posY <= TWO[1][1]:
            
        # Updates Value
        value += "2"

    # Verifies if the button pressed is: "3"
    elif posX >= THREE[0][0] and posX <= THREE[0][1] \
    and posY >= THREE[1][0] and posY <= THREE[1][1]:
            
        # Updates Value
        value += "3"

    # Verifies if the button pressed is: "4"
    elif posX >= FOUR[0][0] and posX <= FOUR[0][1] \
    and posY >= FOUR[1][0] and posY <= FOUR[1][1]:
            
        # Updates Value
        value += "4"

    # Verifies if the button pressed is: "5"
    elif posX >= FIVE[0][0] and posX <= FIVE[0][1] \
    and posY >= FIVE[1][0] and posY <= FIVE[1][1]:
            
        # Updates Value
        value += "5"
    
    # Verifies if the button pressed is: "6"
    elif posX >= SIX[0][0] and posX <= SIX[0][1] \
    and posY >= SIX[1][0] and posY <= SIX[1][1]:
            
        # Updates Value
        value += "6"

    # Verifies if the button pressed is: "7"
    elif posX >= SEVEN[0][0] and posX <= SEVEN[0][1] \
    and posY >= SEVEN[1][0] and posY <= SEVEN[1][1]:
            
        # Updates Value
        value += "7"

    # Verifies if the button pressed is: "8"
    elif posX >= EIGHT[0][0] and posX <= EIGHT[0][1] \
    and posY >= EIGHT[1][0] and posY <= EIGHT[1][1]:
            
        # Updates Value
        value += "8"
    
    # Verifies if the button pressed is: "9"
    elif posX >= NINE[0][0] and posX <= NINE[0][1] \
    and posY >= NINE[1][0] and posY <= NINE[1][1]:
    
        # Updates Value
        value += "9"
    
    # Verifies if the button pressed is: "0"
    elif posX >= ZERO[0][0] and posX <= ZERO[0][1] \
    and posY >= ZERO[1][0] and posY <= ZERO[1][1]:
    
        # Updates Value
        value += "0"

    else:

        # Plays an error noise
        invalidInput()
        # Returns nothing to allow the user to try again
        return

    # Playing the calculator click noise
    calculatorClick()
    
    # Updating the display on screen
    currentValue()

def main():
    """() -> ()
    """
    
    # Setting the variable 'loopsPerSecond' as a clock
    loopsPerSecond = pygame.time.Clock()
    
    # Setting the window for the app to stay open upon initial run
    window = True
    
    # Painting a background
    background()

    # While loop which maintains the app to stay operational
    while window:
        
        # Updates the live time of the app in the top left corner
        clockTime()
        
        # Assigns the clock 'loopsPerSecond' a tick speed of 60
        # ticks per second. This limits the refresh rate of the app
        # to 60 FPS to reduce strain on the processor. 
        loopsPerSecond.tick(FPS)
        
        # Checks for an event in the app
        for event in pygame.event.get():
            
            # Checks if the event was user closing the app
            if event.type == pygame.QUIT:
                
                # Sets the loop condition to false and terminates the app
                window = False
                pygame.quit()
        
            # Checks if the event was a mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
        
                # Obtains the mouse press coordinates
                posX, posY = pygame.mouse.get_pos()

                # Runs the function mouseButtonPress(posX, posY) which 
                # responds with the appropriate action. 
                mouseButtonPress(posX, posY)
    
# Runs only if the file is run and not imported
if __name__ == '__main__':
    
    # Runs the function 'main()' 
    main()