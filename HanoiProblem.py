from search import Problem

class HanoiProblem(Problem):
    """Define o problema das Torres de Hanói."""

    def __init__(self, num_disks=5):
        """Inicializa o problema com o número de discos."""
        self.num_disks = num_disks
        initial_state = (tuple(range(num_disks, 0, -1)), (), ()) 
        goal_state = ((), (), tuple(range(num_disks, 0, -1))) 
        super().__init__(initial_state, goal_state)

    def actions(self, state):
        """Retorna as ações válidas para um determinado estado."""
        actions = []
        for i in range(3): 
            if state[i]:
                disk = state[i][-1]
                for j in range(3): 
                    if i != j and (not state[j] or state[j][-1] > disk): 
                        actions.append((i, j))
        return actions

    def result(self, state, action):
        """Retorna o estado resultante da aplicação de uma ação."""
        state = [list(peg) for peg in state] # Converte tuplas em listas
        disk = state[action[0]].pop()
        state[action[1]].append(disk)
        return tuple(tuple(peg) for peg in state) 

    def goal_test(self, state):
        """Verifica se o estado é o estado objetivo."""
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Retorna o custo do caminho, que é sempre 1 para cada ação."""
        return c + 1

    def h(self, node):
        """Função heurística admissível (nunca superestima)."""

        return sum(len(peg) for peg in node.state[:-1])