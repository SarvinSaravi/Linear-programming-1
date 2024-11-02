import pulp

my_prob = pulp.LpProblem("Farm_Problem", pulp.LpMinimize)

c = pulp.LpVariable("c", lowBound=0)
w = pulp.LpVariable("w", lowBound=0)

# Objective function
my_prob += 0.40*c + 0.45*w, 'Z'
# constraints
my_prob += c + w <= 7, 'c1'
my_prob += 0.1*c + 0.15*w >= 0.65, 'c2'
my_prob += 0.75*c + 0.7*w >= 4, 'c3'

print(my_prob)

status = my_prob.solve()

print(pulp.LpStatus[my_prob.status])
# print(pulp.value(c))
# print(pulp.value(w))

# =============================================
for v in my_prob.variables():
    print(v.name, "=", v.varValue)

print("\nMinimum Objective :")
print(pulp.value(my_prob.objective))

