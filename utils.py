#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


# In[ ]:


" Cette fonction permet de calculer le nombre de voisins en prenant en entrée une matrice composée de 0 et 1 "


def iteration_jeu(Z):
     forme = len(Z), len(Z[0])
     N = calcul_nb_voisins(Z)
     for x in range(1, forme[0]-1):
        for y in range(1, forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
                
                
     return Z


# In[ ]:


"Cette fonction permet de faire une simulation d'un tour du jeu pour une liste Z ""
 
"elle affiche notamment 0 en cas de mort et 1 en cas de naissance."


def iteration_jeu(Z):
     forme = len(Z), len(Z[0])
     N = calcul_nb_voisins(Z)
     for x in range(1, forme[0]-1):
        for y in range(1, forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
                
                
     return Z


# In[ ]:


" Cette fonction permet d'afficher les étapes du jeu de 0 à 9 itérations "


plt.figure(figsize=(20,10))

for i in range (0, 10):
        plt.subplot(2,5,i+1)
        Z=np.array(Z)          " passage à la forme array "
        plt.imshow(Z)
        Z=iteration_jeu(Z)
        plt.title('Itération' + str(i))


# In[ ]:


" Cette fonction prend en entrée une matrice initiale Z_in et un nombre d'itérations nb_iter 
" elle sort une matrice (de même taille que Z_in) décrivant l'état du jeu de la vie après nb_iter itérations "


def jeu_np(Z_in, nb_iter):
    
    for i in range(1, nb_iter+1):
        
        Z_in = iteration_jeu_np(Z_in)
        
    return(Z_in)


# In[ ]:


" Cette fonction permet d'afficher un film (avec la commande animation.FuncAnimation de matplotlib)
" ce qui représente les itérations du jeu de la vie quand on initialise avec la matrice Z_huge "


def mon_film(Z_in, nb_iter):
    
    figure = plt.imshow(Z_in)
    
    def anim(nb_iter):
        figure.set_data(jeu_np(np.array(Z_in), nb_iter))
        return figure
    
    result = animation.FuncAnimation(plt.figure(), anim, frames=nb_iter)
    return result


get_ipython().run_line_magic('matplotlib', 'notebook')
mon_film(Z_huge, 100)

