grid_x = 12
grid_y = 18

tetromino_width = 4

tetrominoes = {

    'I': [[0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],

    'O': [[1, 1],
          [1, 1]],

    'T': [[0, 1, 0],
          [1, 1, 1],
          [0, 0, 0]],

    'J': [[1, 0, 0],
          [1, 1, 1],
          [0, 0, 0]],

    'L': [[0, 0, 1],
          [1, 1, 1],
          [0, 0, 0]],

    'S': [[0, 1, 1],
          [1, 1, 0],
          [0, 0, 0]],

    'Z': [[1, 1, 0],
          [0, 1, 1],
          [0, 0, 0]]

}

colors = ["F92338"]
seed = 1
speed = [500, 100, 1, 0]
moves_limit = 500
move_algorithm = []
inspect_move_selection = False

# Genomes
population_size = 50
genomes = []
current_genome = 1
generation = 0

mutation_rate = 0.05
mutation_step = 0.2
