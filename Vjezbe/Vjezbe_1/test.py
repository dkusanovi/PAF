for i in y: # prolazimo kroz svaku komponentu u listi y
        if i < 0: 
            break # kada naidjemo na prvu komponentu od y koja je manja od nula, stajemo s brojanjem
        brojac = brojac + 1 # ovdje smo racunali koja je to komponenta po redu koja je manja od nula u y listi

    print("Domet je", x[brojac]) # ovdje smo rekli to da je redni broj y komponente kada je ona jednaka nula, da je taj isti redni broj u x listi domet tog hitca 
