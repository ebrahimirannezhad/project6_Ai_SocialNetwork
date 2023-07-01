import networkx as nx
import numpy as np

np.random.seed(10)

def decide_support(graph, voter_support):
    updated_support = voter_support.copy()
    for node in graph.nodes:
        neighbors = list(graph.neighbors(node))
        neighbor_support = [voter_support[neighbor] for neighbor in neighbors]
        support_counts = {
            'Ebrahim': neighbor_support.count('Ebrahim'),
            'Rival': neighbor_support.count('Rival')
        }
        if support_counts['Ebrahim'] > support_counts['Rival']:
            updated_support[node] = 'Ebrahim'
        elif support_counts['Rival'] > support_counts['Ebrahim']:
            updated_support[node] = 'Rival'
        else:
            num_ties = neighbor_support.count('Undecided')
            if num_ties % 2 == 0:
                updated_support[node] = 'Ebrahim'
            else:
                updated_support[node] = 'Rival'
    return updated_support

def count_votes(voter_support):
    num_support_you = list(voter_support.values()).count('Ebrahim')
    num_support_rival = list(voter_support.values()).count('Rival')
    return num_support_you, num_support_rival

def count_persuaded_voters(funding):
    start_id = 3000
    end_id = start_id + int(funding/100) - 1
    return end_id - start_id + 1

def calculate_advertisement_cost(persuaded_voters):
    num_batches = int(persuaded_voters / 10)
    return num_batches * 1000

n = 10000
m = 100000
erdos_renyi_graph = nx.gnm_random_graph(n, m)

preferential_attachment_graph = nx.barabasi_albert_graph(n, 10)

voter_support = {}
for node in erdos_renyi_graph.nodes:
    last_digit = node % 10
    if last_digit in [0, 2, 4, 6]:
        voter_support[node] = 'Ebrahim'
    elif last_digit in [1, 3, 5, 7]:
        voter_support[node] = 'Rival'
    else:
        voter_support[node] = 'Undecided'

for day in range(1, 11):
    voter_support = decide_support(preferential_attachment_graph, voter_support)

num_support_you, num_support_rival = count_votes(voter_support)

funding = 9000
persuaded_voters = count_persuaded_voters(funding)

advertisement_cost = calculate_advertisement_cost(persuaded_voters)

num_support_you += persuaded_voters

if num_support_you > num_support_rival:
    election_result = 'Ebrahim win the election!'
    vote_difference = num_support_you - num_support_rival
elif num_support_rival > num_support_you:
    election_result = 'Your rival wins the election!'
    vote_difference = num_support_rival - num_support_you
else:
    election_result = 'It\'s a tie!'
    vote_difference = 0

print(election_result)
print("Vote Difference:", vote_difference)
print("Persuaded Voters:", persuaded_voters)
print("Advertisement Cost:", advertisement_cost)
