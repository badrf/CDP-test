# CDP-2018

[![Build Status](https://travis-ci.com/badrf/CDP-2018.svg?branch=master)](https://travis-ci.com/badrf/CDP-2018)

Releases
======================
Release finale : 0.3 - 07 Décembre 2018.   
Changelog : Troisième itération, la mise en place de la base de données permet un formulaire d'inscription et des formulaires de création de projets, d'issues, tâches et sprints  ainsi que leur modification.

Nous avons également mis en place des tests pour l'ajout d'un projet, ainsi qu'une page d'inscription distincte de la page d'accueil développeur.

Installation 
-------------
L'installation peut se faire simplement via la commande suivante :

docker-compose build

Execution
-------------------
L'exécution peut se faire simplement via la commande suivante :

docker-compose up

Anciennes releases
-------------------

La release précédente : 0.2 - 23 Novembre 2018.   
Une page html qui propose des formulaires de créations de projets et d'issues ainsi que de modifications d'issues pas encore fonctionnels.

La première release:  0.1 - 9 Novembre 2018.
Une page html simple proposant un formulaire basique de création de projet.

Backlog
======================
Echelle de difficulté : 1-5  
Echelle de priorité : Basse / Moyenne / Haute  
Nombre de sprints prévus : 3

| Numéro d'US | Description précise | Priorité | Difficulté | Sprint n° |
|----------|----------|----------|----------|----------|
| 1 | **En tant que** visiteur, **je souhaite** créer un compte développeur à l'aide d'un login simple (username/password) **afin de** gérer mes projets | Moyenne | 4 | 1 |
| 2 | **En tant que** visiteur, **je souhaite** pouvoir me connecter à l'aide des identifiants créés en issue n°1 **afin de** gérer mes projets | Moyenne | 2 | 1 |
| 3 | **En tant que** visiteur, **je souhaite** pouvoir me déconnecter **afin de** garantir ma sécurité | Basse | 1 | 1 |
| 4 | **En tant que** développeur, **je souhaite** pouvoir créer un projet via un formulaire simple (nom de projet/createur) **afin de** pouvoir le gérer | Haute | 3 | 1 |
| 5 | **En tant que** développeur, **je souhaite** pouvoir supprimer un projet en cas d'annulation ou d'abandon | Basse | 3 | 1 |
| 6 | **En tant que** développeur, **je souhaite** pouvoir consulter la liste des projets | Moyenne | 2 | 1 |
| 7 | **En tant que** développeur, **je souhaite** pouvoir inviter des développeurs à un projet **afin qu**'ils puissent intégrer l'équipe de développement | Moyenne | 3 | 3 |
| 8 | **En tant que** développeur, **je souhaite** pouvoir ajouter une issue a mon projet (sous la forme de champs id/description/priorité/difficulté/sprint) **afin de** synthétiser les besoins du projet et d'ajouter des informations sur ceux-ci | Haute | 3 | 2 |
| 9 | **En tant que** développeur, **je souhaite** pouvoir modifier une issue de mon projet **afin de** suivre les demandes du client | Haute | 3 | 2 |
| 10 | **En tant que** développeur, **je souhaite** pouvoir supprimer une issue de mon projet si elle n'est plus conforme aux attentes du client | Basse | 3 | 2 |
| 11 | **En tant que** développeur, **je souhaite** pouvoir accéder au backlog d'un projet afin de consulter la liste des issues | Haute | 2 | 2 |
| 12 | **En tant que** développeur, **je souhaite** pouvoir créer un sprint (numéro de sprint, liste de tâches, date de départ/de fin) à l'intérieur d'un projet **afin d'** organiser le travail de l'équipe de développement en tâches et dans le temps | Basse | 3 | 2 |
| 13 | **En tant que** développeur, **je souhaite** pouvoir consulter la liste des sprints d'un projet | Basse | 2 | 2 |
| 14 | **En tant que** développeur, **je souhaite** pouvoir retirer une tâche d'un sprint si elle n'est plus conforme aux attentes du client ou pour la reporter à un sprint ultérieur | Basse | 2 | 2 |
| 15 | **En tant que** développeur, **je souhaite** pouvoir ajouter une tâche à un sprint **afin de** planifier le travail de l'équipe | Basse | 2 | 2 |
| 16 | **En tant que** développeur, **je souhaite** pouvoir consulter les données d'une tâche (temps évalué en jours-homme, date, nature de la tâche, dépendances éventuelles à d'autres tâches, état de la tache) **afin de** l'effectuer | Basse | 2 | 3 |
| 17 | **En tant que** développeur, **je souhaite** pouvoir modifier les données d'une tâche (temps évalué en jours-homme, date, nature de la tâche, dépendances éventuelles à d'autres tâches, état de la tache) **afin de** les corriger si besoin | Basse | 3 | 3 |
| 18 | **En tant que** développeur, **je souhaite** pouvoir accéder à la liste des tâches d'un sprint | Basse | 2 | 3 |
| 19 | **En tant que** développeur, **je souhaite** pouvoir générer un burn down chart  **afin de** visualiser aisément si le projet respecte le temps imparti | Basse | 3 | 3 |
