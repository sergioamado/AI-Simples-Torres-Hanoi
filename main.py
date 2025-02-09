from HanoiEnvironment import HanoiEnvironment
from HanoiAgent import HanoiAgent
from utils import print_state, print_solution

if __name__ == "__main__":
    num_disks = 5
    env = HanoiEnvironment(num_disks=num_disks)
    agent = HanoiAgent()

    print("Estado inicial:")
    print_state(env.state)

    solution = agent.solve(env)

    print_solution(solution) # Imprime a solução de forma descritiva.

    agent.execute_actions(env, solution)

    print("Estado final:")
    print_state(env.state)