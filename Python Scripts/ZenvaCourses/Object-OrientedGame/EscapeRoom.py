'''
Build and escape room game
    room contains several objects
    player needs a code to escape(3 digit)
    objects provide clues of the code
player pieces together clues to get code and escape(5 objects)
    each item can be looked at, smelled, or touched
    each sense provides new information
    player discerns information based on interaction
'''
'''
Project Design
game will be text-based
    run in the terminal
    print prompts and capture user text responses
    run until player wins or loses(3 incorrect guesses) or quits
game components
    GameObject
        look
        smell
        touch
    Room
        has escape code
        objects
    Game
        keeps track of 1 room
        tracks number of attempts of the room
'''
'''
GameObject
    string name
    string appearance
    string feel
    string smell
        init
            look()
            touch()
            sniff()
'''
class GameObject:
    #Sets up an instance of GameObject with name, appearance, feel, and smell
    def __init__(self,name,appearance,feel,smell):
        self.name=name
        self.appearance=appearance
        self.feel=feel
        self.smell=smell

    #Returns a string describing object appearance
    def look(self):
        return f'You look at the {self.name}. {self.appearance}\n'

    #Returns a string desciribing object feel
    def touch(self):
        return f'You touch the {self.name}. {self.feel}\n'

    #Returns a string describing object smell
    def sniff(self):
        return f'You sniff the {self.name}. {self.smell}\n'
    
'''
Room
    Int escape_code
    [GameObject]game_objects
        init(int escape_code,[GameObject]game_objects)
        Bool check_code
        get_game_object_names()
'''
class Room:
    #escape_code=0
    #game_objects=[]
    #Our Room class has an escape code and a list of game objects as attributes/fields
    
    #initializer
    def __init__(self,escape_code,game_objects):
        self.escape_code=escape_code
        self.game_objects=game_objects

    #Returns whether the escape code matches the code entered by player
    def check_code(self,code):
        return self.escape_code==code
    
    #Returns a list with all the names of the objects we have in our room
    def get_game_object_names(self):
        names= []
        for object in self.game_objects:
            names.append(object.name)
        return names
    
'''
Game
    int attempts
    Room room
        init()
        [GameObject]create_objects()
        take_turn()
        String get_room_prompt()
        select_object(Int index)
        String get_object_interaction_string(String name)
        String interact_with_object(GameObject object,String interaction)
        Bool guess_code(int code)
'''

class Game:
    def __init__(self):
        #number of attempts the player has made on the escape code of the room
        self.attempts=0
        objects=self.create_objects()
        #instantiating our room object
        self.room=Room(731,objects)

    #Returns a list with all the objects we're going to have in our escape room
    def create_objects(self):
        return [
            GameObject(
                "Sweater",
                "It's a blue sweater that had the number 12 stitched on it.",
                "Someone has unstitched the second number, leaving only the 1.",
                "The sweater smells of laundry detergent."
            ),
            GameObject(
                "Chair",
                "It's a wooden chair with only 3 legs.",
                "Someone had deliberately snapped off one of the legs.",
                "It smells like old wood."
            ),
            GameObject(
                "Journal",
                "The final entry states that time should be hours, then minutes, then seconds(H-M-S).",
                "The cover is worn and several pages are missing.",
                "It smells like must leather."
            ),
            GameObject(
                "Bowl of soup",
                "It appears to be tomato soup.",
                "It has coold down to room temperature.",
                "You detect 7 different herbs and spices."
            ),
            GameObject(
                "Clock",
                "The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.",
                "The batter compartment is open and empty.",
                "It smells of plastic."
            )
        ]
    
    '''
    Prompt user to guess code or select object
        get user selection
            user response
                guess code
                    check code
                    if match
                        Win
                        End
                    elif doesn't match if guesses <3
                        try again
                        +1 on guesses
                    else
                        Lose
                        End
                select object
                    select object
                    prompt user to select an action
                    get action selection
                        which action?
                            look
                            touch
                            sniff
    '''
    
    #For each turn, we want to present the prompt to the player
    def take_turn(self):
        prompt=self.get_room_prompt()
        selection=int(input(prompt))
        if selection>=1 and selection <=5:
            self.select_object(selection-1)
            self.take_turn()
        else:
            is_code_correct=self.guess_code(selection)
            if is_code_correct:
                print("Congratulations, you win!")
            else:
                if self.attempts == 3:
                    print("Game over, you ran out of guesses. Better luck next time!")
                else:
                    print(f"Incorrect, you have used {self.attempts}/3 attempts.\n")
                    self.take_turn()
            #if self.attempts<=3 and selection== :
                #print("You've Escaped the Room!")
            #else:
                #print("You Lose")
    
    #Shows the option to enter the code or interact further with the objects in the room
    def get_room_prompt(self):
        prompt= "Enter the 3 digit lock code or choose an item to interact with:\n"
        names= self.room.get_game_object_names()
        index=1
        for name in names:
            prompt += f"{index}. {name}\n"
            index+=1
        return prompt
    
    #Selects the object chosen by the player and prompts them for further interaction
    def select_object(self, index):
        selected_object= self.room.game_objects[index]
        prompt=self.get_object_interaction_string(selected_object.name)
        interaction=input(prompt)
        clue=self.interact_with_object(selected_object,interaction)
        print(clue)
    
    #Displays message to get type of interaction with the selected object
    def get_object_interaction_string(self, name):
        return f"How do you want to interact with the {name}?\n1. Look\n2. Touch\n3. Smell\n"

    #Shows the interaction message to the player
    def interact_with_object(self,object,interaction):
        if interaction == '1':
            return object.look()
        elif interaction == '2':
            return object.touch()
        elif interaction == '3':
            return object.sniff()

    #Compares the code entered to the code of the room
    def guess_code(self, code):
        if self.room.check_code(code):
            return True
        else:
            #If the codes don't match, increases attempts variable by 1
            self.attempts +=1
            return False

#We're creating an object of the game class
#and calling on it's take_turn() method
game=Game()
game.take_turn()

class RoomTests:
    def __init__(self):
        self.room_1=Room(111,[
            GameObject(
                "Sweater",
                "It's a blue sweater that had the number 12 stitched on it.",
                "Someone has unstitched the second number, leaving only the 1.",
                "The sweater smells of laundry detergent."
            ),
            GameObject(
                "Chair",
                "It's a wooden chair with only 3 legs.",
                "Someone had deliberately snapped off one of the legs.",
                "It smells like old wood."
            )])
        self.room_2=Room(111,[])
        
    def test_check_code(self):
        print(self.room_1.check_code(111)==True)
        print(self.room_1.check_code(222)==False)
#tests=RoomTests()
#tests.test_check_code()
    def test_get_game_objects(self):
        print(self.room_1.game_objects)
        print(self.room_2.game_objects)
        print(self.room_1.get_game_object_names()==['Sweater','Chair'])
        print(self.room_2.get_game_object_names()==[])
#tests=RoomTests()
#tests.test_get_game_objects()