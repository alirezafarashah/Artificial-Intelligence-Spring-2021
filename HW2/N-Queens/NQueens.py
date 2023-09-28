import time


class NQueens:
    def __init__(self, n):
        self.n = n
        self.variables = list(range(n))
        self.domains = {var: list(range(n)) for var in self.variables}
        self.remaining_domain = {var: list(range(n)) for var in self.variables}
        self.deleted = {var: [] for var in self.variables}
        self.rows = [0] * n
        self.up_diagonal = [0] * (2 * n - 1)
        self.down_diagonal = [0] * (2 * n - 1)

    def is_complete(self, assignment):
        return len(assignment) == self.n

    def assign(self, var, val, assignment):
        assignment[var] = val
        self.update_conflicts(var, val, False)
        forward_checking(self, var, val, assignment)

    def unassign(self, var, val, assignment):
        self.update_conflicts(var, val, True)
        del assignment[var]

    def update_dom(self, var):
        for (x, y) in self.deleted[var]:
            self.remaining_domain[x].append(y)
        self.deleted[var] = []

    def update_conflicts(self, var, val, removed):
        t = 1
        if removed:
            t = -1
        self.rows[val] += t
        self.down_diagonal[var - val + self.n - 1] += t
        self.up_diagonal[var + val] += t

    def number_of_conflicts(self, var, val, assignment):
        res = self.rows[val] + self.up_diagonal[var + val] + self.down_diagonal[var - val + self.n - 1]
        if var in assignment:
            res -= 3
        return res


def forward_checking(csp, var, val, assignment):
    for neighbor in csp.domains[var]:
        if neighbor not in assignment:
            for value in csp.remaining_domain[neighbor][:]:
                if not queen_is_consistent(neighbor, value, var, val):
                    csp.remaining_domain[neighbor].remove(value)
                    csp.deleted[var].append((neighbor, value))


def queen_is_consistent(X, x, Y, y):
    return X == Y or (x != y and X + x != Y + y and X - x != Y - y)


def lcv(var, x, csp):
    return -(min(csp.n - var, csp.n - x) + min(var, x) + min(csp.n - var, x) + min(var, csp.n - x))


def order_domain_values(var, csp):
    domain_values = [x for x in csp.remaining_domain[var]]
    domain_values.sort(key=lambda x: lcv(var, x, csp))
    return domain_values


def select_unassigned_variable(assignment, csp):
    unassigned_vars = [var for var in csp.variables if var not in assignment]
    unassigned_vars.sort(key=lambda var: len(csp.remaining_domain[var]))
    return unassigned_vars[0]


def back_tracking(assignment, csp):
    if csp.is_complete(assignment):
        return assignment
    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, csp):
        if csp.number_of_conflicts(var, value, assignment) == 0:
            csp.assign(var, value, assignment)
            res = back_tracking(assignment, csp)
            if res is not False:
                return res
            csp.unassign(var, value, assignment)
            csp.update_dom(var)
    return False


def print_queens(queens, N):
    res = ""
    for i in range(N):
        for j in range(N):
            if queens[j] == i:
                res += 'o'
            else:
                res += '-'
        res += '\n'
    print(res)


n = int(input())
# start_time = time.time()
nQueens = NQueens(n)
print_queens(back_tracking({}, nQueens), n)
# end_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))
