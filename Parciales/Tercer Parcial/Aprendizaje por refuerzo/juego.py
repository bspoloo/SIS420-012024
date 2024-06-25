import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Dimensiones del rompecabezas
ROWS = 4
COLS = 5
IMAGE_PATH = r"F:\acceso\7.- septimo semestre\Inteligencia artificial I\SIS420-012024\Parciales\Tercer Parcial\Aprendizaje por refuerzo\gato.jpg"


class Game:
    def __init__(self, rows, cols, image_path, root):
        self.rows = rows
        self.cols = cols
        self.image_path = image_path
        self.root = root
        
        self.piece_width = 0
        self.piece_height = 0
        self.pieces = []
        self.pieces_original = []
        
        self.load_image()
        self.shuffle_pieces()
        self.create_buttons()
    
    def load_image(self):
        image = Image.open(self.image_path)
        image = image.resize((800, 640))  # Ajusta el tamaño de la imagen según sea necesario
        self.piece_width = image.width // self.cols
        self.piece_height = image.height // self.rows
        
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                x = j * self.piece_width
                y = i * self.piece_height
                piece = image.crop((x, y, x + self.piece_width, y + self.piece_height))
                row.append(piece)
            self.pieces.append(row)
            self.pieces_original.append(row.copy())  # Guardar una copia de las piezas originales
        
        self.pieces[self.rows-1][self.cols-1] = None  # La última pieza es la pieza vacía (sin imagen)
    
    def shuffle_pieces(self):
        flat_pieces = [item for sublist in self.pieces for item in sublist]
        random.shuffle(flat_pieces)
        for i in range(self.rows):
            for j in range(self.cols):
                self.pieces[i][j] = flat_pieces[i * self.cols + j]
    
    def click_piece(self, row, col):
        # Intenta mover la pieza seleccionada
        if row > 0 and self.pieces[row-1][col] is None:  # Mover hacia arriba
            self.pieces[row-1][col], self.pieces[row][col] = self.pieces[row][col], self.pieces[row-1][col]
        elif row < self.rows-1 and self.pieces[row+1][col] is None:  # Mover hacia abajo
            self.pieces[row+1][col], self.pieces[row][col] = self.pieces[row][col], self.pieces[row+1][col]
        elif col > 0 and self.pieces[row][col-1] is None:  # Mover hacia la izquierda
            self.pieces[row][col-1], self.pieces[row][col] = self.pieces[row][col], self.pieces[row][col-1]
        elif col < self.cols-1 and self.pieces[row][col+1] is None:  # Mover hacia la derecha
            self.pieces[row][col+1], self.pieces[row][col] = self.pieces[row][col], self.pieces[row][col+1]
        else:
            return False
        
        self.update_display()
        return True
    
    def update_display(self):
        # Actualizar la interfaz gráfica con las piezas actuales
        for i in range(self.rows):
            for j in range(self.cols):
                piece = self.pieces[i][j]
                if piece is not None:
                    photo = ImageTk.PhotoImage(piece)
                    self.buttons[i][j].config(image=photo)
                    self.buttons[i][j].image = photo
                else:
                    self.buttons[i][j].config(image='')
        
        self.root.update_idletasks()
    
    def check_win(self):
        # Verificar si todas las piezas están en la posición correcta
        for i in range(self.rows):
            for j in range(self.cols):
                if self.pieces[i][j] is not None and (self.pieces[i][j] != self.pieces_original[i][j]):
                    return False
        return True
    
    def create_buttons(self):
        self.buttons = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                if self.pieces[i][j] is not None:
                    photo = ImageTk.PhotoImage(self.pieces[i][j])
                    button = tk.Button(self.root, image=photo, command=lambda row=i, col=j: self.click_piece(row, col))
                    button.image = photo
                else:
                    button = tk.Button(self.root)
                button.grid(row=i, column=j, padx=2, pady=2)
                row.append(button)
            self.buttons.append(row)

class Agent:
    def __init__(self, game, learning_rate=0.1, discount_factor=0.9, exploration_rate=1):
        self.game = game
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.q_table = {}
        self.actions = ['up', 'down', 'left', 'right']
        
        # Inicializar la tabla Q con valores arbitrarios
        for i in range(game.rows):
            for j in range(game.cols):
                state = (i, j)
                self.q_table[state] = {action: 0 for action in self.actions}
    
    def choose_action(self, state):
        # Epsilon-greedy para seleccionar una acción
        if random.uniform(0, 1) < self.exploration_rate:
            return random.choice(self.actions)
        else:
            # Seleccionar la acción con el valor Q máximo
            return max(self.q_table[state], key=self.q_table[state].get)
    
    def update_q_table(self, state, action, reward, next_state):
        # Actualizar la tabla Q según el algoritmo Q-Learning
        max_next_q = max(self.q_table[next_state].values()) if next_state in self.q_table else 0
        current_q = self.q_table[state][action]
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_next_q - current_q)
        self.q_table[state][action] = new_q
    
    def train(self, num_episodes=100):
        for episode in range(num_episodes):
            self.game.shuffle_pieces()
            current_state = (self.game.rows-1, self.game.cols-1)  # Estado inicial (posición vacía)
            done = False
            while not done:
                action = self.choose_action(current_state)
                row, col = current_state
                if action == 'up' and row > 0:
                    new_state = (row - 1, col)
                elif action == 'down' and row < self.game.rows - 1:
                    new_state = (row + 1, col)
                elif action == 'left' and col > 0:
                    new_state = (row, col - 1)
                elif action == 'right' and col < self.game.cols - 1:
                    new_state = (row, col + 1)
                else:
                    continue  # Acción inválida, saltar este paso
                
                reward = 1 if self.game.click_piece(new_state[0], new_state[1]) else -1
                self.update_q_table(current_state, action, reward, new_state)
                print (f"episodio: {episode}, Estado actual: {current_state}, Acción: {action}, Nuevo estado: {new_state}, Recompensa: {reward}")
                current_state = new_state
                done = self.game.check_win()
                self.game.update_display()
                self.game.root.update()  # Actualizar la ventana principal de tkinter
            messagebox.showinfo("Episodio completado", f"Episodio {episode + 1} completado.")

# Configuración de la interfaz gráfica y juego
root = tk.Tk()
root.title("Rompecabezas")
game = Game(ROWS, COLS, IMAGE_PATH, root)
agent = Agent(game)
# Entrenar al agente
agent.train(num_episodes=10)
root.mainloop()