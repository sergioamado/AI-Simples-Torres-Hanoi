from HanoiProblem import HanoiProblem

class HanoiEnvironment:
    """Representa o ambiente do problema das Torres de Hanói."""

    def __init__(self, num_disks=5):
        """Inicializa o ambiente com um problema das Torres de Hanói."""
        self.problem = HanoiProblem(num_disks)
        self.state = self.problem.initial

    def execute_action(self, action):
        """Executa uma ação no ambiente.  Trata ações inválidas."""
        if action in self.problem.actions(self.state):
            self.state = self.problem.result(self.state, action)
        else:
            print(f"Ação inválida: {action} no estado {self.state}. Ação: {action}") # Log da ação inválida
            # Lançar uma exceção seria outra opção: raise ValueError("Ação inválida")

    def is_done(self):
        """Verifica se o problema foi resolvido."""
        return self.problem.goal_test(self.state)