"""
Improve Your French Vocabulary - Animals
Version 1.0

This program allows the user to answer questions and access more 
information on French vocabulary.

It was created with Python 3.12 and Tkinter 8.6.
"""
import tkinter as tk
import tkinter.font


# Definitions


def update_scroll_region():
    """
    update_scroll_region updates the window to make sure
    the scrollbar works after the dynamic buttons are
    clicked
    """
    root.update()
    container.config(scrollregion=container.bbox("all"))

    
def arrange_grid(row_start, col, lst, location = None):
    """
    arrange_grid takes a list of labels or buttons and arranges
    them with the help of the grid() function in the row and column
    specified.
    
    params:
        row_start (int): the first row on which the elements of
                         list will pe positioned
        col (int): the column on which the elements of the list
                   will be positioned
        lst (list): the list of labels or buttons to be positioned
        location (anchor constant): an anchor constant defined in Tk
                        that will be passed to the sticky attribute
                        of grid()
    """
    for i in range(len(lst)):
      lst[i].grid(row = (row_start + i), column = col, sticky = location)



def change_incorrect(incorrect_button):
    """
    change_incorrect changes the color and text displayed on a button
    corresponding to an incorrect answer
    
    params:
        incorrect_button (tk.Button): the incorrect button whose color and
                                      text will be changed
    """
    incorrect_button.configure(bg = "red", fg = "black", text = "Incorrect")



def change_correct(correct_button):
    """
    change_correct changes the color and text displayed on a button
    corresponding to a correct answer
    
    params:
        correct_button (tk.Button): the correct button whose color and
                                    text will be changed
    """
    correct_button.configure(bg = "green", fg = "white", text = "Correct",
                           font = correct_font)


def create_quest_info_label(parent, new_txt):
    """
    create_quest_info_label creates a tk.Label used as title for
    questions and infos
    
    params:
        parent (tk widget): the master to which the label is attached
        new_txt (str): the title of the question or info
        
    return (tk.Label): returns a label with the question or info title
    """
    return tk.Label(parent, text = new_txt, font = quest_font)



def create_answer_label(parent, new_txt):
    """
    create_answer_label creates a tk.Label used to provide the answer
    choices to a question
    
    params:
        parent (tk widget): the master to which the label is attached
        new_txt (str): the answer choice to the question
        
    return (tk.Label): returns a label with the answer choice
    """
    return tk.Label(parent, text = new_txt, width = 20, anchor = tk.W)



def create_answer_button(parent):
    """
    create_answer_button creates a tk.Button corresponding to an answer
    choice to a question which is used to validate or invalidate the
    selected answer choice
    
    params:
        parent (tk widget): the master to which the button is attached
        
    return (tk.Button): returns a button (in)validating the answer choice
    """
    return tk.Button(parent, text="Verify",
                   width=14, bg = "aqua", fg="black")



def clicked(widget, new_text):
    """
    clicked configures a widget (button) upon being clicked and updates
    the scroll region to ensure the scrollbar works for the dynamic buttons
    
    params:
        widget (tk.Button): the widget (button) which will be configured
                            upon being clicked
        new_text (str): the new text that will be displayed on the button
                        after being clicked
    """
    widget.config(bg = "gold", fg = "black", text=new_text)
    update_scroll_region()



def create_explan_button(parent):
    """
    create_explan_button creates a tk.Button corresponding to an answer
    choice to a question which is used to validate or invalidate the
    selected answer choice
    
    params:
        parent (tk widget): the master to which the button is attached
        
    return (tk.Button): returns a button (in)validating the answer choice
    """
    return tk.Button(parent, text='Click for explanation!',
                    bg = "DodgerBlue", padx = 10, pady = 15, font = info_font)



def create_info_button(parent):
    """
    create_info_button creates a tk.Button which is used to show
    information on a certain topic when clicked.
    
    params:
        parent (tk widget): the master to which the button is attached
        
    return (tk.Button): returns a button with "INFO Click me!" written
                        on it
    """
    return tk.Button(parent, text='INFO\n\nClick me!',
                     bg = "salmon", padx = 30, pady = 30, font = info_font)


# start window

root = tk.Tk()

# create window title

root.title('French Vocabulary')

# set minimum size

root.minsize(550, 600)

# create canvas to enable scrolling

container = tk.Canvas(root)

# create frame in canvas to place widgets

widget_frame = tk.Frame(container)

# create scrollbar

vertical_scrollbar = tk.Scrollbar(root)


# configure canvas, frame, scrollbar

container.config(yscrollcommand=vertical_scrollbar.set)

vertical_scrollbar.config(orient=tk.VERTICAL, command=container.yview)

vertical_scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)

container.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)

container.create_window(0, 0, window=widget_frame, anchor=tk.NW)


# create row counter

row_count = 0


# FONTS

quest_font = tk.font.Font(family='Georgia',
        size=12, weight='bold')

correct_font = tk.font.Font(family='Times_New_Roman',
        size=9, weight='bold')

info_font = tk.font.Font(family='Georgia',
        size=10)



# title 1 - main title

title = tk.Label(
  widget_frame,
  text='Improve Your French Vocabulary',
  font=('Book_Antiqua 20 bold'),
  background='DarkBlue',
  foreground='white',
  padx = 8,
  pady = 8,

  relief = tk.RAISED,
  borderwidth = 5

)

title.grid(column = 0, columnspan = 2, padx = 30, pady = (30, 10))

row_count += 1


# title 2 - subtitle

title = tk.Label(
  widget_frame,
  text='Animals',
  font=('Book_Antiqua 18 bold'),
  background='DarkBlue',
  foreground='white',
  padx = 5,
  pady = 5,
  relief = tk.RAISED,
  borderwidth = 5
)

title.grid(column = 0, columnspan = 2, pady = (10, 20))

row_count += 1



# I.a. Question 1 - text

quest_text = '1. What is the singular of "animaux"?'
quest_1_label = create_quest_info_label(widget_frame, quest_text)


quest_1_label.grid(row = row_count, column = 0, columnspan = 2,
                   sticky=tk.N, pady = (25, 15))

row_count += 1

quest_1_answ_1 = create_answer_label(widget_frame, "a. animau")


quest_1_answ_2 = create_answer_label(widget_frame, "b. animou")


quest_1_answ_3 = create_answer_label(widget_frame, "c. animal")


quest_1_answ_4 = create_answer_label(widget_frame, "d. animeau")


quest_1_answ_lst = [quest_1_answ_1, quest_1_answ_2,
                    quest_1_answ_3, quest_1_answ_4]

arrange_grid(row_count, 0, quest_1_answ_lst, tk.E)


# I.b. Question 1 - buttons

quest_1_answ_b1 = create_answer_button(widget_frame)

quest_1_answ_b2 = create_answer_button(widget_frame)

quest_1_answ_b3 = create_answer_button(widget_frame)

quest_1_answ_b4 = create_answer_button(widget_frame)

quest_1_answ_b1.configure(command = lambda: change_incorrect(quest_1_answ_b1))

quest_1_answ_b2.configure(command = lambda: change_incorrect(quest_1_answ_b2))

quest_1_answ_b3.configure(command = lambda: change_correct(quest_1_answ_b3))

quest_1_answ_b4.configure(command = lambda: change_incorrect(quest_1_answ_b4))



quest_1_button_lst = [quest_1_answ_b1, quest_1_answ_b2,
                      quest_1_answ_b3, quest_1_answ_b4]

arrange_grid(row_count, 1, quest_1_button_lst, tk.W)

row_count += 4

# I.c. Question 1 - explanation

quest_1_new_text = "\
Most French nouns ending in -al in the singular\n\
end in -aux in the plural:\n\
amiral, amiraux\n\
animal, animaux\n\
capital, capitaux\n\
cheval, chevaux\n\
marsupial, marsupiaux\n\
minéral, minéraux\n\
total, totaux\n\
végétal, végétaux\n\
\n\
The same is true for the far greater category of\n\
masculine adjectives in -al:\n\
abdominal, abyssal, adjectival, adverbial,\n\
alluvial, amical, ancestral, anormal,\n\
anticlérical, antisocial ...\n\
\n\
Among the exceptions to this rule are:\n\
bal(s), carnaval(s), chacal(s),\nfestival(s), gavial(s), narval(s),\n\
récital(s), régal(s), serval(s).\n"

quest_1_expl_button = create_explan_button(widget_frame)

quest_1_expl_button.configure(command=lambda: clicked(quest_1_expl_button, quest_1_new_text),
                              padx = 20, pady = 20)

quest_1_expl_button.grid(column = 0, columnspan = 2, pady = 15)

row_count += 1




# II.a Info 1 - label

info_text_1 = '2. Animals'

info_1_label = create_quest_info_label(widget_frame, info_text_1)


info_1_label.grid(row = row_count, column = 0, columnspan = 2,
                   sticky=tk.N, pady = (25, 15))

row_count += 1


# II.b Info 1 - button

info_1_text = "\
insect = un insecte\n\
mollusk = un mollusque\n\
fish = un poisson\n\
amphibian = un amphibien\n\
reptile = un reptile\n\
bird = un oiseau\n\
mammal = un mammifère\n\
invertebrate = un invertébré\n\
vertebrate = un vertébré"

info_1_button = create_info_button(widget_frame)

info_1_button.configure(command=lambda: clicked(info_1_button, info_1_text))

info_1_button.grid(column = 0, columnspan = 2, pady = (10, 15))

row_count += 1




# III.a. Question 2 - text

quest_2_text = '3. How do you say "horse" in French?'

quest_2_label = create_quest_info_label(widget_frame, quest_2_text)


quest_2_label.grid(row = row_count, column = 0, columnspan = 2,
                   sticky=tk.N, pady = (25, 15))

row_count += 1

quest_2_answ_1 = create_answer_label(widget_frame, "a. chevreau")


quest_2_answ_2 = create_answer_label(widget_frame, "b. cheval")


quest_2_answ_3 = create_answer_label(widget_frame, "c. cheveu")


quest_2_answ_4 = create_answer_label(widget_frame, "d. chèvre")


quest_2_answ_lst = [quest_2_answ_1, quest_2_answ_2,
                    quest_2_answ_3, quest_2_answ_4]

arrange_grid(row_count, 0, quest_2_answ_lst, tk.E)


# III.b. Question 2 - buttons

quest_2_answ_b1 = create_answer_button(widget_frame)

quest_2_answ_b2 = create_answer_button(widget_frame)

quest_2_answ_b3 = create_answer_button(widget_frame)

quest_2_answ_b4 = create_answer_button(widget_frame)

quest_2_answ_b1.configure(command = lambda: change_incorrect(quest_2_answ_b1))

quest_2_answ_b2.configure(command = lambda: change_correct(quest_2_answ_b2))

quest_2_answ_b3.configure(command = lambda: change_incorrect(quest_2_answ_b3))

quest_2_answ_b4.configure(command = lambda: change_incorrect(quest_2_answ_b4))



quest_2_button_lst = [quest_2_answ_b1, quest_2_answ_b2,
                      quest_2_answ_b3, quest_2_answ_b4]

arrange_grid(row_count, 1, quest_2_button_lst, tk.W)

row_count += 4


# III.c. Question 2 - explanation

quest_2_new_text = "\
Cheval means horse.\n\
Cheveu means hair.\n\
Chèvre means goat.\n\
Chevreau means kid (young goat)."

quest_2_expl_button = create_explan_button(widget_frame)

quest_2_expl_button.configure(command=lambda: clicked(quest_2_expl_button, quest_2_new_text),
                              padx = 20, pady = 20)

quest_2_expl_button.grid(column = 0, columnspan = 2, pady = 15)

row_count += 1



# IV.a Info 2 - label

info_text_2 = '4. Horses'

info_2_label = create_quest_info_label(widget_frame, info_text_2)


info_2_label.grid(row = row_count, column = 0, columnspan = 2,
                   sticky=tk.N, pady = (25, 15))

row_count += 1


# IV.b Info 2 - button

info_2_text = "\
horse = un cheval\n\
mare = une jument\n\
stalion = un étalon\n\
colt = un poulain\n\
filly = une pouliche"

info_2_button = create_info_button(widget_frame)

info_2_button.configure(command=lambda: clicked(info_2_button, info_2_text))

info_2_button.grid(column = 0, columnspan = 2, pady = (10, 15))

row_count += 1



# V.a. Question 3 - text

quest_3_text = '5. A female duck is called a:'

quest_3_label = create_quest_info_label(widget_frame, quest_3_text)


quest_3_label.grid(row = row_count, column = 0, columnspan = 2,
                   sticky=tk.N, pady = (25, 15))

row_count += 1

quest_3_answ_1 = create_answer_label(widget_frame, "a. dinde")


quest_3_answ_2 = create_answer_label(widget_frame, "b. daine")


quest_3_answ_3 = create_answer_label(widget_frame, "c. oie")


quest_3_answ_4 = create_answer_label(widget_frame, "d. cane")


quest_3_answ_lst = [quest_3_answ_1, quest_3_answ_2,
                    quest_3_answ_3, quest_3_answ_4]

arrange_grid(row_count, 0, quest_3_answ_lst, tk.E)



# V.b. Question 3 - buttons

quest_3_answ_b1 = create_answer_button(widget_frame)

quest_3_answ_b2 = create_answer_button(widget_frame)

quest_3_answ_b3 = create_answer_button(widget_frame)

quest_3_answ_b4 = create_answer_button(widget_frame)

quest_3_answ_b1.configure(command = lambda: change_incorrect(quest_3_answ_b1))

quest_3_answ_b2.configure(command = lambda: change_incorrect(quest_3_answ_b2))

quest_3_answ_b3.configure(command = lambda: change_incorrect(quest_3_answ_b3))

quest_3_answ_b4.configure(command = lambda: change_correct(quest_3_answ_b4))



quest_3_button_lst = [quest_3_answ_b1, quest_3_answ_b2,
                      quest_3_answ_b3, quest_3_answ_b4]

arrange_grid(row_count, 1, quest_3_button_lst, tk.W)

row_count += 4


# V.c. Question 3 - explanation

quest_3_new_text = "\
Cane is a female duck.\n\
Dinde is a female turkey.\n\
Daine is a doe.\n\
Oie is a goose."

quest_3_expl_button = create_explan_button(widget_frame)

quest_3_expl_button.configure(command=lambda: clicked(quest_3_expl_button, quest_3_new_text),
                              padx = 20, pady = 20)

quest_3_expl_button.grid(column = 0, columnspan = 2, pady = 15)

row_count += 1




# VI.a Info 3 - label

info_text_3 = '6. Chickens, ducks and geese'

info_3_label = create_quest_info_label(widget_frame, info_text_3)


info_3_label.grid(row = row_count, column = 0, columnspan = 2,
                   sticky = tk.N, pady = (25, 15))

row_count += 1


# VI.b Info 3 - button

info_3_text = "\
rooster = un coq\n\
hen = une poule\n\
chick = un poussin\n\
\n\
drake = un canard\n\
(female) duck = une cane\n\
duckling = un caneton\n\
\n\
gander = un jars\n\
goose = une oie\n\
gosling = un oison"

info_3_button = create_info_button(widget_frame)

info_3_button.configure(command=lambda: clicked(info_3_button, info_3_text))

info_3_button.grid(column = 0, columnspan = 2, pady = (10, 15))

row_count += 1



# VII.a. Question 4 - text

quest_4_text = '7. The old name for fox (renard) was:'

quest_4_label = create_quest_info_label(widget_frame, quest_4_text)


quest_4_label.grid(row = row_count, column = 0, columnspan = 2,
                   sticky=tk.N, pady = (25, 15))

row_count += 1

quest_4_answ_1 = create_answer_label(widget_frame, "a. courlis")


quest_4_answ_2 = create_answer_label(widget_frame, "b. goupil")


quest_4_answ_3 = create_answer_label(widget_frame, "c. marcassin")


quest_4_answ_4 = create_answer_label(widget_frame, "d. hérisson")


quest_4_answ_lst = [quest_4_answ_1, quest_4_answ_2,
                    quest_4_answ_3, quest_4_answ_4]

arrange_grid(row_count, 0, quest_4_answ_lst, tk.E)



# VII.b. Question 4 - buttons

quest_4_answ_b1 = create_answer_button(widget_frame)

quest_4_answ_b2 = create_answer_button(widget_frame)

quest_4_answ_b3 = create_answer_button(widget_frame)

quest_4_answ_b4 = create_answer_button(widget_frame)

quest_4_answ_b1.configure(command = lambda: change_incorrect(quest_4_answ_b1))

quest_4_answ_b2.configure(command = lambda: change_correct(quest_4_answ_b2))

quest_4_answ_b3.configure(command = lambda: change_incorrect(quest_4_answ_b3))

quest_4_answ_b4.configure(command = lambda: change_incorrect(quest_4_answ_b4))



quest_4_button_lst = [quest_4_answ_b1, quest_4_answ_b2,
                      quest_4_answ_b3, quest_4_answ_b4]

arrange_grid(row_count, 1, quest_4_button_lst, tk.W)

row_count += 4


# VII.c. Question 4 - explanation

quest_4_new_text = "\
The old noun designating the fox was 'goupil'.\n\
This was replaced by 'renard' in Middle French, thanks to\n\
the popularity of Roman de Renart, a medieval cycle of\n\
allegoric tales featuring animals, and of its main character,\n\
Renart (Renard) the fox.\n\
\n\
Courlis is a migratory shorebird (curlew).\n\
Marcassin is a young wild boar.\n\
Hérisson is a hedgehog."

quest_4_expl_button = create_explan_button(widget_frame)

quest_4_expl_button.configure(command=lambda: clicked(quest_4_expl_button, quest_4_new_text),
                              padx = 20, pady = 20)

quest_4_expl_button.grid(column = 0, columnspan = 2, pady = 15)

row_count += 1



# VIII.a Info 4 - label

info_text_4 = '8. Canids and felines'

info_4_label = create_quest_info_label(widget_frame, info_text_4)


info_4_label.grid(row = row_count, column = 0, columnspan = 2,
                   sticky=tk.N, pady = (25, 15))

row_count += 1


# VIII.b Info 4 - button

info_4_text = "\
Canids = Canidés\n\
dog = un chien\n\
wolf = un loup\n\
fox = un renard\n\
coyote = un coyote\n\
jackal = un chacal\n\
\n\
Felines = Félins\n\
lion = un lion\n\
jaguar = un jaguar\n\
leopard = un léopard\n\
tiger = un tigre\n\
cheetah = un guépard\n\
lynx = un lynx\n\
cougar (puma) = un couguar (un puma)\n\
ocelot = un ocelot\n"

info_4_button = create_info_button(widget_frame)

info_4_button.configure(command=lambda: clicked(info_4_button, info_4_text))

info_4_button.grid(column = 0, columnspan = 2, pady = (10, 15))

row_count += 1



# DO NOT DELETE
update_scroll_region()


root.mainloop()



















