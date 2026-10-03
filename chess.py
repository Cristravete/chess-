import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))
running = True
font = pygame.font.SysFont(["segoeuisymbol", "dejavusans", "arial"], 40)

light = (240, 217, 181)
dark = (181, 136, 99)
squaresize = 80
clickedpos = None
startpos = None
endpos = None
activebox = None

row = 0
col = 0

pieces = {
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

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def iswhite(piece):
     return piece != '--' and piece.isupper()

def isblack(piece):
     return piece != '--' and piece.islower()

def isally(p1,p2):
     if p1 == '--' and p2 == '--':
          return False

     bothwhite = p1.isupper() and p2.isupper()
     bothblack = p1.islower() and p2.islower()

     return bothwhite or bothblack



def board(screen):

    for row in range(8):
        for col in range(8):
            colour = light if (row + col)%2 == 0 else dark

            x = col * squaresize + 80
            y = row * squaresize + 80

            pygame.draw.rect(screen, colour, (x, y, squaresize, squaresize))
def drawpieces(screen, board, square_size):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "--":
                letters = pieces[piece]
                
                # Render text (black pieces drawn dark gray, white pieces drawn white/gold)
                color = (40, 40, 40) if piece.islower() else (180,40,40)
                text_surface = font.render(letters, True, color)
                
                # Center the character inside the square
                x = (col * square_size  + (square_size - text_surface.get_width()) // 2 ) + 80
                y = (row * square_size  + (square_size - text_surface.get_height()) // 2) + 80
                
                screen.blit(text_surface, (x, y))

def getposition(mouseclick):
    x,y = mouseclick

    col = (x - 80) // squaresize
    row = (y - 80) // squaresize


    if 0 <= row <= 8 and 0 <= col <= 8:
    
        #print(alph[row-1]+str(col +1))
        return row, col
    
    
    return None
    

while running:
    
    pygame.display.set_caption('chess')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
             clickedpos = getposition(event.pos)
             if clickedpos is not None:
                         if activebox is None:
                             r, c = clickedpos

                             if gameboard[r][c] != '--':
                                 startpos = clickedpos
                                 activebox = clickedpos
                         else:
                             startr, startc = startpos
                             endr, endc = clickedpos

                             startpiece = gameboard[startr][startc]
                             endpiece = gameboard[endr][endc]
                             
                             if isally(startpiece, endpiece):
                                     print('nono hun')
                             else:
                                     gameboard[endr][endc] = gameboard[startr][startc]
                                     gameboard[startr][startc] = '--'
                                     
                                     activebox = None
                                     startpos = None

                            
            
    board(screen)
    drawpieces(screen, gameboard, squaresize)

    if activebox is not None:
         row, col = activebox
         x = col * squaresize + 80
         y = row * squaresize + 80
        
         pygame.draw.rect(screen, (255,0,0), (x, y, squaresize, squaresize), 5)

    pygame.display.update()
pygame.quit()




