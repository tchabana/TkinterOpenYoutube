from tkinter import *
import webbrowser

def bouton():
    webbrowser.open_new("https://www.youtube.com/@ifntisokode-licenceinforma7120")

fenetre = Tk()


# personalisation de la fenetre

fenetre.title("IFNTI")
fenetre.geometry("620x720")
fenetre.minsize(300,300) # taille mini de la fenetre
fenetre.config(background='#2596be')
# insertion de logo
#fenetre.iconbitmap("/home/hafiz/python_projet/logo.ico")


# ajout de texte
texte_fenetre=Label(fenetre, text='BIENVENU SUR MOODLE IFNTI', font=("Goudy stout",40), bg="#be2596")
texte_fenetre.pack(expand=YES)
# ajout de bouton
bouton_star=Button(text="OUVRIR MOODLE",font=("Goudy stout",25), bg="#9925be" ,command=bouton)
bouton_star.pack()

# afficher
fenetre.mainloop()
