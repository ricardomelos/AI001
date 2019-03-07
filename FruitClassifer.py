# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:01:09 2019

@author: ricardo.melos
"""

from sklearn import tree

lisa = 1
irregular = 0
maça = 1
laranja = 0


orchard = [[150, lisa], [130, lisa], [180, irregular], [160, irregular]]
result = [maça, maça, laranja, laranja]

classifier = tree.DecisionTreeClassifier()

classifier.fit(orchard, result)

weight = input("Digite o peso ")
skill = input("Entre com o tipo de superficie ")


classifiedResult = classifier.predict([[weight, skill]])

if classifiedResult == 1:
    print("É uma maçã")
else:
    print("É uma laranja")
    
        
