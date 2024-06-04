#El agente tiene una función de valor (cargada desde un archivo) que asigna a cada estado posible del tablero un valor basado en la recompensa esperada. 
# Durante la fase de explotación, el agente utiliza esta función de valor para seleccionar la acción que cree que le dará la mayor recompensa.
# En el método move, el agente examina todos los movimientos válidos que puede hacer en el tablero actual. Para cada movimiento, 
# calcula el valor del estado del tablero que resultaría de ese movimiento. Luego, elige el movimiento que resulta en el estado con el valor más alto.

import pickle

class Agent():
    def __init__(self, value_function_path):
        with open(value_function_path, 'rb') as handle:
            self.value_function = pickle.load(handle)
        self.symbol = 1

    def move(self, board):
        valid_moves = board.valid_moves()
        # vamos a la posición con más valor
        max_value = -1000
        for row, col in valid_moves:
            next_board = board.state.copy()
            next_board[row, col] = self.symbol
            next_state = str(next_board.reshape(4*4))
            value = 0 if self.value_function.get(next_state) is None else self.value_function.get(next_state)
            if value >= max_value:
                max_value = value
                best_row, best_col = row, col
        return best_row, best_col
