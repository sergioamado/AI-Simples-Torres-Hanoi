from search import astar_search

class HanoiAgent:
    """Um agente que resolve o problema das Torres de Hanói usando A*."""

    def solve(self, environment):
        """Encontra uma solução para o problema no ambiente usando A*."""
        problem = environment.problem
        solution_node = astar_search(problem) 
        return solution_node.solution() if solution_node else [] 

    def execute_actions(self, environment, actions):
        """Executa uma sequência de ações no ambiente."""
        for action in actions:
            environment.execute_action(action)