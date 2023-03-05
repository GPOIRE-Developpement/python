from math import * # importation du module math
import pygame # importation du module pygame | python -m pip install -U pygame==2.1.3 --user
import random # importation du module random

pygame.init() # initialisation du module pygame

window_resolution = (1100, 600) # définition de la dimension de la fenêtre
background_color = (255, 255, 255) # définition de la couleur de fond de la fenêtre
line_color = (0, 0, 0) # définition de la couleur de la ligne de base
cercle = False # Est ce que vous souhaitez voir les cercles de la génération du tracé ?
cercle_color = (255, 0, 0) # définition de la couleur des cercles de visualisation
size_depla = 100 # définition de la taille de chaque segment du tracé principal

pygame.display.set_caption("Sujet 9") # définition du titre de la fenêtre

window_surface = pygame.display.set_mode(window_resolution) # application de la taille de la fenêtre
window_surface.fill(background_color) # application de la couleur de fond 

segment_1 = [] # définition de la variable utilisé pour trouver les moitiers de segment
segment_2 = [] # définition de la variable utilisé pour trouver les moitiers de segment

for i in range(1, 11): # Boucle définissant le nombre de segment principal
    if(len(segment_1) == 0): # Condition si le segment est le premier
        x_depart = 50 # définition de la coordonnée x de départ du segment
        y_depart = 300 # définition de la coordonnée y de départ du segment
        y = y_depart+random.randint(-size_depla, size_depla) # définition de la coordonnée y du segment de manière aléatoire

        # Création du segment grace aux coordonnées de départ et à la coordonnée y pour définir la coordonnée x
        pygame.draw.line(window_surface, line_color, [x_depart, y_depart], [x_depart+sqrt(size_depla**2-(y_depart-y)**2), y], 2) 
        if cercle: # Condition si on veut voir le cercle
            pygame.draw.circle(window_surface, cercle_color, [x_depart, y_depart], size_depla, 2) # Création du cercle pour facilité la compréhension de la création du segment précédent

        segment_1.append([[x_depart, y_depart], [x_depart+sqrt(size_depla**2-(y_depart-y)**2), y]]) # Sauvegarde des coordonnées du segment
    else:
        x_depart = segment_1[len(segment_1)-1][1][0] # définition de la coordonnée x au coordonnée x du segment précédent
        y_depart = segment_1[len(segment_1)-1][1][1] # définition de la coordonnée y au coordonnée y du segment précédent
        y = y_depart+random.randint(-size_depla, size_depla) # définition de la coordonnée y du segment de manière aléatoire

        # Création du segment grace aux coordonnées de départ et à la coordonnée y pour définir la coordonnée x
        pygame.draw.line(window_surface, line_color, [x_depart, y_depart], [x_depart+sqrt(size_depla**2-(y_depart-y)**2), y], 2)
        if cercle: # Condition si on veut voir le cercle
            pygame.draw.circle(window_surface, cercle_color, [x_depart, y_depart], size_depla, 2) # Création du cercle pour facilité la compréhension de la création du segment précédent

        segment_1.append([[x_depart, y_depart], [x_depart+sqrt(size_depla**2-(y_depart-y)**2), y]]) # Sauvegarde des coordonnées du segment

for rep in range(1, 20): # Boucle définissant le nombre de segment visible (si l'application ne répond plus, réduire le premier le second nombre)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # Définition de la couleur du segment
    if(rep % 2 != 0): # Condition si la répétion est impaire
        tableau = segment_1 # Définition de la variable tableau à segment_1

        x_dep = tableau[0][0][0] # Recherche de la coordonnée x de départ
        y_dep = tableau[0][0][1] # Recherche de la coordonnée y de départ
        x = (tableau[0][0][0]+tableau[0][1][0])/2 # Recherche de la moitier du premier segment
        y = (tableau[0][0][1]+tableau[0][1][1])/2 # Recherche de la moitier du premier segment

        pygame.draw.line(window_surface, color, [x_dep, y_dep], [x, y], 2) # Tracé du segment de départ

        segment_2.append([[x_dep, y_dep], [x, y]]) # Ajouter les coordonnées du premier segment dans le tableau segment_2

        for i in range(1, len(tableau)): # Boucle sur le nombre de segment enregistré dans la variable tableau

            x_dep = (tableau[i-1][0][0]+tableau[i-1][1][0])/2 # Trouver la coordonnée x de départ du segment en fonction du tracé précédent
            y_dep = (tableau[i-1][0][1]+tableau[i-1][1][1])/2 # Trouver la coordonnée y de départ du segment en fonction du tracé précédent
            x = (tableau[i][0][0]+tableau[i][1][0])/2 # Trouver la coordonnée x d'arrivé du segment en fonction du segment précédent
            y = (tableau[i][0][1]+tableau[i][1][1])/2 # Trouver la coordonnée y d'arrivé du segment en fonction du segment précédent

            pygame.draw.line(window_surface, color, [x_dep, y_dep], [x, y], 2) # Tracer le segment en fonction des coordonnées précédentes

            segment_2.append([[x_dep, y_dep], [x, y]]) # Sauvegarder les coordonnées du segment
        
        x_dep = (tableau[len(tableau)-1][0][0]+tableau[len(tableau)-1][1][0])/2 # Recherche de la coordonnée x départ du dernier segment
        y_dep = (tableau[len(tableau)-1][0][1]+tableau[len(tableau)-1][1][1])/2 # Recherche de la coordonnée y départ du dernier segment
        x = tableau[len(tableau)-1][1][0] # Recherche de la coordonnée x d'arrivé du dernier segment
        y = tableau[len(tableau)-1][1][1] # Recherche de la coordonnée y d'arrivé du dernier segment

        pygame.draw.line(window_surface, color, [x_dep, y_dep], [x, y], 2) # Tracer le dernier segment

        segment_2.append([[x_dep, y_dep], [x, y]]) # Sauvegarde des coordonnées du dernier segment

        segment_1 = [] # Réinitialisation de la variable segment_1 à un tableau vide
    else: # Condition si la répétition est paire
        tableau = segment_2 # Définition de la variable tableau à segment_2

        x_dep = tableau[0][0][0] # Recherche de la coordonnée x de départ
        y_dep = tableau[0][0][1] # Recherche de la coordonnée y de départ
        x = (tableau[0][0][0]+tableau[0][1][0])/2 # Recherche de la moitier du premier segment
        y = (tableau[0][0][1]+tableau[0][1][1])/2 # Recherche de la moitier du premier segment

        pygame.draw.line(window_surface, color, [x_dep, y_dep], [x, y], 2) # Tracé du segment de départ

        segment_1.append([[x_dep, y_dep], [x, y]]) # Ajouter les coordonnées du premier segment dans le tableau segment_1

        for i in range(1, len(tableau)): # Boucle sur le nombre de segment enregistré dans la variable tableau

            x_dep = (tableau[i-1][0][0]+tableau[i-1][1][0])/2 # Trouver la coordonnée x de départ du segment en fonction du tracé précédent
            y_dep = (tableau[i-1][0][1]+tableau[i-1][1][1])/2 # Trouver la coordonnée y de départ du segment en fonction du tracé précédent
            x = (tableau[i][0][0]+tableau[i][1][0])/2 # Trouver la coordonnée x d'arrivé du segment en fonction du segment précédent
            y = (tableau[i][0][1]+tableau[i][1][1])/2 # Trouver la coordonnée y d'arrivé du segment en fonction du segment précédent

            pygame.draw.line(window_surface, color, [x_dep, y_dep], [x, y], 2) # Tracer le segment en fonction des coordonnées précédentes

            segment_1.append([[x_dep, y_dep], [x, y]]) # Sauvegarder les coordonnées du segment
        
        x_dep = (tableau[len(tableau)-1][0][0]+tableau[len(tableau)-1][1][0])/2 # Recherche de la coordonnée x départ du dernier segment
        y_dep = (tableau[len(tableau)-1][0][1]+tableau[len(tableau)-1][1][1])/2 # Recherche de la coordonnée y départ du dernier segment
        x = tableau[len(tableau)-1][1][0] # Recherche de la coordonnée x d'arrivé du dernier segment
        y = tableau[len(tableau)-1][1][1] # Recherche de la coordonnée y d'arrivé du dernier segment

        pygame.draw.line(window_surface, color, [x_dep, y_dep], [x, y], 2) # Tracer le dernier segment

        segment_1.append([[x_dep, y_dep], [x, y]]) # Sauvegarde des coordonnées du dernier segment

        segment_2 = [] # Réinitialisation de la variable segment_2 à un tableau vide

pygame.display.flip() # Mise à jour de l'affichage en fonction des tracers précédants

launched = True # Définition de la variable launched à True 

while launched: # Tant que launched est égal à True
    for event in pygame.event.get(): # Boucle sur les évènements du module PyGame
        if event.type == pygame.QUIT: # Condition si le type d'évènement est pygame.QUIT
            launched = False # Eteindre le programme python
