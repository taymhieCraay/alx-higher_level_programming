import sys

def solve_nqueens(n, queens, xy_diffs, xy_sums):

    p = len(queens)

    if p==n:

        print(queens)

        return

    for q in range(n):

        if q not in queens and p-q not in xy_diffs and p+q not in xy_sums:

            queens.append(q)

            xy_diffs.add(p-q)

            xy_sums.add(p+q)

            solve_nqueens(n, queens, xy_diffs, xy_sums)

            queens.pop()

            xy_diffs.remove(p-q)

            xy_sums.remove(p+q)



def main():

    if len(sys.argv) != 2:

        print("Usage: nqueens N")

        sys.exit(1)



    try:

        n = int(sys.argv[1])

    except ValueError:

        print("N must be a number")

        sys.exit(1)



    if n < 4:

        print("N must be at least 4")

        sys.exit(1)



    solve_nqueens(n, [], set(), set())



if name == "main":

    main()
