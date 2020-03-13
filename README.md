# TP-1---JEU-DE-LA-VIE-GAME-OF-LIFE-13-03-2020

Projet - Développement Logiciel - HMMA238

Professeur : Joseph Salmon

Travail fait par SAYD Yassine - M1 MIND - 2019/2020


Dans un premier temps, j'ai créé un fichier HMMA238_TP_saydyassine.ipynb qui contient un notebook avec les réponses aux questions (à la fois code / questions mathématiques). 

Le jeu de la vie est un automate cellulaire mis au point par le mathématicien britannique John Horton Conway en 1970. Il constitue l'exemple le plus connu d'un automate cellulaire. Le "jeu" est en fait un jeu à zéro joueur, ce qui signifie que son évolution est déterminée par son état initial et ne nécessite aucune intervention de la part d'un humain. On interagit avec le jeu de la vie en créant une configuration initiale ; il ne reste plus alors qu'à observer son évolution. 
L'univers du jeu est initialement une grille orthogonale bidimensionnelle infinie de cellules carrées.
On supposera cependant que la grille est carrée et de taille finie pour éviter toute difficulté.
On supposera aussi que le pourtour de la grille est toujours inactif/mort.
Les cellules du jeu ne peuvent prendre qu'un état parmi l'un des deux états possibles : vivant (1) ou mort (0).

Le principe est le suivant : 
- Toute cellule morte ayant exactement 3 voisins vivants devient une cellule vivante ( naissance ).
- Toute cellule vivante avec 2 ou 3 voisins vivants reste vivante à la génération suivante ( équilibre ).
- Toute cellule vivante ayant 4 voisins vivants meurt à la génération suivante ( mort par étouffement ).
- Toute cellule vivante ayant 0 ou 1 voisin vivant décède à la génération suivante ( mort par isolement ).

Le travail a été fait en 2 parties : une implémentation sans numpy suivie d'une implémentation avec numpy.
