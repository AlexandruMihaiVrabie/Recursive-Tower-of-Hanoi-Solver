def hanoi_solver(n):
    rods = [[], [], []]
    for i in range(n, 0, -1):
        rods[0].append(i)

    history = []
    snapshot = f"{rods[0]} {rods[1]} {rods[2]}"

    history.append(snapshot)

    def solve(n, source, target, auxiliary):
        if n > 0:
            solve(n-1, source, auxiliary, target)

            disk = rods[source].pop()
            rods[target].append(disk)
            snapshot = f"{rods[0]} {rods[1]} {rods[2]}"
            history.append(snapshot)

            solve(n-1, auxiliary, target, source)

    solve(n, 0, 2, 1)

    return "\n".join(history)


print(hanoi_solver(5))
