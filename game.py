#### SETTING OBJECTS FOR DRAWING ######
letter_x = """
 x   x
 x   x
  x x
   x
  x x
 x   x"""

letter_o = """
  ooo
 o   o
 o   o
 o   o
 o   o
  ooo"""
letter_blank = """





       """


def letter_to_list(letter):
    list =[]
    for item in letter.split("\n"):
        if len(item) < 7:
            item = item + ' '*(7-len(item))
        list.append(item)
    return list

list_x = letter_to_list(letter_x)
list_o = letter_to_list(letter_o)
list_blank = letter_to_list(letter_blank)

line_bottom_a = """_______|"""
line_bottom_b = """_______ """

dict_letter_list = {'X':list_x , 'O': list_o,'blank': list_blank}

class Boxes:
    """each box that is set for the TicTacToe game"""
    def __init__(self,int,bottom=False,right=False):
        self.int = int
        self.right = right ## needs a line drawn on the right
        self.bottom = bottom ## needs a line at the bottom
        self.bottom_b = False ## if False, then use a. If True, use b.
        self.letter_list = list_blank ## list
        self.final_box = []
        self.set_box()

    def set_bottom_b(self):
        self.bottom = True ## cannot be bottom B, without being Bottom
        self.right = False ## cannot have a right either
        self.bottom_b = True
        self.set_box()

    def set_letter(self,letter):
        self.letter_list = dict_letter_list[letter]
        self.set_box()

    def set_box(self):
        self.final_box = []
        if self.right:
            for i in range(len(self.letter_list)):
                self.final_box.append(self.letter_list[i] +'|')
        else:
            for i in range(len(self.letter_list)):
                self.final_box.append(self.letter_list[i])
        if self.bottom:
            if self.bottom_b:
                self.final_box.append(line_bottom_b)
            else:
                self.final_box.append(line_bottom_a)
        return

    def draw_box(self):
        for i in range(len(self.final_box)):
            print(self.final_box[i])

boxes_list =[]

boxes_list.append(Boxes(1,True,True))
boxes_list.append(Boxes(2,True,True))
box = Boxes(3,True,False)
box.set_bottom_b()
boxes_list.append(box)
boxes_list.append(Boxes(4,True,True))
boxes_list.append(Boxes(5,True,True))
box2 = Boxes(6)
box2.set_bottom_b()
boxes_list.append(box2)
boxes_list.append(Boxes(7,False,True))
boxes_list.append(Boxes(8,False,True))
boxes_list.append(Boxes(9,False,False))


def draw_all_boxes():
    print("""
        """)
    for i in range(8):
        print(' '*7 + boxes_list[0].final_box[i] + boxes_list[1].final_box[i] + boxes_list[2].final_box[i])
    for i in range(8):
        print(' '*7 + boxes_list[3].final_box[i] + boxes_list[4].final_box[i] + boxes_list[5].final_box[i])
    for i in range(7):
        print(' '*7 +boxes_list[6].final_box[i] + boxes_list[7].final_box[i] + boxes_list[8].final_box[i])
    print("""
        """)

class Outcomes:
    """each potential outcome of the match (see Journal pg.9 for mapping)"""
    def __init__(self,letter):
        self.name = letter
        self.X = False
        self.O = False
        self.count_allocated = 0 # count number used

    def set_player(self,player):
        if player == 'X':
            self.X = True
        elif player == 'O':
            self.O = True
        else:
            print('incorrect selection made, try again')
        self.count_allocated = self.count_allocated + 1
        #print('outcome  '+self.name + ' allocated ' + str(self.count_allocated))
        if self.count_allocated == 3:
            if self.X != self.O:
                return True ## This means the game is over, and this player won
        return False

dict_outcomes = dict()
dict_index_to_outcome = dict()
dict_allowable_plays = dict()

for each in ('A','B','C','D','E','F','G','H'):
    dict_outcomes[each] = Outcomes(each)

dict_index_to_outcome[1] = [dict_outcomes['A'],dict_outcomes['D'],dict_outcomes['F']]
dict_index_to_outcome[2] = [dict_outcomes['A'],dict_outcomes['G']]#,outcomes_dict['F']]
dict_index_to_outcome[3] = [dict_outcomes['A'],dict_outcomes['E'],dict_outcomes['H']]
dict_index_to_outcome[4] = [dict_outcomes['B'],dict_outcomes['F']]#,outcomes_dict['F']]
dict_index_to_outcome[5] = [dict_outcomes['B'],dict_outcomes['D'],dict_outcomes['E'],dict_outcomes['G']]
dict_index_to_outcome[6] = [dict_outcomes['B'],dict_outcomes['H']]#,outcomes_dict['F']]
dict_index_to_outcome[7] = [dict_outcomes['C'],dict_outcomes['E'],dict_outcomes['F']]
dict_index_to_outcome[8] = [dict_outcomes['C'],dict_outcomes['G']]#,outcomes_dict['F']]
dict_index_to_outcome[9] = [dict_outcomes['C'],dict_outcomes['D'],dict_outcomes['H']]

# set defaults for the game to be all indexes are allowable
for i in range(9):
    dict_allowable_plays[i+1] = True

def assign_play(int,player):
    dict_allowable_plays[int] = False
    boxes_list[int-1].set_letter(player)

    for outcome in dict_index_to_outcome[int]:
        if outcome.set_player(player) == True:
            return True
    return False

def check_allowable_play(int):
    return dict_allowable_plays.get(int,False)

################################## GAME START #################################
final_winner = False
play_count = 0
player1 = input("""Welcome to TIC TAC TOE !
Are you naughts, or crosses?
Please enter X or O """)

if player1 == "X":
    player2 = "O"
elif player1 == "O":
    player2 = "X"
else:
    player1 = "O"
    player2 = "X"

print("""Thank you! You are now referred to as Player """ + player1 +
"""
and your opponent will be Player """ + player2)
current_player = player1

while play_count < 9  and not final_winner :
    question = "PLAYER " + current_player + " please select an empty box, 1 - 9 : "
    choice = input(question)
    int_choice = int(choice)

    while not check_allowable_play(int_choice) :
        print('Invalid choice')
        choice = input(question)
        int_choice = int(choice)

    final_winner = assign_play(int_choice,current_player)
    draw_all_boxes()

    play_count = play_count + 1

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

if current_player == player1:
    current_player = player2
else:
    current_player = player1

if final_winner == False:
    print("""
    ==================== GAME OVER =============================

    ======================= A DRAW =============================""")
else:
    print("""
    ==================== GAME OVER =============================

    ================== PLAYER """ + current_player + """ WINS ! =========================""")
