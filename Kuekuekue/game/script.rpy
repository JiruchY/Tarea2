# You can place the script of your game in this file.

#Para Transicion
define dissolve = Dissolve(.2)
#Para Transicion

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image naho = "images/Nahos.png"
image feliz = "images/feliz.png"
image prad = "images/pradera.png"
image bla = "images/bg8.png"

# Declare characters used by this game.
define e = Character('Naho', color="#000088", )



# The game starts here.
label start:
    scene prad
    show naho 
    #Musica
    play music "images/ff.mp3" fadeout 1
    queue music "images/ff.mp3"
    #Musica
    e "\"Bienvenido.. ha pasado mucho tiempo\""
    show naho at left
    with dissolve
    #INTERACCION USUARIO
    $ nombre= renpy.input("\"Recuerdas tu nombre?\"")
    e "\"Es hora de que escojas un camino, [nombre]\""
    #USER INTERACTION
    hide naho
    #MENUS
    menu:
            with dissolve
            "\"Recordar..\"":
                jump choice_yes
                
            "...":
                jump choice_no
                
                label choice_yes:
                  $ menu_flag =True
                 #Transicion
                  scene prad 
                  with dissolve
                  scene bla
                  #Transicion
                  show naho at center
                  with dissolve
                  "\"Mira a mis ojos\""
                  stop music 
                  #MOVIE
                  
                  play movie "images/opening.avi"
                  #MOViE
                  "soiefj!"
                  stop movie
                  hide movie
                
                  jump choice_done
                  
                  label choice_no:
                  $ menu_flag = False
                  
                  "..."
                  show naho
                  e "Adios"
                  return
                  
                  
                  
                  label choice_done:
                      play music "images/ff.mp3"
                      e "\"Se que no deben vernos juntos...\""
                      e "\"Pero quiero que sepan que soy la unica en tus ojos\""
                      "Terminado"
                      #MENUS
    
     
