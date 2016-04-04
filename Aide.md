# Introduction #
Vous avez rencontrez un problème dans DamnVid? Quelque chose que vous ne pouvez faire fonctionner? C'est l'endroit où aller, avant de vous éclater la tête contre le clavier. Vous souhaitez rapporter un bug? Alors dirigez vous vers [Issues tab](http://code.google.com/p/damnvid/issues/list), ou utilisez la nouvelle fonction "sigaler un bug" dans l'onglet Aide de Damnvid.


# Installation #
## Windows ##
L’installation sous Windows est assez directe. DamnVid est empaqueté en utilisant un standard [NSIS](http://nsis.sourceforge.net/) installateur avec le [Modern User Interface 2 (MUI2)](http://nsis.sourceforge.net/Docs/Modern%20UI%202/Readme.html). Si vous ne pouvez le comprendre, cliquez sur Suivant jusqu’à ce que l’installation soit terminée.
**Sur Vista**, vous devez autoriser l'installateur pour qu'il puisse écrire des fichiers. Vista devrait vous le demander au moment de lancer l'installateur.
## Mac OS X ##
À faire
## Linux ##
À faire


# Lancer le programme #
## Windows ##
Sur Windows, l’installateur devrait vous permettre de lancer DamnVid à la fin de l’installation, si vous laissez cocher la boite "Lancer Damnvid".
Autrement, vous pouvez lancer DamnVid en utilisant une de ces méthodes :
  * Si vous avez créé un raccourci dans le menu Démarrer, cliquez sur Démarrer -> Tous les programmes -> DamnVid (ou quelque soit le nom que vous avez donné à l’entrée) -> DamnVid.
  * Pour lancer DamnVid directement depuis l’exécutable, ouvrez l’explorateur (Bouton Windows + E) and naviguez jusqu’au dossier d’installation (Par défaut, C:\Program Files\DamnVid). Ensuite double cliquez sur DamnVid.exe.
  * Vous pouvez créer un raccourci de DamnVid sur le bureau, en allant dans le dossier d’installation de DamnVid comme expliqué ci-dessus, puis d’un clique-droit sur DamnVid.exe sélectionnez "Envoyer vers -> Bureau (créer un raccourci)". Vous pouvez ensuite renommer ce raccourci et éventuellement le mettre dans la zone de lancement rapide.

# Structure principale de la fenêtre #
DamnVid est conçu en trois zones.
  * La plus large, en haut à gauche, est la liste où l’on ajoute les vidéos.
  * Les boutons sur la droite sont les boutons d’action. Ils permettent d’ajouter, déplacer, renommer et supprimer des vidéos. Le bouton en bas, vous permet de lancer la conversion des vidéos dans la liste, ce qui n’empêche pas d’agir sur les vidéos toujours en attente.
  * En dessous de la liste se trouve la barre de progression, qui montre l’avancée de la conversion en cours. Sur la droite de cette barre, se trouve le bouton "Stop", annulant la conversion en cours.
Au dessus de la fenêtre on trouve la barre de menu, qui permet de faire les même actions que mentionné précédemment, ainsi que bien d’autres chose comme vérifier la présence de mise à jours, afficher l’aide, changer les préférences de DamnVid, terminer le programme ou encore signaler un bug.
### Note ###
> Vous pouvez aussi faire un clique-droit sur la liste, ce qui vous permettra de faire certaines actions sur des vidéos sélectionnées. Si vous n’avez sélectionné aucune vidéo, faire un clique-droit vous permettra d’ajouter d’autres vidéos.

# Préférences #
Les preferences de DamnVid sont accessible dans la barre de menu de DamnVid. Cliquez sur "DamnVid", puis sur "préférences".

![http://damnvid.googlecode.com/files/preferences.png](http://damnvid.googlecode.com/files/preferences.png)

Depuis cette boîte de dialogue vous pouvez affiner les paramètres de DamnVid. Ils sont divisés en 3 parties :
  * Préférences vidéo. Elles permettent de contrôler plusieurs aspects visuels de la vidéo convertie.
  * Préférences audio. Elles permettent de  contrôler plusieurs aspects auditifs de la vidéo convertie.
  * Préférences diverses. Elles vous permettent de régler de multiples choses (comme l’apparition du splashcreen).
## Préférences vidéo ##
  * **Codec**: C’est le codec de la vidéo qui servira à encoder le flux de vidéo. Le changer affectera la qualité et la compatibilité de la vidéo. Par défaut : **MPEG-4**. Recommandé : **MPEG-4**.
  * **Images par seconde**: C’est le nombre d’images par seconde. Une valeur plus grande rend la vidéo plus fluide, mais rend le fichier plus important. Par défaut : **30**. Recommandé : **24 à 40** (l’œil humain perçoit 24 ou 25 images par seconde).
  * **Débit**: c'est le flux de donnée, le débit exprimé en kbps ou kilo bits par seconde. C’est aussi l’espace alloué par fragment de la vidéo. Ainsi de plus grandes valeurs augmentent la qualité, mais rend le fichier plus important. Par défaut : **768k**. Recommandé : **512k à 1024k**. Note: Si la qualité de la vidéo source est mauvaise, il est inutile d’augmenter trop le débit. La qualité de la vidéo finale ne surpassera jamais celle de la source.
  * **Débit minimum**: Puisque le débit est variable, c’est la limite inférieure du débit. Elle est déterminée automatiquement si rien n’est spécifié, c’est pour ça qu’il est préférable de la laisser comme telle. Par défaut : **(Par défaut)**. Recommandé : **(Par défaut)**.
  * **Débit maximum**: Puisque le débit est variable, c’est la limite supérieure du débit. Elle est déterminée automatiquement si rien n’est spécifié, c’est pour ça qu’il est préférable de la laisser comme telle. Par défaut : **(Par défaut)**. Recommandé : **(Par défaut)**.
  * **Mémoire Tampon**: C’est la mémoire tampon de la vidéo. Il est recommandé de ne pas y toucher. Par défaut : **(Par défaut)**. Recommandé : **(Par défaut)**.
  * **Passage**: C’est le nombre de passage qui sera fait sur le flux de vidéo. C’est soit 1, soit 2. Puisque 2 passages rendent la conversion bien plus longue, et qu’un seul passage est dans la plupart des cas largement suffisant, il est recommandé de laisser ce nombre à 1. Par défaut : **(Par défaut)**. Recommandé : **(Par défaut)** ou **1 passage** (c'est pareil).
  * **Taille de groupe d'image**: Pour les codecs de vidéo qui utilise une taille de groupe d’image (Group Of Picture, GOP, en anglais), comme MPEG, ceci sert à paramétrer la distance entre deux images. Pour plus d’information (en anglais) [here](http://en.wikipedia.org/wiki/Group_of_pictures). Par défaut : **(Par défaut)**. Recommandé : **(Par défaut)**. (Peut beaucoup varier).
## Préférences audio ##
  * **Codec**: C’est le codec de la vidéo qui servira à encoder le flux audio. Le changer affectera la qualité et la compatibilité de la vidéo. Par défaut : **MP3**. Recommandé : **MP3**, **MP2**.
  * **Volume**: Utilisé pour modifier le volume de la vidéo finale. C’est un pourcentage, ce qui veut dire que 100 ne changera rien. Par défaut : **100%**. Recommandé : **100%**.
  * **Débit**: c'est le flux de donnée, le débit exprimé en kbps ou kilo bits par seconde. C’est aussi l’espace alloué par fragment d’audio. Ainsi de plus grandes valeurs augmentent la qualité, mais rend le fichier plus important. Par défaut : **128k**. Recommandé : **96k à 256k**. Note: Si la qualité de l’audio source est mauvaise, il est inutile d’augmenter trop le débit. La qualité de l’audio final ne surpassera jamais celle de la source.
  * **Échantillonnage**: C’est l’échantillonnage audio. Plus d’information (en anglais) [here](http://en.wikipedia.org/wiki/Sampling_rate). De plus grandes valeurs donnent une meilleure qualité, mais un fichier plus important. Par défaut : **44 100 Hz**. Recommandé : **22 050Hz à 48 000Hz**.
  * **Canaux**: C’est le nombre de canaux audio utilisés. Soit un (flux audio unique) ou deux (flux audio double, un pour le haut-parleur gauche et un pour celui de droite). Mais 2 canaux doubleront la taille du fichier audio. Par défaut : **1 (mono)**. Recommandé : **N’importe lequel**.
## Préférences diverses ##
  * **Activer la récursivité des dossier**: Quand vous déposez un dossier dans DamnVid, deux choses peuvent arriver:
    * Si cete option est **activée**, le logiciel scannera le répertoire et tous les fichiers seront ajoutés à la liste. Si le répertoire contient des sous-répertoires, tous seront ajoutés aussi.
    * Si cette option est **désactivée**, ajouter directement un répertoire à DamnVid ne fera absolument rien.
> Par défaut : **Activé**. Recommandé : **Activé**.
  * **Dossier par défaut**: C’est le dossier où toutes les vidéos seront enregistrées. Il est recommandé de le changer pour son répertoire préféré. Par défaut : **C:\Users\Username\Videos\DamnVid**. Recommandé : **N’importe quel répertoire**.
  * **Réduire dans la barre de tâche**: Vous permet de réduire DamnVid dans la barre de tâche plutôt que dans la barre centrale. Vous pouvez agrandir de nouveau DamnVid en cliquant une fois sur l’icône en bas à droite.
  * **Langue**: Vous permet de choisir entre Anglais et Français (pour l’instant) comme langue d’utilisation de DamnVid.
  * **Afficher le Splash screen au démarrage**: En cochant cette case vous choisissez si vous souhaitez ou pas voir apparaitre le Splash screen à chaque démarrage de DamnVid.
  * **M’avertir lorsque j’enlève une vidéo**: Vous permet de choisir si vous voulez être prévenu avant de retirer une ou toutes les vidéos de la liste.
  * **Fenêtre principale**: Vous permet de choisir si vous souhaitez que damnVid se souvienne de sa position et ses dimensions ou si vous voulez qu’il soit toujours recentré.
  * **Taille de l’historique de vidéo**: Vous permet de choisir le nombre de vidéos sauvegardées dans l’historique. Par défaut : **8**. Recommandé : **N’importe quoi entre 0 et 50**.
## Réinitialiser les configurations ##
En bas à gauche de la fenêtre de préférence se trouve un menu, qui contient 5 boutons, le dernier "Tout restaurer" permet de remettre toutes les configurations par défaut.

# Désinstallation #
## Windows ##
Tout comme installer, désinstaller est assez direct, sinon plus. Pour désinstaller DamnVid, il faut utiliser une des méthodes suivantes :
  * Ouvrez le menu démarrer -> Tous les programmes -> DamnVid, et cliquez sur "Désinstaller".
  * Si vous n’avez pas créé de raccourci dans le menu démarrer, ouvrez l’explorateur Windows, allez jusqu’au dossier d’installation de DamnVid comme décrit dans la section instalation. Puis double-cliquez sur "uninstaller.exe".
  * Vous pouvez aussi passez par le Panneau de configuration -> Programmes et fonctionnalités, puis cliquez sur DamnVid pour le désinstaller.
## Mac OS X ##
À faire
## Linux ##
À faire
### Note ###
> Le dossier de destination par défaut est un sous-dossier dans le répertoire d’installation de DamnVid. Si des vidéos sont dans ce répertoire, il ne sera pas supprimé par une désinstallation. Si une vidéos converties se trouve dans ce répertoire, vous devez la déplacer pour pouvoir supprimer au complet DamnVid et tout ses dossiers.