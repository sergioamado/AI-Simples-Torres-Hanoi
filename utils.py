def print_state(state):
    """Imprime o estado do jogo Torres de Hanói formatado."""
    for i, peg in enumerate(state):
        print(f"Haste {i}: {list(peg)}")
    print()

def action_to_string(action):
    """Converte uma ação (tupla) em uma texto."""
    if not action:
        return "Nenhuma ação"
    return f"Mova o disco da haste {action[0] + 1} para a haste {action[1] + 1}"

def print_solution(solution):
    """Imprime a solução."""
    if not solution:
        print("Nenhuma solução encontrada.")
        return

    print("Solução:")
    for i, action in enumerate(solution):
        print(f"{i+1}. {action_to_string(action)}")