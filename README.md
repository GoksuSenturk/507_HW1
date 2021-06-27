Implementation of Simulated Annealing optimization to solve the Quadratic Assignment Problem (QAP)


This code is an implementation of Simualted Annealing to solve the Quadratic Assignment Problem (QAP) test problems of 5 location and 5 facility. The objective is to minimize flow costs between the placed facilities. The flow cost is (flow * distance), where both flow and distance are symmetric between any given pair of departments.

First run main.py
python3 main.py

This algorithm give us optimized solutions and write it to sonuc.txt

Secondly for finding minimum cost from all solutions you should run min.py
python3 min.py

You can find solution which give optimal cost with going sonuc.txt and search the value you found from min.py
