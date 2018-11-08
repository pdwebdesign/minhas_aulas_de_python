from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
#IMPORT DATASET
iris = load_iris()
test_idx = [0,50,100]
#print(iris.feature_names)
#print(iris.target_names)
#print(iris.data[0]) #parametros dessa flor
#print(iris.target[0]) #a varavel target contem os marcadores



#for i in range(len(iris.target)):
    #print("Exemplo %d: label %s, features %s" % (i,iris.tagert[i],iris.data[i]))
 #   print("Dataset Order:",i+1,"Species:",iris.target[i],iris.data[i])

#TRAIN A CLASSIFIER

#O teste é uma parte muito importante no aprendizado de máquinas

#training data
train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data,test_idx,axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

#o treino terá a maior parte dos dados
#e o teste apenas os exemplos que removi

#arvore de decisao e treinar:
clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)

print(test_target) #marcadores previstos correspondem com nossos dados de teste
print(clf.predict(test_data))#quer dizer que acertou todos
#print(iris.data[0])
#print(clf.predict([[6.3,2.5,5.0,1.9]]))