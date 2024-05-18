import pygame
import sys
import random

def reset():
    global piłka_rect, pad_rect, ruch_x, ruch_y
    piłka_rect.center = (szerokość_ekranu // 2, wysokość_ekranu // 2)
    pad_rect.centerx = szerokość_ekranu // 2
    ruch_x = 5
    ruch_y = 5

def generuj_cegielki():
    global cegielki, poziom
    liczba_cegielek = 10 + (poziom - 1) * 5  # Zwiększ liczbę cegiełek na każdym poziomie
    cegielki = [pygame.Rect(random.randint(0, szerokość_ekranu - 50), random.randint(50, 200), 50, 20) for _ in range(liczba_cegielek)]

def przejscie_na_kolejny_poziom():
    global poziom, punkty
    poziom += 1
    if poziom > 5:
        return True  # Gracz wygrał
    punkty = 0
    reset()
    generuj_cegielki()
    return False

pygame.init()

szerokość_ekranu = 644
wysokość_ekranu = 600

ekran = pygame.display.set_mode([szerokość_ekranu, wysokość_ekranu])
zegar = pygame.time.Clock()

# Załaduj obraz tła
obraz_tla = pygame.image.load('background.png').convert()

pad = pygame.image.load('pad.png')
pad_rect = pad.get_rect()
pad_rect.bottom = wysokość_ekranu  # Ustawia dolną krawędź pada na dolnej krawędzi ekranu
pad_rect.centerx = szerokość_ekranu // 2  # Ustawia pad na środku ekranu

piłka = pygame.image.load('ball.png')
piłka_rect = piłka.get_rect()
piłka_rect.center = (szerokość_ekranu // 2, wysokość_ekranu // 2)

ruch_x = 5
ruch_y = 5

punkty = 0
poziom = 1

# Losowe generowanie cegiełek na ekranie
generuj_cegielki()

game_work = True
while game_work:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_work = False
    
    # Obsługa sterowania padem
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and pad_rect.left > 0:
        pad_rect.x -= 5
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and pad_rect.right < szerokość_ekranu:
        pad_rect.x += 5

    # Ruch piłki
    piłka_rect = piłka_rect.move(ruch_x, ruch_y)
    
    # Odbicie piłki od krawędzi ekranu
    if piłka_rect.left < 0 or piłka_rect.right > szerokość_ekranu:
        ruch_x = -ruch_x
    if piłka_rect.top < 0:
        ruch_y = -ruch_y
    
    # Odbicie piłki od padu
    if piłka_rect.colliderect(pad_rect):
        ruch_y = -ruch_y
    
    # Sprawdzenie, czy piłka wypadła poza pad
    if piłka_rect.bottom > wysokość_ekranu:
        reset()
    
    # Kolizja piłki z cegiełkami
    for cegielka in cegielki[:]:
        if piłka_rect.colliderect(cegielka):
            cegielki.remove(cegielka)
            punkty += random.randint(1, 12)
            ruch_y = -ruch_y
            break
    
    # Sprawdzenie, czy wszystkie cegiełki zostały zebrane
    if not cegielki:
        generuj_cegielki()
    
    # Sprawdzenie, czy gracz osiągnął 1000 punktów
    if punkty >= 250:
        if przejscie_na_kolejny_poziom():
            game_work = False
            break
    
    # Rysowanie na ekranie
    ekran.blit(obraz_tla, (0, 0))
    ekran.blit(pad, pad_rect)
    ekran.blit(piłka, piłka_rect)
    
    # Rysowanie cegiełek
    for cegielka in cegielki:
        pygame.draw.rect(ekran, (255, 0, 0), cegielka)
    
    # Wyświetlanie punktów i poziomu
    font = pygame.font.SysFont(None, 36)
    tekst_punkty = font.render("Punkty: " + str(punkty), True, (255, 255, 255))
    tekst_poziom = font.render("Poziom: " + str(poziom), True, (255, 255, 255))
    ekran.blit(tekst_punkty, (10, 10))
    ekran.blit(tekst_poziom, (10, 50))
    
    pygame.display.flip()
    zegar.tick(60)

# Wyświetlanie komunikatu o wygranej
if poziom > 5:
    font = pygame.font.SysFont(None, 48)
    tekst_wygrana = font.render("Wygrana! Zdobyłeś wszystkie poziomy!", True, (255, 255, 255))
    ekran.blit(tekst_wygrana, (szerokość_ekranu // 2 - tekst_wygrana.get_width() // 2, wysokość_ekranu // 2 - tekst_wygrana.get_height() // 2))
    pygame.display.flip()

# Czekaj, aż użytkownik zamknie okno
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
