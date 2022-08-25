# https://beta.programming.in.th/tasks/0013

dwarves = []
for _ in range(9):
    dwarves.append(int(input()))

imposter = []
sumDwarves = sum(dwarves)

for i in range(9):
    for j in range(i+1, 9):
        if sumDwarves-dwarves[i]-dwarves[j]==100:
            imposter.append(dwarves[i])
            imposter.append(dwarves[j])

for e in dwarves:
    if e not in imposter:
        print(e)