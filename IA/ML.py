from sklearn import tree

#classificar

features = [[140,"liso"],[130,"liso"],[150,"irregular"],[170,"irregular"]]
label = ["maca","maca","laranja","laranja"]

features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]

#treinar o classificador um exemplo e arvore de decisao

#criando a arvore vazia
clf = tree.DecisionTreeClassifier()
# vamos dizer que o mais pesado tem probabilidade maior de ser uma laranja
#no scikit o algoritmo de treinamento esta incluido no objeto do classificador e e chamado fit

clf = clf.fit(features,labels)

print(clf.predict([150,0]))

#vamos utilizar para classificar uma nova fruta


print("hello")