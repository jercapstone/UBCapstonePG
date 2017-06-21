
#cargamos las librerías
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil.parser import parse

from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
#from scipy.cluster.vq import kmeans,vq
from sklearn.cluster import KMeans
from __future__ import division


#cargamos fichero
campanyes = pd.read_csv ("D:/Capstone-UOC/Data/dades-capstone-def3_2.csv", parse_dates=True)

campanyes.info()

#validamos las columnas cargadas
campanyes.columns

# cálculo de la edad en años
campanyes['data_naixement']=pd.to_datetime(campanyes['data_naixement'])
campanyes['edad_dias']=(pd.to_datetime(campanyes['data_ini_lead'])-pd.to_datetime(campanyes['data_naixement']))
campanyes['edad_anyos']=campanyes['edad_dias'].astype('timedelta64[D]')/365.24

edad_media_anyos=campanyes['edad_anyos'].mean()
edad_media_anyos

campanyes['edad_anyos'].hist(bins=90) 

edad_media_anyos


# recuento de usuarios por semestre
campanyes.groupby(['semestre'])['identif_usuari'].count()

# recuento de usuarios por "estado de lead" vs "semestre"
campanyes.groupby(['semestre','estat_lead_recode'])['producte_comprat_recode'].count()

# recuento de usuarios por "matricula" vs "semestre"
campanyes.groupby(['semestre','matricula'])['producte_comprat_recode'].count()


# evolución campañas 20151, 20152 y 20161
campanya_20151 = campanyes[campanyes['semestre'] == 20151]
campanya_20152 = campanyes[campanyes['semestre'] == 20152]
campanya_20161 = campanyes[campanyes['semestre'] == 20161]
campanya_20151
campanya_20152
campanya_20161

campanya_20151['data_ini_lead_date']=pd.to_datetime(campanya_20151['data_ini_lead'])
campanya_20152['data_ini_lead_date']=pd.to_datetime(campanya_20152['data_ini_lead'])
campanya_20161['data_ini_lead_date']=pd.to_datetime(campanya_20161['data_ini_lead'])

#graficamos la evolución de leads campanya 20151, 20152 y 20161 por fecha
evol_campanya_20151=campanya_20151.groupby(['data_ini_lead_date'])['producte_comprat_recode'].count()
evol_campanya_20152=campanya_20152.groupby(['data_ini_lead_date'])['producte_comprat_recode'].count()
evol_campanya_20161=campanya_20161.groupby(['data_ini_lead_date'])['producte_comprat_recode'].count()

evol_campanya_20151

evol_campanya_20151.plot()
evol_campanya_20152.plot()
evol_campanya_20161.plot()


# seleccionamos a los usuarios matriculados
campanya_matriculats = campanyes[campanyes['just_lead_recode'] == 'Matriculado']
campanya_matriculats = campanya_matriculats[['identif_usuari','just_lead_recode']] #seleccionamos la columna de matriculados
campanya_matriculats 


# agrupamos por identif_usuari y calculamos first, promedio, count_distinct para diferentes campos
Persones_Campanya_sexe = pd.DataFrame(campanyes.groupby(['identif_usuari'])['sexe'].first())  #sexo 
Persones_Campanya_edat = pd.DataFrame(campanyes.groupby(['identif_usuari'])['edad_anyos'].mean())  #edad
Persones_Campanya_prodcomp = pd.DataFrame(campanyes.groupby(['identif_usuari'])['producte_comprat_recode'].nunique())  #producto comprado
Persones_Campanya_puntentr = pd.DataFrame(campanyes.groupby(['identif_usuari'])['punt_entrada_recode'].nunique())  #punto entrada
Persones_Campanya_area = pd.DataFrame(campanyes.groupby(['identif_usuari'])['area_prod_comprat_recode'].nunique())  #área
Persones_Campanya_subarea = pd.DataFrame(campanyes.groupby(['identif_usuari'])['subarea_prod_comprat_recode'].nunique())  #subarea
Persones_Campanya_tipusprod = pd.DataFrame(campanyes.groupby(['identif_usuari'])['tipus_producte_comprat'].nunique())  #tipo de producto
Persones_Campanya_canal_recode = pd.DataFrame(campanyes.groupby(['identif_usuari'])['canal_recode'].nunique())  #canal
Persones_Campanya_idioma_recode = pd.DataFrame(campanyes.groupby(['identif_usuari'])['idioma_recode'].nunique())  #idioma
Persones_Campanya_semestre = pd.DataFrame(campanyes.groupby(['identif_usuari'])['semestre'].nunique())  #semestre
Persones_Campanya_regio = pd.DataFrame(campanyes.groupby(['identif_usuari'])['regio'].nunique())  #región

#añadimos índice para liberar el código de usuario que está siendo utilizado previamente como clave
Persones_Campanya_sexe = Persones_Campanya_sexe.reset_index(drop=False)
Persones_Campanya_edat = Persones_Campanya_edat.reset_index(drop=False)
Persones_Campanya_prodcomp = Persones_Campanya_prodcomp.reset_index(drop=False)
Persones_Campanya_puntentr = Persones_Campanya_puntentr.reset_index(drop=False)
Persones_Campanya_area = Persones_Campanya_area.reset_index(drop=False)
Persones_Campanya_subarea = Persones_Campanya_subarea.reset_index(drop=False)
Persones_Campanya_tipusprod = Persones_Campanya_tipusprod.reset_index(drop=False)
Persones_Campanya_canal_recode = Persones_Campanya_canal_recode.reset_index(drop=False)
Persones_Campanya_idioma_recode = Persones_Campanya_idioma_recode.reset_index(drop=False)
Persones_Campanya_semestre = Persones_Campanya_semestre.reset_index(drop=False)
Persones_Campanya_regio = Persones_Campanya_regio.reset_index(drop=False)

#unimos los dataframes con información por usuario a una tabla única
Persones_activitat = pd.merge(Persones_Campanya_sexe, Persones_Campanya_edat, on='identif_usuari')
Persones_activitat = pd.merge(Persones_activitat, Persones_Campanya_prodcomp, on='identif_usuari')
Persones_activitat = pd.merge(Persones_activitat, Persones_Campanya_puntentr, on='identif_usuari')
Persones_activitat = pd.merge(Persones_activitat, Persones_Campanya_area, on='identif_usuari')
Persones_activitat = pd.merge(Persones_activitat, Persones_Campanya_subarea, on='identif_usuari')
Persones_activitat = pd.merge(Persones_activitat, Persones_Campanya_tipusprod, on='identif_usuari')
Persones_activitat = pd.merge(Persones_activitat, Persones_Campanya_canal_recode, on='identif_usuari')
Persones_activitat = pd.merge(Persones_activitat, Persones_Campanya_idioma_recode, on='identif_usuari')
Persones_activitat = pd.merge(Persones_activitat, Persones_Campanya_regio, on='identif_usuari')
Persones_activitat = pd.merge(Persones_activitat, campanya_matriculats,how='left', on='identif_usuari')
Persones_activitat['just_lead_recode'].fillna('No Matriculado', inplace=True)
Persones_activitat = Persones_activitat.rename(columns={'just_lead_recode':'estado_matricula'})
Persones_activitat.groupby('estado_matricula')['identif_usuari'].count()



Persones_activitat.describe() #descriptivas de los índices obtenidos

#Borramos las tablas intermedias
del Persones_Campanya_sexe
del Persones_Campanya_edat
del Persones_Campanya_prodcomp
del Persones_Campanya_puntentr
del Persones_Campanya_area
del Persones_Campanya_subarea
del Persones_Campanya_tipusprod
del Persones_Campanya_canal_recode
del Persones_Campanya_idioma_recode
del Persones_Campanya_semestre
del Persones_Campanya_regio
del campanya_matriculats




# clustering con K-means

data_clustering = Persones_activitat.ix[:,3:11]
data_clustering

kmeans_n3 = KMeans(n_clusters=3)
kmeans_n3.fit(data_clustering)
kmeans_n3
centroid_n3 = kmeans_n3.cluster_centers_
cluster_n3 = kmeans_n3.labels_

kmeans_n4 = KMeans(n_clusters=4)
kmeans_n4.fit(data_clustering)
kmeans_n4
centroid_n4 = kmeans_n4.cluster_centers_
cluster_n4 = kmeans_n4.labels_

kmeans_n5 = KMeans(n_clusters=5)
kmeans_n5.fit(data_clustering)
kmeans_n5
centroid_n5 = kmeans_n5.cluster_centers_
cluster_n5 = kmeans_n5.labels_

kmeans_n6 = KMeans(n_clusters=6)
kmeans_n6.fit(data_clustering)
kmeans_n6
centroid_n6 = kmeans_n6.cluster_centers_
cluster_n6 = kmeans_n6.labels_

kmeans_n7 = KMeans(n_clusters=7)
kmeans_n7.fit(data_clustering)
kmeans_n7
centroid_n7 = kmeans_n7.cluster_centers_
cluster_n7 = kmeans_n7.labels_

kmeans_n8 = KMeans(n_clusters=8)
kmeans_n8.fit(data_clustering)
kmeans_n8
centroid_n8 = kmeans_n8.cluster_centers_
cluster_n8 = kmeans_n8.labels_


print (centroid_n3)
print (centroid_n4)
print (centroid_n5)
print (centroid_n6)
print (centroid_n7)
print (centroid_n8)

cluster_n3=pd.DataFrame(cluster_n3)
cluster_n4=pd.DataFrame(cluster_n4)
cluster_n5=pd.DataFrame(cluster_n5)
cluster_n6=pd.DataFrame(cluster_n6)
cluster_n7=pd.DataFrame(cluster_n7)
cluster_n8=pd.DataFrame(cluster_n8)

cluster_n3 = cluster_n3.rename(columns={0:'cluster_n3'})
cluster_n4 = cluster_n4.rename(columns={0:'cluster_n4'})
cluster_n5 = cluster_n5.rename(columns={0:'cluster_n5'})
cluster_n6 = cluster_n6.rename(columns={0:'cluster_n6'})
cluster_n7 = cluster_n7.rename(columns={0:'cluster_n7'})
cluster_n8 = cluster_n8.rename(columns={0:'cluster_n8'})

frame=[Persones_activitat,cluster_n3,cluster_n4,cluster_n5,cluster_n6,cluster_n7,cluster_n8]
Persones_activitat_cluster=pd.concat(frame,axis=1)


################
#Churn analysis#
################

# Isolate target data
churn_result = Persones_activitat['estado_matricula']
y = np.where(churn_result == 'Matriculado',1,0)

# We don't need these columns
to_drop = ['identif_usuari','sexe','edad_anyos','estado_matricula']
churn_feat_space = Persones_activitat.drop(to_drop,axis=1)

# 'yes'/'no' has to be converted to boolean values
# NumPy converts these from boolean to 1. and 0. later
#yes_no_cols = ["Int'l Plan","VMail Plan"]
#churn_feat_space[yes_no_cols] = churn_feat_space[yes_no_cols] == 'yes'

# Pull out features for future use
features = churn_feat_space.columns

X = churn_feat_space.as_matrix().astype(np.float)

print "Feature space holds %d observations and %d features" % X.shape
print "Unique target labels:", np.unique(y)


%matplotlib inline
import matplotlib.pyplot as plt
plt.pie(np.c_[len(y)-np.sum(y),np.sum(y)][0],labels=['No Churn','Churn'],colors=['r','g'],shadow=True,autopct ='%.2f' )
fig = plt.gcf()
fig.set_size_inches(6,6)

import pickle
ofname = open('churn_data.pkl', 'wb')
s = pickle.dump([X,y,features],ofname)
ofname.close()



#Let's see what the boundary looks like in a toy problem.

MAXN=10
X = np.concatenate([1.25*np.random.randn(MAXN,2),5+1.5*np.random.randn(MAXN,2)]) 
X = np.concatenate([X,[8,5]+1.5*np.random.randn(MAXN,2)])
y = np.concatenate([np.ones((MAXN,1)),-np.ones((MAXN,1))])
y = np.concatenate([y,np.ones((MAXN,1))])
idxplus = y==1
idxminus = y==-1
plt.scatter(X[idxplus.ravel(),0],X[idxplus.ravel(),1],color='r')
plt.scatter(X[idxminus.ravel(),0],X[idxminus.ravel(),1],color='b')

from sklearn import cross_validation
from sklearn import neighbors
from sklearn import metrics

delta = 0.05
xx = np.arange(-5.0, 15.0, delta)
yy = np.arange(-5.0, 15.0, delta)
XX, YY = np.meshgrid(xx, yy)
Xf = XX.flatten()
Yf = YY.flatten()
sz=XX.shape
data = np.c_[Xf[:,np.newaxis],Yf[:,np.newaxis]];


#Evaluate the model for a given weight
clf = neighbors.KNeighborsClassifier(1)
clf.fit(X,y.ravel())
Z=clf.predict(data)
Z.shape=sz

plt.imshow(Z, interpolation='bilinear', origin='lower', extent=(-5,15,-5,15),alpha=0.3, vmin=-1, vmax=1)
plt.contour(XX,YY,Z,[0])
fig = plt.gcf()
fig.set_size_inches(9,9)



#Let's see what the boundary looks like in a toy problem.

plt.scatter(X[idxplus.ravel(),0],X[idxplus.ravel(),1],color='r')
plt.scatter(X[idxminus.ravel(),0],X[idxminus.ravel(),1],color='b')

clf = neighbors.KNeighborsClassifier(3)
clf.fit(X,y.ravel())
Z2=clf.predict(data)
Z2.shape=sz

plt.imshow(Z, interpolation='bilinear', origin='lower', extent=(-5,15,-5,15),alpha=0.4, vmin=-1, vmax=1)
plt.imshow(Z2, interpolation='bilinear', origin='lower', extent=(-5,15,-5,15),alpha=0.2, vmin=-1, vmax=1)

plt.contour(XX,YY,Z2,[0])
fig = plt.gcf()
fig.set_size_inches(9,9)


#Recover Churn data
import pickle
fname = open('churn_data.pkl','rb')
data = pickle.load(fname)
X = data[0]
y = data[1]
print 'Loading ok.'



from sklearn import cross_validation
from sklearn import neighbors
from sklearn import metrics
acc = np.zeros((5,))
i=0
kf=cross_validation.KFold(n=y.shape[0], n_folds=5, shuffle=False, random_state=0)
#We will build the predicted y from the partial predictions on the test of each of the folds
yhat = y.copy()
for train_index, test_index in kf:
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    dt = neighbors.KNeighborsClassifier(n_neighbors=1)
    dt.fit(X_train,y_train)
    yhat[test_index] = dt.predict(X_test)
    acc[i] = metrics.accuracy_score(yhat[test_index], y_test)
    i=i+1
print 'Mean accuracy: '+ str(np.mean(acc))



def draw_confusion(y,yhat,labels):
    cm = metrics.confusion_matrix(y, yhat)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.matshow(cm)
    plt.title('Confusion matrix',size=20)
    ax.set_xticklabels([''] + labels, size=20)
    ax.set_yticklabels([''] + labels, size=20)
    plt.ylabel('Predicted',size=20)
    plt.xlabel('True',size=20)
    for i in xrange(2):
        for j in xrange(2):
            ax.text(i, j, cm[i,j], va='center', ha='center',color='white',size=20)
    fig.set_size_inches(7,7)
    plt.show()

draw_confusion(y,yhat,['no churn', 'churn'])
print metrics.classification_report(y,yhat)



# Standarize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)


from sklearn import metrics
acc_snooping = np.zeros((5,))
i=0
kf=cross_validation.KFold(n=y.shape[0], n_folds=5, shuffle=False, random_state=0)
#We will build the predicted y from the partial predictions on the test of each of the folds
yhat = y.copy()
for train_index, test_index in kf:
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    dt = neighbors.KNeighborsClassifier(3)
    dt.fit(X_train,y_train)
    yhat[test_index] = dt.predict(X_test)
    acc_snooping[i] = metrics.accuracy_score(yhat[test_index], y_test)
    i=i+1
print 'Mean accuracy: '+ str(np.mean(acc_snooping))



#NO SNOOPING
acc = np.zeros((5,))
i=0
#We will build the predicted y from the partial predictions on the test of each of the folds
yhat = y.copy()
for train_index, test_index in kf:
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    dt = neighbors.KNeighborsClassifier(3)
    dt.fit(X_train,y_train)
    X_test = scaler.transform(X_test)
    yhat[test_index] = dt.predict(X_test)
    acc[i] = metrics.accuracy_score(yhat[test_index], y_test)
    i=i+1
print 'Mean accuracy: '+ str(np.mean(acc))


acct=np.c_[acc_snooping,acc]
plt.boxplot(acct);
for i in xrange(2):
    xderiv = (i+1)*np.ones(acct[:,i].shape)+(np.random.rand(5,)-0.5)*0.1
    plt.plot(xderiv,acct[:,i],'ro',alpha=0.3)
ax = plt.gca()
ax.set_xticklabels(['snooping', 'no snooping'])



def draw_confusion(y,yhat,labels):
    cm = metrics.confusion_matrix(y, yhat)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.matshow(cm)
    plt.title('Confusion matrix',size=20)
    ax.set_xticklabels([''] + labels, size=20)
    ax.set_yticklabels([''] + labels, size=20)
    plt.ylabel('Predicted',size=20)
    plt.xlabel('True',size=20)
    for i in xrange(2):
        for j in xrange(2):
            ax.text(i, j, cm[i,j], va='center', ha='center',color='white',size=20)
    fig.set_size_inches(7,7)
    plt.show()

draw_confusion(y,yhat,['no churn', 'churn'])
print metrics.classification_report(y,yhat)



def draw_confusion(y,yhat,labels):
    cm = metrics.confusion_matrix(y, yhat)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.matshow(cm)
    plt.title('Confusion matrix',size=20)
    ax.set_xticklabels([''] + labels, size=20)
    ax.set_yticklabels([''] + labels, size=20)
    plt.ylabel('Predicted',size=20)
    plt.xlabel('True',size=20)
    ax.text(0, 0, 'TP', va='center', ha='center',color='white',size=20)
    ax.text(0, 1, 'FN', va='center', ha='center',color='white',size=20)
    ax.text(1, 0, 'FP', va='center', ha='center',color='white',size=20)
    ax.text(1, 1, 'TN', va='center', ha='center',color='white',size=20)            
    fig.set_size_inches(7,7)
    plt.show()

draw_confusion(y,yhat,['positive', 'negative'])



# Let us check the concepts with churn as the positive class
TP = np.sum(np.logical_and(yhat==1,y==1))
TN = np.sum(np.logical_and(yhat==0,y==0))
FP = np.sum(np.logical_and(yhat==1,y==0))
FN = np.sum(np.logical_and(yhat==0,y==1))

print 'TP: ' + str(TP)
print 'TN: ' + str(TN)
print 'FP: ' + str(FP)
print 'FN: ' + str(FN)
print 'sensitivity/recall: '+ str(TP/(TP+FN))
print 'precision: '+ str(TP/(TP+FP))




#######################
# Árboles de decisión #
#######################

%matplotlib inline
#Let's see what the boundary looks like in a toy problem.
%reset -f
import numpy as np
import matplotlib.pyplot as plt
MAXN=10
np.random.seed(2)
X = np.concatenate([1.25*np.random.randn(MAXN,2),5+1.5*np.random.randn(MAXN,2)]) 
X = np.concatenate([X,[8,5]+1.5*np.random.randn(MAXN,2)])
y = np.concatenate([np.ones((MAXN,1)),-np.ones((MAXN,1))])
y = np.concatenate([y,np.ones((MAXN,1))])
idxplus = y==1
idxminus = y==-1
plt.scatter(X[idxplus.ravel(),0],X[idxplus.ravel(),1],color='r')
plt.scatter(X[idxminus.ravel(),0],X[idxminus.ravel(),1],color='b')

from sklearn import tree
from sklearn import metrics

delta = 0.05
xx = np.arange(-5.0, 15.0, delta)
yy = np.arange(-5.0, 15.0, delta)
XX, YY = np.meshgrid(xx, yy)
Xf = XX.flatten()
Yf = YY.flatten()
sz=XX.shape
data = np.c_[Xf[:,np.newaxis],Yf[:,np.newaxis]];
clf = tree.DecisionTreeClassifier(random_state=0)
clf.fit(X,y.ravel())
Z=clf.predict(data)
Z.shape=sz

plt.imshow(Z, interpolation='bilinear', origin='lower', extent=(-5,15,-5,15),alpha=0.3, vmin=-1, vmax=1)
plt.contour(XX,YY,Z,[0])
fig = plt.gcf()
fig.set_size_inches(9,9)

#Export Tree
import os
dotfile = tree.export_graphviz(clf, out_file = "toy_tree.dot")

os.system("dot -Tpng toy_tree.dot -o toy_tree.png")

from IPython.core.display import Image
Image("toy_tree.png")

##

clf = tree.DecisionTreeClassifier(random_state=0,max_depth=1)
clf.fit(X,y.ravel())
Z=clf.predict(data)
Z.shape=sz

plt.scatter(X[idxplus.ravel(),0],X[idxplus.ravel(),1],color='r')
plt.scatter(X[idxminus.ravel(),0],X[idxminus.ravel(),1],color='b')


plt.imshow(Z, interpolation='bilinear', origin='lower', extent=(-5,15,-5,15),alpha=0.3, vmin=-1, vmax=1)
plt.contour(XX,YY,Z,[0])
fig = plt.gcf()
fig.set_size_inches(9,9)



##

clf = tree.DecisionTreeClassifier(random_state=0, max_depth=2)
clf.fit(X,y.ravel())
Z=clf.predict(data)
Z.shape=sz

plt.scatter(X[idxplus.ravel(),0],X[idxplus.ravel(),1],color='r')
plt.scatter(X[idxminus.ravel(),0],X[idxminus.ravel(),1],color='b')

plt.imshow(Z, interpolation='bilinear', origin='lower', extent=(-5,15,-5,15),alpha=0.3, vmin=-1, vmax=1)
plt.contour(XX,YY,Z,[0])
fig = plt.gcf()
fig.set_size_inches(9,9)


##

import numpy as np
entropy = lambda p: -np.sum(p * np.log2(p)) if not 0 in p else 0
gini = lambda p: 1. - (np.array(p)**2).sum()
pvals = np.linspace(0, 1)        
plt.plot(pvals, [entropy([p,1-p])/2. for p in pvals], label='Entropy')
plt.plot(pvals, [gini([p,1-p]) for p in pvals], label='Gini')
plt.legend()





%reset -f
#Recover Churn data
import pickle
fname = open('churn_data.pkl','rb')
data = pickle.load(fname)
X = data[0]
y = data[1]
features = data[2]
print 'Loading ok.'


#NO SNOOPING
import numpy as np
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler
from sklearn import tree
from sklearn import metrics


kf=cross_validation.KFold(n=y.shape[0], n_folds=5, shuffle=False, random_state=0)

acc = np.zeros((5,))
i=0
#We will build the predicted y from the partial predictions on the test of each of the folds
yhat = y.copy()
for train_index, test_index in kf:
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    dt = tree.DecisionTreeClassifier(criterion='entropy')
    dt.fit(X_train,y_train)
    X_test = scaler.transform(X_test)
    yhat[test_index] = dt.predict(X_test)
    acc[i] = metrics.accuracy_score(yhat[test_index], y_test)
    i=i+1
print 'Mean accuracy: '+ str(np.mean(acc))

import matplotlib.pyplot as plt
def draw_confusion(y,yhat,labels):
    cm = metrics.confusion_matrix(y, yhat)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.matshow(cm)
    plt.title('Confusion matrix',size=20)
    ax.set_xticklabels([''] + labels, size=20)
    ax.set_yticklabels([''] + labels, size=20)
    plt.ylabel('Predicted',size=20)
    plt.xlabel('True',size=20)
    for i in xrange(2):
        for j in xrange(2):
            ax.text(i, j, cm[i,j], va='center', ha='center',color='white',size=20)
    fig.set_size_inches(7,7)
    plt.show()

draw_confusion(y,yhat,['no churn', 'churn'])
print metrics.classification_report(y,yhat)

# Let us check the concepts with churn as the positive class
TP = np.sum(np.logical_and(yhat==1,y==1))
TN = np.sum(np.logical_and(yhat==0,y==0))
FP = np.sum(np.logical_and(yhat==1,y==0))
FN = np.sum(np.logical_and(yhat==0,y==1))

print 'TP: ' + str(TP)
print 'TN: ' + str(TN)
print 'FP: ' + str(FP)
print 'FN: ' + str(FN)
print 'sensitivity/recall: '+ str(TP/(TP+FN))
print 'precision: '+ str(TP/(TP+FP))

import os
#Let us check the the first three levels of the tree. GraphViz and PyDot are needed.
dt = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
scaler = StandardScaler()
Xs = scaler.fit_transform(X)
dt.fit(Xs,y)

#Export Tree

dotfile = tree.export_graphviz(dt, out_file = "churn.dot", feature_names = features)


os.system("dot -Tpng churn.dot -o churn.png")


from IPython.core.display import Image
Image("churn.png")


