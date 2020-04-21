# TicTacToe_QLearning
Atelier 4: QLearning ALGORITHME

  •	La classe Game (game.py) représente l’environnement (partie de jeu TicTactoe) pour notre agent.
    o	Cette classe contient la méthode : playGame(self, playerFirst) qui simule le déroulement et l’échange entre l’agent et un joueur (soit l’être humain ou bien un objet Teacher), et vers la fin cette méthode va passer à notre agent un reward selon action choisi par ce dernier.
    o	La méthode getStateKey(board) va nous aider à représenter les états du jeu (STATE) sous forme d’une chaine de caractères (pour faciliter l’indexation au niveau du Q-TABLE)
    o	Les autres méthodes de cette classe sont juste pour aider la méthode playGame à déterminer la fin du jeu et pour afficher son état.
  •	Pour la classe QLearning (agent.py) qui représente notre agent, j’ai essayé d’ajouter :
    o	Un champ(attribue) Q pour stocker la table d’apprentissage sous forme d’un dictionnaire (key -> value), les keys sont les états du jeu (exemple : ‘XX—O-XO-‘) et les valeurs sont les valeur q associer pour chaque action, pour notre cas une action c’est l’index de case à cocher (exemple de valeurs pour une état : [0, 0, 0, 8.51, 0, -1.5, 0, 0, 0])
    o	Une méthode get_action(self, state) : pour retourner l’action adéquate (max des q) pour une état donnée prise par notre agent selon la table Q( si l’état n’est pas introduite au niveau de la table Q alors cette état va être insérer avec initialisation par des zéros dans la méthode update et un action aléatoire sera retourner)
    o	La méthode update(self, prev_state, new_state, prev_action, new_action, reward): cette méthode pour mettre à jour notre table d’apprentissage par la formule de Bellman introduite dans le  cours
  •	Pour la classe GameLearning (play.py) : elle contient deux méthodes pour définir le mode de jeu (soit le mode d’apprentissage ou bien un jeu adversaire contre l’agent)
    o	Vers la fin de fichier vous pouvez voir le code pour exécuter le projet et jouer avec la variable nombre épisodes pour définir combien de parties notre agent va jouer pendant la phase d’apprentissage.
    o	Aussi un plot sera affiché pour voir le nombre de parties notre agent à gagner, perdu pendant la phase d’apprentissage (essayer de diminuer la valeur Level pour l’objet teacher pour laisser l’agent gagne des parties plus)
  •	Pour augmenter l’intelligence de notre agent essayer d’augmenter le nombre d’épisode et aussi le level de l’objet Teacher.
