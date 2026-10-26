import sys
import random
import pygame

# Configurações iniciais
FPS = 60
W_WIDTH, W_HEIGHT = 640, 480
WHITE = (255, 255, 255)

pygame.init()

SCREEN = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption("Rato em busca do Queijo")
clock = pygame.time.Clock()


rato = pygame.image.load("rato.jpg").convert()
rato.set_colorkey((255, 255, 255)) # Remove o fundo branco
rato = pygame.transform.scale(rato, (55, 55))


queijo = pygame.image.load("queijo.jpg").convert()
queijo.set_colorkey((255, 255, 255)) # Remove o fundo branco
queijo = pygame.transform.scale(queijo, (45, 45))

#
rato_rect = rato.get_rect()
queijo_rect = queijo.get_rect()


rato_rect.center = (W_WIDTH // 2, W_HEIGHT // 2)


def reposicionar_queijo():
    queijo_rect.x = random.randint(20, W_WIDTH - queijo_rect.width - 20)
    queijo_rect.y = random.randint(20, W_HEIGHT - queijo_rect.height - 20)

reposicionar_queijo()

pontos = 0
fonte = pygame.font.SysFont("Arial", 24)

while True:
    SCREEN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentação do rato
    if pygame.key.get_focused():
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            rato_rect.x -= 5
        if key[pygame.K_RIGHT]:
            rato_rect.x += 5
        if key[pygame.K_UP]:
            rato_rect.y -= 5
        if key[pygame.K_DOWN]:
            rato_rect.y += 5

    
    rato_rect.clamp_ip(SCREEN.get_rect())

    # Checa colisão
    if rato_rect.colliderect(queijo_rect):
        pontos += 1
        print(f"Queijo coletado! Pontuação: {pontos}")
        reposicionar_queijo()

    # Desenha os elementos na tela
    SCREEN.blit(queijo, queijo_rect)
    SCREEN.blit(rato, rato_rect)

    # Exibe a pontuação
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, (0, 0, 0))
    SCREEN.blit(texto_pontos, (10, 10))

    pygame.display.update()
    clock.tick(FPS)