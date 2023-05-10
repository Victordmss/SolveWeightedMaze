from grid import Grid
import argparse


# This function allows us to convert the source file gave into the command line into a matrix
def convert_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("grid_file_name")
    arg = parser.parse_args()
    with open(arg.grid_file_name) as f:
        text_grid = f.read()
    return text_to_matrix(text_grid)


# This function allows us to convert the grid in .txt format into a matrix easier to process with python.
def text_to_matrix(text: str):
    rows = text.strip().split('\n')  # Allows you to separate each line with the escape character "\n"
    matrix = [[''] * len(rows[0]) for _ in range(len(rows))]  # Every row has the same length
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            matrix[i][j] = rows[i][j]  # Convert the text into a matrix to facilitate data processing
    return matrix


# This function allows to run the grid until the end of the process
def run_the_grid(grid: Grid):
    while not grid.end_game:
        grid.next_time_step(grid.matrix)


def main():
    matrix = convert_file()   # Converting the file into a matrix
    grid = Grid(matrix)    # Creating a logical grid with the class Grid
    run_the_grid(grid)   # Processing the grid
    print(grid.end_score)


if __name__ == '__main__':
    main()
