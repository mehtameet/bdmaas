from dataset import datasets

datasetObj=datasets()

from algorithms import algorithms

algorithmObj=algorithms()
algorithmObj.testrandomforest("KDD1")
algorithmObj.testrandomforest("KDD1")
algorithmObj.runrandomforest("KDD1")

