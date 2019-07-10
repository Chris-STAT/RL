import numpy as np
from env import Env
from Node import Node
from MCTS import MCTS 


root = Node()
M = MCTS(C = 15, symbol= -1)
for i in range(2000000):
    current_node = M.traversal(root)
    end_node = M.rollout(current_node)
    M.backpropagation(end_node)
    if i % 10000 == 0:
        print(i)


#######################################
#              Human                  #
#######################################

class Human:

    def __init__(self):
        pass

    def usr_play(self,env):

        action = [int(x) for x in input().split()]

        while action not in env.feasible_actions():
            print("This is not a legitimate action! Please input a another action.")
            action = [int(x) for x in input().split()]
        
        env.board[action[0], action[1]] = 1

def play(Env, H, root):
    
     print("Do you want to play? Yes/No")
     ans = input()
     while ans.lower() == 'yes':
            current_node = root 
            while not Env.game_over():
               children = current_node.get_children()
               V = [child.V_i for child in children]
               print(V)
               idx = np.argmax(V)
               Env.board = children[idx].state.copy()
               Env.draw_board()
               current_node = children[idx]
               if not Env.game_over():
                  print("Please take an action!")
                  H.usr_play(Env)
                  Env.draw_board()
               if not Env.game_over():
                 children = current_node.get_children()
                 states = [child.state for child in children]
                 for i in range(len(states)):
                    if np.array_equal(states[i], Env.board):
                        break 
                 idx2 = i 
                 current_node = children[idx2]
            if Env.winner == -1:
               print('Game over! The winner is {0}'.format('X'))
            elif Env.winner == 1:
               print('Game over! The winner is {0}'.format('O'))
            else:
               print('Game over! It is a draw!')
            Env.reset_env()
            print("Do you want to play again? Yes/No")
            ans = input()

     print("Session ended!")

# e = Env()
# h = Human()
# play(e,h, root)
