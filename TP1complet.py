import numpy as np
import matplotlib.pyplot as plt  

# question 1:

X = np.array([
    [1881.9, 96.8, 14.2, 25.2, 1135.5, 278.3],
    [3369.8, 96.8, 10.8, 51.6, 1331.7, 284.0],
    [4467.4, 138.2, 9.5, 34.2, 2346.1, 312.3],
    [1862.1, 83.2, 8.8, 27.6, 972.6, 203.4],
    [3499.8, 287.0, 11.5, 49.4, 2139.4, 358.0],
    [3903.2, 170.7, 6.3, 42.0, 1935.2, 292.9],
    [2620.7, 129.5, 4.2, 16.8, 1346.0, 131.8],
    [3678.4, 157.0, 6.0, 24.9, 1682.6, 194.2],
    [3840.5, 187.9, 10.2, 39.6, 1859.9, 449.1],
    [2170.2, 140.5, 11.7, 31.1, 1351.1, 256.5],
    [3920.4, 128.0, 7.2, 25.5, 1911.5, 64.1],
    [2599.6, 39.6, 5.5, 19.4, 1050.8, 172.5],
    [2828.5, 211.3, 9.9, 21.8, 1085.0, 209.0],
    [2498.7, 123.2, 7.4, 26.5, 1086.2, 153.5],
    [2685.1, 41.2, 2.3, 10.6, 812.5, 89.8],
    [2739.3, 100.7, 6.6, 22.0, 1270.4, 180.5],
    [1662.1, 81.1, 10.1, 19.1, 872.2, 123.3],
    [2469.9, 142.9, 15.5, 30.9, 1165.5, 335.5],
    [2350.7, 38.7, 2.4, 13.5, 1253.1, 170.0],
    [3177.7, 292.1, 8.0, 34.8, 1400.0, 358.9]
])


villes = [f"V{i}" for i in range(1, 21)]
sports = ["H.Ball", "B.Ball", "Tennis", "Gym", "Natation", "F.Ball"]

Xt = X.T

print("\nQuestion 1:")

print("Matrice X :")
print(X)

print("\nMatrice transposée Xt :")
print(Xt)



# question 2:

individus = ["V" + str(i) for i in range(1, 21)]

print('\n' * 5) 
print("\nQuestion 2:")

print("\nListe des individus :")
print(individus)

# question 3:

HandBall   = X[:, 0]
BasketBall = X[:, 1]
Tennis     = X[:, 2]
Gym        = X[:, 3]
Natation   = X[:, 4]
FootBall   = X[:, 5]

print("\nQuestion 3:")

print("\nVecteur HandBall :")
print(HandBall)

print("\nVecteur BasketBall :")
print(BasketBall)

print("\nVecteur Tennis :")
print(Tennis)

print("\nVecteur Gym :")
print(Gym)

print("\nVecteur Natation :")
print(Natation)

print("\nVecteur FootBall :")
print(FootBall)



# =========================================================
# QUESTION 4 : Accéder aux individus 3, 11, 15, 19
# =========================================================

indices = [3, 11, 15, 19]
individus_sel = X[np.array(indices) - 1]  # -1 car les indices commencent à 0 en Python
print('\n' * 5) 
print("\nQuestion 4:")
print("\nIndividus sélectionnés :\n", individus_sel)


# =========================================================
# QUESTION 5 : Proximité (distance euclidienne)
# =========================================================

from scipy.spatial.distance import pdist, squareform
distances = squareform(pdist(individus_sel, metric='euclidean'))
print('\n' * 5) 
print("\nQuestion 5:")
print("\nMatrice des distances :\n", distances)


# =========================================================
# QUESTION 6 : Moyenne, Variance, Ecart-type
# =========================================================

moy = np.mean(X, axis=0)
var = np.var(X, axis=0)
std = np.std(X, axis=0)

stats = np.round(np.array([moy, var, std]).T,4)
print('\n' * 5) 
print("\nQuestion 6:")
print("\nTableau statistique [moyenne arithmétique, variance, l’écart type] :\n", stats)


# =========================================================
# QUESTION 7 : Individu moyen 
# =========================================================

ind_moy = moy
print('\n' * 5) 
print("\nQuestion 7:")
print("\nIndividu moyen :\n", ind_moy)


# =========================================================
# QUESTION 8 : Matrice centrée
# =========================================================

Y = X - moy
print('\n' * 5) 
print("\nQuestion 8:")
print("\nMatrice centrée Y:\n", Y)


# =========================================================
# QUESTION 9 : Fonction variance
# =========================================================

def variance(data):
    return np.round(np.var(data, axis=0),4)

print('\n' * 5) 
print("\nQuestion 9:")
print("\nVariance via fonction:\n", variance(X))


# =========================================================
# QUESTION 10 : Matrice de covariance
# =========================================================

m = X.shape[0]
V = (1/m) * np.dot(Y.T, Y)
print('\n' * 5) 
print("\nQuestion 10:")
print("\nMatrice de covariance V:\n", np.round(V,4))  # "positive → évoluent ensemble"  "négative → évoluent en sens opposé"  "proche de 0 → indépendants"


# =========================================================
# QUESTION 11 : (Commentaire à faire dans le rapport)
# =========================================================


# =========================================================
# QUESTION 12 : Matrice de corrélation
# =========================================================

std_mat = np.sqrt(np.diag(V))
R = V / np.outer(std_mat, std_mat)
print('\n' * 5) 
print("\nQuestion 12:")
print("\nMatrice de corrélation R:\n", np.round(R,4))


# =========================================================
# QUESTION 13 : (Commentaire à faire dans le rapport)
# =========================================================


# =========================================================
# QUESTION 14 : Nuages de points
# =========================================================

plt.figure()

plt.subplot(1,3,1)
plt.scatter(X[:,1-1], X[:,4-1])
plt.title("H.Ball vs Gym")

plt.subplot(1,3,2)
plt.scatter(X[:,2-1], X[:,5-1])
plt.title("B.Ball vs Natation")

plt.subplot(1,3,3)
plt.scatter(X[:,3-1], X[:,6-1])
plt.title("Tennis vs F.Ball")

plt.show()