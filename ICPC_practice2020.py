fname = "b3.in"

with open(fname, "r") as f:
    data = f.readlines()

v, e = map(int, data[0].split(" "))
independent_vs = list(range(1, v+1))

V = [list(map(int, i.split(" "))) for i in data[1:]]
# print(V[:10])


def _directConn(v, pair):
    idx = pair.index(v)
    return pair[1 - idx]


to_del = []
for v in independent_vs:
    if v not in to_del:
        for pair in V:
            if v in pair:
                v_out = _directConn(v, pair)
                to_del.append(v_out)

nodes = []
n = 0
print(len(independent_vs))
for i in independent_vs:
    if i not in to_del:
        nodes.append(1)
        n += 1
    else:
        nodes.append(0)

print(n)
print(len(nodes))

with open(f"{fname[:-3]}_ICPC_output.txt", "w") as f:
    f.write(str(n)+"\n")
    f.write(str(nodes).strip("[]").replace(",", ""))
