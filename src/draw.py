import pygame

def draw_window():
    pygame.init()

    WINDOW = pygame.display.set_mode((336,336)) 

    pygame.display.set_caption("Press Enter When Done")
    white = (255,255,255)
    black = (0,0,0)

    WINDOW.fill(white)

    def draw(WINDOW, x, y):
        pygame.draw.rect(WINDOW,black,(x,y,36,36))

    RUN = True
    pressed = False

    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    RUN = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pressed = False
            elif event.type == pygame.MOUSEMOTION and pressed == True:
                (x,y) = pygame.mouse.get_pos()
                draw(WINDOW,x,y)
        pygame.display.update()
    pygame.image.save(WINDOW,"img/screenshot.jpg")
    pygame.quit()
    return True
    

