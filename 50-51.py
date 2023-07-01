import networkx as nx
import random

# ایجاد یک گراف Erdős-Rényi با ۱۰۰۰۰ گره و ۱۰۰۰۰۰ یال
Graph1 = nx.gnm_random_graph(10000, 100000, seed=10)

# ایجاد یک گراف preferential attachment با ۱۰۰۰۰ گره و درجه خروجی ۱۰
Graph2 = nx.barabasi_albert_graph(10000, 10, seed=10)

# اختصاص حمایت رای‌دهنده‌ها بر اساس رقم آخر شناسه گره
for node in Graph1.nodes:
    last_digit = node % 10
    if last_digit in [0, 2, 4, 6]:
        Graph1.nodes[node]['support'] = 'you'
    elif last_digit in [1, 3, 5, 7]:
        Graph1.nodes[node]['support'] = 'rival'
    else:
        Graph1.nodes[node]['support'] = 'undecided'

for node in Graph2.nodes:
    last_digit = node % 10
    if last_digit in [0, 2, 4, 6]:
        Graph2.nodes[node]['support'] = 'you'
    elif last_digit in [1, 3, 5, 7]:
        Graph2.nodes[node]['support'] = 'rival'
    else:
        Graph2.nodes[node]['support'] = 'undecided'

# تنظیم حمایت اولیه رای‌دهندگان تصمیم‌گیر شده
for node in Graph1.nodes:
    if Graph1.nodes[node]['support'] == 'you':
        Graph1.nodes[node]['initial_support'] = 0.4
    elif Graph1.nodes[node]['support'] == 'rival':
        Graph1.nodes[node]['initial_support'] = 0.4
    else:
        Graph1.nodes[node]['initial_support'] = 0.2

for node in Graph2.nodes:
    if Graph2.nodes[node]['support'] == 'you':
        Graph2.nodes[node]['initial_support'] = 0.4
    elif Graph2.nodes[node]['support'] == 'rival':
        Graph2.nodes[node]['initial_support'] = 0.4
    else:
        Graph2.nodes[node]['initial_support'] = 0.2

# شبیه‌سازی فرآیند انتخابات برای ۱۰ روز
for day in range(1, 11):
    # بروزرسانی حمایت رای‌دهندگان تصمیم‌نگر شده بر اساس ترجیحات همسایگانشان
    for node in Graph1.nodes:
        if Graph1.nodes[node]['support'] == 'undecided':
            neighbor_support = [Graph1.nodes[neighbor]['initial_support'] for neighbor in Graph1.neighbors(node)]
            if neighbor_support.count(0.4) > neighbor_support.count(0.6):
                Graph1.nodes[node]['support'] = 'you'
            elif neighbor_support.count(0.4) < neighbor_support.count(0.6):
                Graph1.nodes[node]['support'] = 'rival'
            else:
                Graph1.nodes[node]['support'] = random.choice(['you', 'rival'])

    for node in Graph2.nodes:
        if Graph2.nodes[node]['support'] == 'undecided':
            neighbor_support = [Graph2.nodes[neighbor]['initial_support'] for neighbor in Graph2.neighbors(node)]
            if neighbor_support.count(0.4) > neighbor_support.count(0.6):
                Graph2.nodes[node]['support'] = 'you'
            elif neighbor_support.count(0.4) < neighbor_support.count(0.6):
                Graph2.nodes[node]['support'] = 'rival'
            else:
                Graph2.nodes[node]['support'] = random.choice(['you', 'rival'])

    # چاپ حمایت هر کاندیدا در این روز
    you_support1 = sum([Graph1.nodes[node]['initial_support'] for node in Graph1.nodes if Graph1.nodes[node]['support'] == 'you'])
    rival_support1 = sum([Graph1.nodes[node]['initial_support'] for node in Graph1.nodes if Graph1.nodes[node]['support'] == 'rival'])
    you_support2 = sum([Graph2.nodes[node]['initial_support'] for node in Graph2.nodes if Graph2.nodes[node]['support'] == 'you'])
    rival_support2 = sum([Graph2.nodes[node]['initial_support'] for node in Graph2.nodes if Graph2.nodes[node]['support'] == 'rival'])
    print(f"Day {day}: You - {you_support1 + you_support2:.2%}, Rival - {rival_support1 + rival_support2:.2%}")

# شمارش آرا در روز انتخابات
you_votes1 = sum([1 for node in Graph1.nodes if Graph1.nodes[node]['support'] == 'you'])
rival_votes1 = sum([1 for node in Graph1.nodes if Graph1.nodes[node]['support'] == 'rival'])
you_votes2 = sum([1 for node in Graph2.nodes if Graph2.nodes[node]['support'] == 'you'])
rival_votes2 = sum([1 for node in Graph2.nodes if Graph2.nodes[node]['support'] == 'rival'])

# چاپ نتیجه انتخابات
if you_votes1 + you_votes2 > rival_votes1 + rival_votes2:
    print("Ebrahim win!")
elif you_votes1 + you_votes2 < rival_votes1 + rival_votes2:
    print("Rival wins!")
else:
    print("It's a tie!")