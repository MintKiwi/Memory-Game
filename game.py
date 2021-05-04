#Author:Shibo Chen
#Date:2021.4.21
#Course&Projec:CS5003-Project 11: Final Project
#Link:https://drive.google.com/file/d/1cflGzFptmon37SHUpBFT9Pk6Pd4KVY4X/view?usp=sharing
import graphicsPlus as gr
import random
import time
#create a list of distinct numbers
numbers=[x for x in range(1,22)]
#create matches
matches=numbers+numbers
#shuffle the mathches list
random.shuffle(matches)

#count the number of each two clicks
count=0
#store the number shown on each two cards for comparison
num_list=[]
#count the steps of comparisons
count_step=0
#store the text objects for each two clicks once the numbers does not match
text_list=[]
#store keys from the card_dict that have the same value
card_list=[]

#define a set to count the number of matched pairs
num_set=set()
#define a function to draw cards and exit button
def init_card(win):
    cards=[]
    #create Rectangle objects for cards and exit button
    for i in range(6):
        for j in range(7):
            card=gr.Rectangle(gr.Point(60+100*j,50+120*i),gr.Point(140+100*j,150+120*i))
            cards.append(card)
    
    exit=gr.Rectangle(gr.Point(600,10),gr.Point(650,30))
  
    #draw cards
    for card in cards:
        card.setFill("white")
        card.draw(win)
    
    #show text for exit button 
    exit.setFill("white")
    exit.draw(win)
    text = gr.Text(gr.Point(625, 20), "Exit")
    text.setFill("black")
    text.draw(win)
    return cards,exit
  
#check whether it is clicked in the rectangle
def in_card(point, card):
    #points on the upper left
    ul = card.getP1()   
    #points on the lower right
    lr = card.getP2()  

    return ul.getX()<point.getX()<lr.getX() and ul.getY()<point.getY()<lr.getY()

#define a function to return center point of the card
def center_card(point,card):
    #points on the upper left
    xul,yul = card.getP1().getX(),card.getP1().getY()
    #points on the lower right
    xlr,ylr = card.getP2().getX(),card.getP2().getY()
    #x_coordinate of the central point of the current card
    x_center=(xul+xlr)/2    
    #y_coordinate of the central point of the current card
    y_center=(yul+ylr)/2    

    return x_center,y_center

#define a function to get keys that have the same value
def getKey(val,l):
    global card_list
    for key, value in l.items():
        if val == value:
            card_list.append(key)
    return card_list

# define a function to draw thumbs recursively
def thumbStack(x,y,scale,win):
    #wrist:rectangle objects
    wrist=gr.Rectangle(gr.Point(x+60*scale,y+105*scale),gr.Point(x+120*scale,y+215*scale))
    points = [ gr.Point( x + 120*scale, y + 125*scale ),
                gr.Point( x + 142*scale, y + 115*scale ),
                gr.Point( x + 183*scale, y + 56 *scale ),
                gr.Point( x + 190*scale, y + 16*scale ),
                gr.Point( x + 210*scale, y + 16*scale ),
                gr.Point( x + 220*scale, y + 56*scale ),
                gr.Point( x + 204*scale, y + 105*scale ),
                gr.Point( x + 262*scale, y + 104*scale ),
                gr.Point( x + 259*scale, y + 124*scale ),
                gr.Point( x + 245*scale, y + 126*scale ),
                gr.Point( x + 259*scale, y + 124*scale ),
                gr.Point( x + 258*scale, y + 144*scale ),
                gr.Point( x + 244*scale, y + 144*scale ),
                gr.Point( x + 258*scale, y + 144*scale ),
                gr.Point( x + 256*scale, y + 164*scale ),
                gr.Point( x + 243*scale, y + 164*scale ),
                gr.Point( x + 256*scale, y + 164*scale ),
                gr.Point( x + 254*scale, y + 181*scale ),
                gr.Point( x + 241*scale, y + 179*scale ),
                gr.Point( x + 254*scale, y + 181*scale ),
                gr.Point( x + 251*scale, y + 204*scale ),
                gr.Point( x + 120*scale, y + 195*scale ),
                gr.Point( x + 120*scale, y + 125*scale )]
    #thumb:polygon objects
    thumb=gr.Polygon(points)
    #set color for both objects
    wrist.setFill("dodgerblue")
    thumb.setFill("goldenrod")
    #set the termination condition 
    if scale<0.4:
        return
    #draw wrist and thumb
    wrist.draw(win)
    thumb.draw(win)
    #call thumbStack recursively
    thumbStack(x,y+scale*200,scale*0.8,win)

#define a main function to run the game    
def main():
    global count,num_list,text_list,num_set,count_step,card_list
    #create a window,set autoflash to be true
    win = gr.GraphWin( 'Memory Game', 800, 800, True)
    #set the background color
    win.setBackground("black")

 
    #show up the instructions
    txt=gr.Text(gr.Point(250,20),"Find the two cards that match! Press exit to exit.")
    txt.setTextColor("green")
    txt.draw(win)
  
    #assign cards and exit button
    cards,exit=init_card( win)
    #make a dictionary for cards and matches list, so that each card has unique match number 
    card_num=dict(zip(cards,matches))
        

    while True:
        #record (x,y) coordinate for each click
        click=win.getMouse()

        #exit the game
        if in_card(click,exit):
            break
        #make the texts appear on the cards
        
        for card in cards:
            #return x,y of the center point of the picked card
            x,y=center_card(click,card)
            #create texts for the numbers
            text = gr.Text(gr.Point(x,y), "")
            #if the it is click in the card:
            if in_card(click,card) and count<2:
                
                num=card_num[card]
                
                #make the number appear 
                text.setText(str(num))
                text.setSize(25)
                #append the number to the numlist for comparison 
                num_list.append(num) 
                #append the card and the number to the text_list  
                
                text_list.append(text)
                
                #increase the count
                count+=1
               
                #if it is the second click ,draw the second text
                if len(text_list)==2:
                    text_list[1].draw(win)
                    
                #if it is the first click ,draw the first text       
                elif len(text_list)==1:
                    text_list[0].draw(win)
                
            
            #determine whether the pair match when it is the second click
            if count==2:
                #increase count_step by 1
                count_step+=1
                #if the pair match, restore the count,textlist,card_list and numlist for the next comparison
                if num_list[0]==num_list[1]:
                    # find the card that have the same value once the pair match
                    card_objects=getKey(num_list[0],card_num)
                    for card in card_objects:
                        #slow it down to see what is the number on the second card
                        time.sleep(0.1)
                        #change the color of the two matched card
                        card.setFill("black")
                    num_set.add(num_list[0])
                    count=0
                    num_list=[]
                    text_list=[]
                    card_list=[]
                    
                   
                   
                #if the pair does not match, erase the number,restore the count,textlist and numlist
            
                else:
                    count=0
                    num_list=[]
                    #slow it down to show up the second text
                    time.sleep(0.5)
                    text_list[0].setText("")
                    
                    text_list[1].setText("")
                   
                    text_list=[]
            #pop up the congratulation messages when all matches are found
            if len(num_set)==len(numbers):
                congrats="Congratulations,it takes "+str(count_step)+" steps to find all matches."
                text_end = gr.Text(gr.Point(400,80), congrats)
                text_end.setSize(20)
                text_end.setTextColor("orangered")
                text_end.setStyle("bold italic")
                #draw thumb recursively
                thumbStack(250,100,1,win)
                text_end.draw(win)
                
                break
         
                    
                
                 
    #close the window
    
    win.close()

if __name__ == "__main__":
    main()
 

        