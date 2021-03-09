# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 22:05:42 2021

@author: raha_
"""

import pickle
import py2neo
from py2neo import Graph, Node, Relationship
uri1="bolt://localhost:7687"

f = open('store.pckl', 'rb')
Net = pickle.load(f)
f.close()
edge=Net['edge']
ns=Net['source']
nd=Net['target']
l=len(Net)
for i in range(500):
    e=edge[i]
    s=ns[i]
    d=nd[i]
    n1 = Node("Person",name=s)
    n2 = Node("obj",name=d)
    
    rel = Relationship(n2,e,n1) #n2-RelationshipType->n1
    graph = Graph(uri1, user='neo4j', password='123456')
    tx = graph.begin()
    tx.merge(n1,"Person","name") #node,label,primary key
    tx.merge(n2,"Obj","name") #node,label,pirmary key
    tx.merge(rel)
    tx.commit()
