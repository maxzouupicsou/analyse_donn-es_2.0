# analyse_donn-es_2.0
Prédiction du classement premier league de la prochaine saison 2024/2025 basé sur les performances des club sur la saison 2023/2024 jusqu'à présent.

Facteurs  pris en compte pour la prédiction du classement de la Premier League, ainsi que le système de pondération de points pour chaque facteur, avec une justification pour chaque choix :

1. **Total Points (20%)** :
    - **Justification** : Les points totaux sont un indicateur direct de la performance de l'équipe au cours de la saison, donc c'est le facteur le plus lourdement pondéré.
2. **Total Goals Difference (15%)** :
    - **Justification** : La différence de buts donne une idée claire de la force offensive et défensive, reflétant la capacité de l'équipe à marquer plus qu'elle n'encaisse.
3. **Total Expected Goals Difference (15%)** :
    - **Justification** : Le xGD prend en compte la qualité des opportunités de but créées et concédées, offrant une mesure plus nuancée que les buts réels seuls.
4. **Possession (10%)** :
    - **Justification** : La possession indique le contrôle du jeu, souvent lié à la domination d'une équipe sur ses adversaires.
5. **Performance Save% (10%)** :
    - **Justification** : Le pourcentage d'arrêts du gardien montre l'efficacité du dernier rempart de l'équipe, un aspect crucial de la défense.
6. **Clean Sheets (10%)** :
    - **Justification** : Les matchs sans encaisser de but révèlent la solidité défensive et la capacité du gardien à garder son but inviolé.
7. **Net Penalty Goals (5%)** :
    - **Justification** : Les penalties marqués moins les penalties manqués offrent des points supplémentaires, reflétant les performances sous pression.
8. **Tackles (5%)** :
    - **Justification** : Un nombre élevé de tacles réussis indique une forte activité défensive, essentielle pour stopper les attaques adverses.
9. **Interceptions (5%)** :
    - **Justification** : Les interceptions stoppent les phases de jeu adverses et initient des contre-attaques, un élément clé de la stratégie défensive.
10. **Challenges Won (5%)** :
    - **Justification** : Gagner des duels, surtout des duels défensifs, est essentiel pour maintenir la pression et la possession.
11. **Goals Against (-5%)** :
    - **Justification** : Les buts encaissés ont un impact négatif sur le score, car encaisser moins est essentiel pour gagner des matchs.

Cette pondération cherche à équilibrer les contributions des différents aspects du jeu, mettant l'accent sur les résultats directs (points et buts) tout en intégrant des mesures de performance sous-jacente (xG, défense, gardien) pour une prédiction plus holistique et équilibrée.

Voici le classement complet des équipes de la Premier League basé sur le score de prédiction étendu après avoir exécuté le script :

1. **Liverpool** - Score: 90.950
2. **Tottenham** - Score: 87.315
3. **Arsenal** - Score: 87.015
4. **Manchester City** - Score: 76.820
5. **Everton** - Score: 76.180
6. **Fulham** - Score: 74.765
7. **Manchester United** - Score: 73.670
8. **West Ham** - Score: 73.620
9. **Chelsea** - Score: 73.085
10. **Bournemouth** - Score: 72.475
11. **Newcastle United** - Score: 72.440
12. **Brentford** - Score: 71.530
13. **Wolverhampton Wanderers (Wolves)** - Score: 71.070
14. **Aston Villa** - Score: 70.595
15. **Brighton** - Score: 69.620
16. **Nottingham Forest** - Score: 68.135
17. **Crystal Palace** - Score: 67.595
18. **Luton Town** - Score: 59.590
19. **Sheffield United** - Score: 52.685
20. **Burnley** - Score: 51.830
