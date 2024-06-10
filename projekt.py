import os
import pygame
import sys
import random
import pickle

# Stałe do cen w sklepiku
CENY = {
    "basketball": 400,
    "football": 525,
    "geometry_dash": 1500,
    "super_mario": 3000,
    "point": 2000
}

# Globalne zmienne
punkty = 0
czas_w_grze = 0
zakupione_pilki = {
    "default": True,
    "basketball": False,
    "football": False,
    "geometry_dash": False,
    "super_mario": False
}
aktualna_pilka = "default"
poziom = 1
ruch_x = 5
ruch_y = 5
ruch_pada = 5
odtwarzaj_point_wav = False
życia = 8  # Dodane zmienna dla liczby żyć

def reset():
    global piłka_rect, pad_rect, ruch_x, ruch_y
    piłka_rect.center = (szerokość_ekranu // 2, wysokość_ekranu // 2)
    pad_rect.centerx = szerokość_ekranu // 2
    ruch_x = 5
    ruch_y = 5

def generuj_cegielki():
    global cegielki
    liczba_cegielek = 10 + (poziom - 1) * 5
    cegielki = [pygame.Rect(random.randint(0, szerokość_ekranu - 50), random.randint(50, 200), 50, 20) for _ in range(liczba_cegielek)]

def przejscie_na_kolejny_poziom():
    global poziom
    poziom += 1
    if poziom > 13:
        return True  # Gracz wygrał
    reset()
    generuj_cegielki()
    return False

def zapisz_stan_gry():
    global stan_gry
    stan_gry = {
        "piłka_rect": piłka_rect.topleft,
        "pad_rect": pad_rect.topleft,
        "ruch_x": ruch_x,
        "ruch_y": ruch_y,
        "punkty": punkty,
        "poziom": poziom,
        "cegielki": [cegielka.topleft for cegielka in cegielki],
        "czas_w_grze": czas_w_grze,
        "zakupione_pilki": zakupione_pilki,
        "aktualna_pilka": aktualna_pilka,
        "odtwarzaj_point_wav": odtwarzaj_point_wav,
        "życia": życia  # Dodano życie do stanu gry
    }
    with open("stan_gry.pkl", "wb") as plik:
        pickle.dump(stan_gry, plik)

def wczytaj_stan_gry():
    global piłka_rect, pad_rect, ruch_x, ruch_y, punkty, poziom, cegielki, czas_w_grze, zakupione_pilki, aktualna_pilka, odtwarzaj_point_wav, życia
    if os.path.exists("stan_gry.pkl"):
        with open("stan_gry.pkl", "rb") as plik:
            stan_gry = pickle.load(plik)
            piłka_rect.topleft = stan_gry["piłka_rect"]
            pad_rect.topleft = stan_gry["pad_rect"]
            ruch_x = stan_gry["ruch_x"]
            ruch_y = stan_gry["ruch_y"]
            punkty = stan_gry["punkty"]
            poziom = stan_gry["poziom"]
            cegielki = [pygame.Rect(pos, (50, 20)) for pos in stan_gry["cegielki"]]
            czas_w_grze = stan_gry["czas_w_grze"]
            zakupione_pilki = stan_gry["zakupione_pilki"]
            aktualna_pilka = stan_gry["aktualna_pilka"]
            odtwarzaj_point_wav = stan_gry["odtwarzaj_point_wav"]
            życia = stan_gry["życia"]  # Wczytanie życia
    else:
        reset()
        generuj_cegielki()

def odtworz_dzwiek(plik):
    pygame.mixer.Sound(plik).play()

def rysuj_tekst(tekst, pozycja, rozmiar=36):
    font = pygame.font.SysFont(None, rozmiar)
    render_tekst = font.render(tekst, True, (255, 255, 255))
    ekran.blit(render_tekst, pozycja)

def rysuj_życia():
    for i in range(życia):
        ekran.blit(serce, (10 + i * 25, wysokość_ekranu - 30))

def pokaz_menu():
    global czas_w_grze
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "nowa_gra"
                elif event.key == pygame.K_2:
                    return "kontynuuj_gre"
                elif event.key == pygame.K_3:
                    return "sklepik"
                elif event.key == pygame.K_4:
                    zapisz_stan_gry()
                    rysuj_tekst("Zamykanie gry.exe", (szerokość_ekranu // 2 - 100, wysokość_ekranu // 2))
                    pygame.display.flip()
                    odtworz_dzwiek("shutdown.mp3")
                    pygame.time.wait(2000)
                    pygame.quit()
                    sys.exit()

        ekran.blit(obraz_tla, (0, 0))
        rysuj_tekst("Menu", (szerokość_ekranu // 2 - 50, 50), 48)
        rysuj_tekst("1. Nowa Gra", (100, 150))
        rysuj_tekst("2. Kontynuuj Grę", (100, 200))
        rysuj_tekst("3. Sklepik", (100, 250))
        rysuj_tekst("4. Wyjście", (100, 300))
        rysuj_tekst(f"Czas w grze: {czas_w_grze // 60} minut", (100, 350))
        rysuj_tekst("Version 3.9 June 4-st update Arkanoib by © Bazyli", (100, 400))
        pygame.display.flip()
        zegar.tick(43)

def sklepik():
    global punkty, aktualna_pilka, odtwarzaj_point_wav
    shop = True
    while shop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and punkty >= CENY["basketball"]:
                    punkty -= CENY["basketball"]
                    zakupione_pilki["basketball"] = True
                    aktualna_pilka = "basketball"
                elif event.key == pygame.K_2 and punkty >= CENY["football"]:
                    punkty -= CENY["football"]
                    zakupione_pilki["football"] = True
                    aktualna_pilka = "football"
                elif event.key == pygame.K_3 and punkty >= CENY["geometry_dash"]:
                    punkty -= CENY["geometry_dash"]
                    zakupione_pilki["geometry_dash"] = True
                    aktualna_pilka = "geometry_dash"
                elif event.key == pygame.K_4 and punkty >= CENY["super_mario"]:
                    punkty -= CENY["super_mario"]
                    zakupione_pilki["super_mario"] = True
                    aktualna_pilka = "super_mario"
                elif event.key == pygame.K_5 and punkty >= CENY["point"]:
                    punkty -= CENY["point"]
                    odtwarzaj_point_wav = True
                    print("Kupiono point.mp3")
                elif event.key == pygame.K_ESCAPE:
                    return

        ekran.blit(obraz_tla, (0, 0))
        rysuj_tekst("Sklepik", (szerokość_ekranu // 2 - 50, 50), 48)
        rysuj_tekst(f"Twoje punkty: {punkty}", (100, 100))

        # Wyświetlanie miniaturek piłek
        ekran.blit(basketball_mini, (100, 150))
        rysuj_tekst(f"1. Basketball - 400 pkt", (150, 150))
        ekran.blit(football_mini, (100, 200))
        rysuj_tekst(f"2. Football - 525 pkt", (150, 200))
        ekran.blit(geometry_dash_mini, (100, 250))
        rysuj_tekst(f"3. Geometry Dash - 1500 pkt", (150, 250))
        ekran.blit(super_mario_mini, (100, 300))
        rysuj_tekst(f"4. Super Mario - 3000 pkt", (150, 300))
        rysuj_tekst(f"5. Point.mp3 - 2000 pkt", (100, 350))
        rysuj_tekst("ESC - Powrót do menu", (100, 400))
        pygame.display.flip()
        zegar.tick(45)

pygame.init()

szerokość_ekranu = 644
wysokość_ekranu = 600

ekran = pygame.display.set_mode([szerokość_ekranu, wysokość_ekranu])
zegar = pygame.time.Clock()

# Ładowanie dźwięków
pygame.mixer.init()
odtworz_dzwiek("startup.wav")

# Ładowanie obrazów
try:
    obraz_tla = pygame.image.load('tlo.png').convert()
    pad = pygame.image.load('pad.png').convert_alpha()
    piłka = pygame.image.load('default_ball.png').convert_alpha()
    piłka = pygame.transform.scale(piłka, (40, 40))
    basketball = pygame.image.load('basketball.jpg').convert_alpha()
    basketball = pygame.transform.scale(basketball, (40, 40))
    football = pygame.image.load('football.png').convert_alpha()
    football = pygame.transform.scale(football, (40, 40))
    geometry_dash = pygame.image.load('geometry_dash.jpg').convert_alpha()
    geometry_dash = pygame.transform.scale(geometry_dash, (40, 40))
    super_mario = pygame.image.load('super_mario.jpg').convert_alpha()
    super_mario = pygame.transform.scale(super_mario, (40, 60))
    basketball_mini = pygame.transform.scale(basketball, (40, 40))
    football_mini = pygame.transform.scale(football, (40, 40))
    geometry_dash_mini = pygame.transform.scale(geometry_dash, (40, 40))
    super_mario_mini = pygame.transform.scale(super_mario, (40, 40))
except pygame.error as e:
    print(f"Błąd ładowania obrazów: {e}")
    sys.exit()

# Ładowanie obrazu serca po inicjalizacji pygame.display
serce = pygame.image.load('hearth.png').convert_alpha()
serce = pygame.transform.scale(serce, (20, 20))

piłka_rect = piłka.get_rect()
pad_rect = pad.get_rect(midbottom=(szerokość_ekranu // 2, wysokość_ekranu - 30))

reset()
generuj_cegielki()

while True:
    wybór = pokaz_menu()
    if wybór == "nowa_gra":
        reset()
        generuj_cegielki()
        poziom = 1
        punkty = 0
        czas_w_grze = 0
        życia = 8  # Resetuj życie na nową grę
    elif wybór == "kontynuuj_gre":
        wczytaj_stan_gry()
    elif wybór == "sklepik":
        sklepik()

    game_work = True
    while game_work:
        czas_w_grze += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                zapisz_stan_gry()
                odtworz_dzwiek("shutdown.mp3")
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    zapisz_stan_gry()
                    game_work = False
                    break

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and pad_rect.left > 0:
            pad_rect.x -= ruch_pada
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and pad_rect.right < szerokość_ekranu:
            pad_rect.x += ruch_pada

        piłka_rect = piłka_rect.move(ruch_x, ruch_y)
        
        if piłka_rect.left < 0 or piłka_rect.right > szerokość_ekranu:
            ruch_x = -ruch_x
        if piłka_rect.top < 0:
            ruch_y = -ruch_y
        
        if piłka_rect.colliderect(pad_rect):
            ruch_y = -ruch_y
        
        if piłka_rect.bottom > wysokość_ekranu:
            życia -= 1
            punkty -= 10
            if życia <= 0:
                game_work = False
                break
            reset()
        
        for cegielka in cegielki[:]:
            if piłka_rect.colliderect(cegielka):
                cegielki.remove(cegielka)
                punkty += random.randint(30, 69)
                if odtwarzaj_point_wav:
                    odtworz_dzwiek("point.wav")
                ruch_y = -ruch_y
                break
        
        if not cegielki:
            if przejscie_na_kolejny_poziom():
                game_work = False
                break
        
        ekran.blit(obraz_tla, (0, 0))
        ekran.blit(pad, pad_rect)
        
        # Wybór piłki
        if aktualna_pilka == "basketball":
            ekran.blit(basketball, piłka_rect)
        elif aktualna_pilka == "football":
            ekran.blit(football, piłka_rect)
        elif aktualna_pilka == "geometry_dash":
            ekran.blit(geometry_dash, piłka_rect)
        elif aktualna_pilka == "super_mario":
            ekran.blit(super_mario, piłka_rect)
        else:
            ekran.blit(piłka, piłka_rect)
        
        for cegielka in cegielki:
            pygame.draw.rect(ekran, (255, 0, 0), cegielka)
        
        rysuj_tekst(f"Punkty: {punkty}", (10, 10))
        rysuj_tekst(f"Poziom: {poziom}", (10, 50))
        rysuj_życia()
        
        pygame.display.flip()
        zegar.tick(45)  # Stała prędkość ticków: 45

    if poziom > 13:
        rysuj_tekst("Wygrana! Zdobyłeś wszystkie poziomy!", (szerokość_ekranu // 2 - 200, wysokość_ekranu // 2), 48)
        pygame.display.flip()
        pygame.time.wait(4000)
        pygame.quit()
        sys.exit()
    
    # Dodanie obsługi game over
    if życia <= 0:
        rysuj_tekst("Game Over! Straciłeś wszystkie życia!", (szerokość_ekranu // 2 - 200, wysokość_ekranu // 2), 48)
        pygame.display.flip()
        pygame.time.wait(4000)
        continue  # Powrót do menu