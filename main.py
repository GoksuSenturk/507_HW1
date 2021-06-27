import numpy as np
import random as rd
import sys

flow = np.array([
    [0, 5, 2, 4, 1],
    [5, 0, 3, 0, 2],
    [2, 3, 0, 0, 0],
    [4, 0, 0, 0, 5],
    [1, 2, 0, 5, 0]
])

dist = np.array([
    [0, 1, 1, 2, 3],
    [1, 0, 2, 1, 2],
    [1, 2, 0, 1, 2],
    [2, 1, 1, 0, 1],
    [3, 2, 2, 1, 0]
])


# cost function = flow*distance matrix
def cost(flow):
    global dist
    cost = flow * dist
    return np.sum(cost[np.triu_indices(5, 1)])


# Generate random solution with the random function creating initial solution
def randHeu(mat):
    ndim = mat.shape[0]
    rand_sol = rd.sample(range(ndim), ndim)
    return mat[np.ix_(rand_sol, rand_sol)], rand_sol


rand = randHeu(flow)

sol_len = 5
N = 10  # size of neighboorhood matrix
neighbors = np.zeros((N, sol_len + 2), dtype=int)


# 2 Opt Neighborhood Approach:
# swap the first two elements in the given solution,
# move one spot to the right in the new solution list
# and swap these two values in given solution to
# form another new solution, make another one move to
# the right and perform same operation until the
# end of the index in the solution list is reached
# all of these new solutions (neighbors) form the neighborhood matrix
def swap_move(sol_n):
    global idx, neighbors
    # print idx
    for i in range(sol_len):
        j = i + 1
        for j in range(sol_len):
            if i < j:
                idx = idx + 1
                sol_n[j], sol_n[i] = sol_n[i], sol_n[j]  # swap two elements
                neighbors[idx, :-2] = sol_n
                neighbors[idx, -2:] = [sol_n[i], sol_n[j]]
                sol_n[i], sol_n[j] = sol_n[j], sol_n[i]


def return_neighbor(curnt_sol):
    global neighbors, idx
    idx = -1
    swap_move(curnt_sol)  # make a move to 2-opt neighboorhood
    cost = np.zeros((len(neighbors)))  # holds the cost of the neighbors
    for index in range(len(neighbors)):
        cost[index] = solcost(neighbors[index, :-2])  # evaluate the cost of the candidate neighbors
    rank = np.argsort(cost)  # sorted index based on cost
    neighbors = neighbors[rank]
    k = []
    for n in range(N):
        k = rd.randint(0, N - 1)
    return (neighbors[k, :-2])  # randomly select one of the neighbors


def solcost(sol):
    global flow, dist
    cost = flow * dist[np.ix_(sol, sol)]
    # return np.sum(cost[np.triu_indices(5,1)])*2
    return np.sum(cost)


# Acceptance Probability function
def accProb(delta, T):
    return np.exp(-delta / T) > rd.random()


def simAnneal(flow, dist):
    curr_sol = rd.sample(range(sol_len), sol_len)
    # print curr_sol
    # curr_sol = [2,1,0,4,3]
    curr_cost = cost(flow[np.ix_(curr_sol, curr_sol)])
    final_sol = curr_sol
    final_cost = cost(flow[np.ix_(final_sol, final_sol)])
    T = 10000
    T_min = 0.001
    alpha = 0.8
    while T > T_min:
        new_sol = return_neighbor(curr_sol)
        new_cost = cost(flow[np.ix_(new_sol, new_sol)])
        if new_cost < curr_cost | accProb(new_cost - curr_cost, T):
            curr_sol = new_sol
            curr_cost = cost(flow[np.ix_(curr_sol, curr_sol)])
        if curr_cost < final_cost:
            final_sol = curr_sol
            final_cost = cost(flow[np.ix_(final_sol, final_sol)])
        T = T * alpha
    print("Final Simulated Annealing Solution: " + str(final_sol))
    print("Final Simulated Annealing Cost: " + str(final_cost))

sys.stdout = open("./sonuc.txt", "w")

for _ in range(120):
    simAnneal(flow, dist)
sys.stdout.close()









