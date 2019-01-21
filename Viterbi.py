import sys
states = ("rainy", "sunny")
start_p = {"rainy": 0.7, "sunny": 0.3}
observations = list(sys.argv[1])
for i in range(len(observations)):
    if observations[i] == "W":
        observations[i] = "walk"
    elif observations[i] == "C":
        observations[i] = "clean"
    else:
        observations[i] = "shop"


transition_p = {
    "rainy": {"rainy": 0.6, "sunny": 0.4},
    "sunny": {"rainy": 0.3, "sunny": 0.7}
}

emission_p = {
    "rainy": {"walk": 0.3, "shop": 0.35, "clean": 0.35},
    "sunny": {"walk": 0.5, "shop": 0.4, "clean": 0.1}
}

def viterbi (states, start_p, observations, transition_p, emission_p):
    v = []
    for i in range(len(observations)):
        v.append({})
    path = {}

    for s in states:
        v[0][s] = start_p[s] * emission_p[s][observations[0]]
        path[s] = [s]

    for t in range(1, len(observations)):
        newPath = {}

        for s in states:
            max = 0
            smax = ""
            for s2 in states:
                temp = v[t-1][s2] * transition_p[s2][s] * emission_p[s][observations[t]]
                if temp > max:
                    max = temp
                    smax = s2

            v[t][s] = max
            newPath[s] = path[smax] + [s]

        path = newPath
    max = 0
    smax = ""
    for s in states:
        if v[len(observations)-1][s] > max:
            max = v[len(observations)-1][s]
            smax = s
    statesSeq = path[smax]
    for i in range(len(statesSeq)):
        if statesSeq[i] == "rainy":
            statesSeq[i] = "R"
        else:
            statesSeq[i] = "S"
    seq = "".join(statesSeq)
    print("This is the path probabilities matrix:")
    print(v)
    print()
    print("This is the result:")
    print(seq)

viterbi(states, start_p, observations, transition_p, emission_p)
