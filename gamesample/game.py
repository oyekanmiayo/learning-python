#import draw
#from draw import draw_game
import draw as draw2

def play_game():
    return "Playing Sudoku"

def main():
    result = play_game()
    draw2.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()