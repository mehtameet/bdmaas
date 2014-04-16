from dataset import datasets

datasetObj=datasets()

from algorithms import algorithms

algorithmObj=algorithms()
#algorithmObj.testrandomforest("dataset10")
algorithmObj.trainrandomforest("dataset10")
#algorithmObj.runrandomforest("dataset10")

