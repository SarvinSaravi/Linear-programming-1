import pulp

prob = pulp.LpProblem("My_3d_Problem", pulp.LpMinimize)

x_1 = pulp.LpVariable("x1", lowBound=0)
x_2 = pulp.LpVariable("x2", lowBound=0)
x_3 = pulp.LpVariable("x3", lowBound=0)

# Objective function
prob += 100 * x_1 + 1250 * x_2 + 750 * x_3, 'Objective'
# constraints
prob += x_1 <= 10, 'C1'
prob += x_2 >= 15, 'C2'
prob += x_1 + x_2 + x_3 <= 35, 'C3'

print(prob)

status = prob.solve()

print(pulp.LpStatus[prob.status])
# print(pulp.value(x_1))
# print(pulp.value(x_2))
# print(pulp.value(x_3))

print('++++++++++++++++++++++++++++++++')

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("\nMinimum Objective :")
print(pulp.value(prob.objective))
