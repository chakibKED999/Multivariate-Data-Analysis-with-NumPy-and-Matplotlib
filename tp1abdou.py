import numpy as np
import matplotlib.pyplot as plt



#question 1:

sports = ["H.Ball", "B.Ball", "Tennis", "Gym", "Natation", "F.Ball"]
villes = ["V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
          "V11","V12","V13","V14","V15","V16","V17","V18","V19","V20"]

donnees = [
    [1881.9, 96.8,  14.2, 25.2, 1135.5, 278.3],
    [3369.8, 96.8,  10.8, 51.6, 1331.7, 284.0],
    [4467.4, 138.2,  9.5, 34.2, 2346.1, 312.3],
    [1862.1, 83.2,   8.8, 27.6,  972.6, 203.4],
    [3499.8, 287.0, 11.5, 49.4, 2139.4, 358.0],
    [3903.2, 170.7,  6.3, 42.0, 1935.2, 292.9],
    [2620.7, 129.5,  4.2, 16.8, 1346.0, 131.8],
    [3678.4, 157.0,  6.0, 24.9, 1682.6, 194.2],
    [3840.5, 187.9, 10.2, 39.6, 1859.9, 449.1],
    [2170.2, 140.5, 11.7, 31.1, 1351.1, 256.5],
    [3920.4, 128.0,  7.2, 25.5, 1911.5,  64.1],
    [2599.6, 39.6,   5.5, 19.4, 1050.8, 172.5],
    [2828.5, 211.3,  9.9, 21.8, 1085.0, 209.0],
    [2498.7, 123.2,  7.4, 26.5, 1086.2, 153.5],
    [2685.1, 41.2,   2.3, 10.6,  812.5,  89.8],
    [2739.3, 100.7,  6.6, 22.0, 1270.4, 180.5],
    [1662.1, 81.1,  10.1, 19.1,  872.2, 123.3],
    [2469.9, 142.9, 15.5, 30.9, 1165.5, 335.5],
    [2350.7, 38.7,   2.4, 13.5, 1253.1, 170.0],
    [3177.7, 292.1,  8.0, 34.8, 1400.0, 358.9],
]

X  = np.array(donnees)
Xt = X.T

print("Taille de X  :", X.shape)
print("Taille de Xt :", Xt.shape)

# ---- Affichage de X ----
print("\n--- Matrice X (20x6) ---")
print(f"{'':>5}", end="")
for s in sports:
    print(f"{s:>10}", end="")
print()
for i in range(20):
    print(f"{villes[i]:>5}", end="")
    for val in X[i]:
        print(f"{val:>10.1f}", end="")
    print()

# ---- Affichage de Xt ----
print("\n--- Transposee Xt (6x20) ---")
print(f"{'':>10}", end="")
for v in villes:
    print(f"{v:>8}", end="")
print()
for j in range(6):
    print(f"{sports[j]:>10}", end="")
    for val in Xt[j]:
        print(f"{val:>8.1f}", end="")
    print()



# construction de la matrice de données X représentant
# les 20 villes (individus) et les 6 sports (variables),
# puis calcul de sa transposée Xt







#question 2:

individus = list(X)   
print('\n' * 5) 
print("\nQuestion 2:")
print("\nListe de tous les individus")
for i, ind in enumerate(individus):
    print(f"  {villes[i]} : {ind.tolist()}")



# extraction de la liste des individus (villes)
# sous forme de vecteurs pour faciliter leur manipulation.



#question 3:

print('\n' * 5) 
print("\nQuestion 3:")
print("\nToutes les variables extraites")
variables = {}
for j in range(6):
    variables[sports[j]] = X[:, j]

for nom, vecteur in variables.items():
    print(f"\n  Variable {nom} :")
    print(f"    {vecteur.tolist()}")



# sélection de 4 villes (V3, V11, V15, V19)
# pour effectuer une analyse comparative.





#question 4:

print('\n' * 5) 
print("\nQuestion 4:")

indices = [2, 10, 14, 18]
labels  = ["V3", "V11", "V15", "V19"]

X_sel = X[indices]

print("Individus V3, V11, V15, V19")
print(f"{'':>5}", end="")
for s in sports:
    print(f"{s:>10}", end="")
print()

for i, label in enumerate(labels):
    print(f"{label:>5}", end="")
    for val in X_sel[i]:
        print(f"{val:>10.1f}", end="")
    print()


# dans cette étape, un sous-ensemble d’individus (villes) est sélectionné à partir de la matrice de données initiale
# les villes V3, V11, V15 et V19 sont choisies afin de réaliser une analyse comparative ciblée
# cette sélection permet de simplifier l’étude tout en conservant des profils représentatifs pour mesurer les similitudes et différences entre comportements sportifs








#question 5:

print('\n' * 5) 
print("qst5")

from scipy.spatial.distance import euclidean
import numpy as np

n = len(X_sel)
distances = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        distances[i, j] = euclidean(X_sel[i], X_sel[j])

print(" Matrice des distances")
print(f"{'':>5}", end="")
for label in labels:
    print(f"{label:>10}", end="")
print()

for i, label1 in enumerate(labels):
    print(f"{label1:>5}", end="")
    for j in range(n):
        print(f"{distances[i, j]:>12.4f}", end="")
    print()



# calcul de la matrice des distances euclidiennes entre les villes sélectionnées
# cette distance permet de quantifier le degré de similarité entre deux villes selon leurs pratiques sportives
# une distance faible indique des profils sportifs proches, tandis qu’une distance élevée traduit des comportements différents
# cette matrice constitue une base essentielle pour l’analyse des relations entre individus





#question 6:


moy = np.mean(X, axis=0)
var = np.var(X, axis=0)
std = np.std(X, axis=0)

stats = np.round(np.array([moy, var, std]).T,4)
print('\n' * 5) 
print("\nQuestion 6:")
sports = ["H.Ball", "B.Ball", "Tennis", "Gym", "Natation", "F.Ball"]
print(f"\n{'Variable':>12}  {'Moyenne':>12}  {'Variance':>14}  {'Ecart-type':>12}")
print("-" * 56)
for j in range(6):
    print(f"{sports[j]:>12}  {stats[j,0]:>12.4f}  {stats[j,1]:>14.4f}  {stats[j,2]:>12.4f}")



# calcul des statistiques descriptives pour chaque sport : moyenne, variance et écart-type
# ces mesures permettent d’analyser la distribution des pratiques sportives :
# - la moyenne représente le niveau moyen de pratique
# - la variance mesure la dispersion des données
# - l’écart-type indique la variabilité autour de la moyenne
# cette étape permet d’évaluer l’homogénéité des comportements sportifs





#question 7:


ind_moy = moy
print('\n' * 5) 
print("\nQuestion 7:")
print("\nIndividu moyen :\n", ind_moy)


# construction de l’individu moyen en calculant la moyenne de chaque variable sportive
# cet individu représente une ville fictive typique dont les caractéristiques correspondent au comportement sportif global observé
# il sert de référence statistique pour comparer chaque ville au profil moyen
 







#question 8:


Y = X - moy
print('\n' * 5) 
print("\nQuestion 8:")
print("\nMatrice centree Y (arrondie a 4 decimales):\n")
print(f"{'':>5}", end="")
for s in sports:
    print(f"{s:>10}", end="")
print()
for i in range(20):
    print(f"{villes[i]:>5}", end="")
    for val in Y[i]:
        print(f"{val:>10.4f}", end="")
    print()



# centrage des données en soustrayant l’individu moyen à chaque ville
# cette transformation permet d’éliminer l’effet du niveau global et de se concentrer uniquement sur les écarts entre les villes
# après centrage :
# - une valeur positive indique une pratique supérieure à la moyenne
# - une valeur négative indique une pratique inférieure à la moyenne
# le centrage prépare les données pour les analyses multivariées




#question 9:


def variance(data):
    return np.round(np.var(data, axis=0),4)

print('\n' * 5) 
print("Question 9:")
print("\nVariance des 6 variables :")
print(f"\n{'Sport':>12}  {'Variance':>14}")
print("-" * 30)
variances = variance(X)
for j in range(6):
    print(f"{sports[j]:>12}  {variances[j]:>14.4f}")



# calcul de la variance de chaque variable sportive
# la variance mesure le niveau de dispersion des pratiques autour de la moyenne
# une variance élevée indique que les villes présentent des comportements très différents pour ce sport
# une variance faible signifie que les pratiques sont relativement homogènes entre les villes
# cette mesure permet d’identifier les sports les plus discriminants



#question 10:

m = X.shape[0]
V = (1/m) * np.dot(Y.T, Y)
print('\n' * 5) 
print("\nQuestion 10:")
print("\nMatrice de covariance V:\n")
print(f"{'':>10}", end="")
for s in sports:
    print(f"{s:>14}", end="")
print()
for i in range(6):
    print(f"{sports[i]:>10}", end="")
    for j in range(6):
        print(f"{V[i,j]:>14.4f}", end="")
    print()


# construction de la matrice de covariance
# cette matrice permet d’analyser les relations linéaires entre les différentes pratiques sportives
# une covariance positive indique que deux sports évoluent dans le même sens
# une covariance négative indique des évolutions opposées
# cette matrice constitue la base des méthodes d’analyse multidimensionnelle comme l’ACP





# question 11 :
# on remarque que par exemple dans le H.ball et Natation une valeur  tres grande positives 
# donc les villes fortes en handball sont aussi forte en natation 
# et entre h.ball et tennis valeur negatif donc relation inverse 
# extraction des variances à partir de la matrice de covariance (éléments diagonaux)
# cette étape permet de vérifier la cohérence entre la variance calculée précédemment et celle issue de la structure de covariance




#question 12:

std_mat = np.sqrt(np.diag(V))
R = V / np.outer(std_mat, std_mat)
print('\n' * 5) 
print("\nQuestion 12:")
print("\nMatrice de correlation R:\n")
print(f"{'':>10}", end="")
for s in sports:
    print(f"{s:>10}", end="")
print()
for i in range(6):
    print(f"{sports[i]:>10}", end="")
    for j in range(6):
        print(f"{R[i,j]:>10.4f}", end="")
    print()



# construction de la matrice de corrélation
# contrairement à la covariance, la corrélation standardise les relations entre les variables
# les valeurs sont comprises entre -1 et 1 :
# - proche de 1  → forte corrélation positive
# - proche de -1 → forte corrélation négative
# - proche de 0  → absence de relation linéaire
# cette matrice permet de comparer l’intensité des relations entre sports indépendamment de leurs unités






# question 13 :
# analyse des relations entre sports à partir de la matrice de corrélation
# cette étape permet d’identifier :
# - les sports pratiqués conjointement
# - les sports indépendants
# - les oppositions éventuelles
# elle aide à comprendre la structure globale des comportements sportifs des villes







#question 14:

plt.figure(figsize=(15,5))

# 1) h.ball & gym 
plt.subplot(1,3,1)
plt.scatter(X[:,0], X[:,3], color='royalblue', edgecolor='black', s=80, alpha=0.7)
plt.title("Handball vs Gym", fontsize=12, fontweight='bold')
plt.xlabel("Handball")
plt.ylabel("Gym")
plt.grid(True)

# 2) b.ball & natation 
plt.subplot(1,3,2)
plt.scatter(X[:,1], X[:,4], color='darkorange', edgecolor='black', s=80, alpha=0.7)
plt.title("Basketball vs Natation", fontsize=12, fontweight='bold')
plt.xlabel("Basketball")
plt.ylabel("Natation")
plt.grid(True)

# 3) tennis & f.ball 
plt.subplot(1,3,3)
plt.scatter(X[:,2], X[:,5], color='seagreen', edgecolor='black', s=80, alpha=0.7)
plt.title("Tennis vs Football", fontsize=12, fontweight='bold')
plt.xlabel("Tennis")
plt.ylabel("Football")
plt.grid(True)

plt.tight_layout()
plt.show()



# représentation graphique des relations entre certaines paires de sports :
# - handball vs dym
# - basketball vs natation
# - tennis vs football
# chaque point représente une ville, cette visualisation permet d’observer :
# - les tendances
# - les regroupements
# - les éventuelles corrélations
# elle facilite l’interprétation des relations entre variables
