import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))
running = True
font = pygame.font.SysFont(["segoeuisymbol", "dejavusans", "arial"], 40)

light = (240, 217, 181)
dark = (181, 136, 99)
squaresize = 80

UNICODE_PIECES = {
    'K': 'wK', 'Q': 'wQ', 'R': 'wR', 'B': 'wB', 'N': 'wN', 'P': 'wP',
    'k': 'bK', 'q': 'bQ', 'r': 'bR', 'b': 'bB', 'n': 'bN', 'p': 'bP'
}

gameboard = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]


def board(screen):
    for row in range(8):
        for col in range(8):
            colour = light if (row + col)%2 == 0 else dark

            x = row * squaresize + 80
            y = col * squaresize + 80

            pygame.draw.rect(screen, colour, (x, y, squaresize, squaresize))
def drawpieces(screen, board, square_size):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "--":
                symbol = UNICODE_PIECES[piece]
                
                # Render text (black pieces drawn dark gray, white pieces drawn white/gold)
                color = (40, 40, 40) if piece.islower() else (180, 40, 40)
                text_surface = font.render(symbol, True, color)
                
                # Center the character inside the square
                x = (col * square_size  + (square_size - text_surface.get_width()) // 2 ) + 80
                y = (row * square_size  + (square_size - text_surface.get_height()) // 2) + 80
                
                screen.blit(text_surface, (x, y))

while running:
    pygame.display.set_caption('chess')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

    



    
    board(screen)
    drawpieces(screen, gameboard, squaresize)
     
    pygame.display.update()
pygame.quit()
                 


