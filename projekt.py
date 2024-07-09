# -*- coding: utf-8 -*-

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
    "point": 2000,
    "bg1": 500,
    "bg2": 1000,
    "bg3": 1500,
    "bg4": 2000,
    "regen_życia": 1000  # Dodana cena regeneracji życia
}

# Globalne zmienne
punkty = 5000
czas_w_grze = 0
zakupione_pilki = {
    "default": True,
    "basketball": False,
    "football": False,
    "geometry_dash": False,
    "super_mario": False
}
zakupione_tła = {
    "default": True,
    "bg1": False,
    "bg2": False,
    "bg3": False,
    "bg4": False
}
aktualna_pilka = "default"
aktualne_tło = "default"
poziom = 1
ruch_x = 5
ruch_y = 5
ruch_pada = 5
odtwarzaj_point_wav = False
życia = 13

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
    if poziom > 50:
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
        "zakupione_tła": zakupione_tła,
        "aktualna_pilka": aktualna_pilka,
        "aktualne_tło": aktualne_tło,
        "odtwarzaj_point_wav": odtwarzaj_point_wav,
        "życia": życia
    }
    with open("stan_gry.pkl", "wb") as plik:
        pickle.dump(stan_gry, plik)

def wczytaj_stan_gry():
    global piłka_rect, pad_rect, ruch_x, ruch_y, punkty, poziom, cegielki, czas_w_grze, zakupione_pilki, zakupione_tła, aktualna_pilka, aktualne_tło, odtwarzaj_point_wav, życia
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
            zakupione_pilki = stan_gry.get("zakupione_pilki", zakupione_pilki)
            zakupione_tła = stan_gry.get("zakupione_tła", zakupione_tła)
            aktualna_pilka = stan_gry.get("aktualna_pilka", "default")
            aktualne_tło = stan_gry.get("aktualne_tło", "default")
            odtwarzaj_point_wav = stan_gry["odtwarzaj_point_wav"]
            życia = stan_gry["życia"]
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
        ekran.blit(serce, (10 + i * 25, wysokość_ekranu - 40))

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

        ekran.blit(tła[aktualne_tło], (0, 0))
        rysuj_tekst("Menu", (szerokość_ekranu // 2 - 50, 50), 48)
        rysuj_tekst("1. Nowa Gra", (100, 150))
        rysuj_tekst("2. Kontynuuj Grę", (100, 200))
        rysuj_tekst("3. Sklepik", (100, 250))
        rysuj_tekst("4. Wyjście", (100, 300))
        rysuj_tekst(f"Czas w grze: {czas_w_grze // 60000} minut", (100, 350))
        rysuj_tekst("Version 5.0 June update Arkanoid by © Bazyli", (100, 400))
        pygame.display.flip()
        zegar.tick(65)

def sklepik():
    global punkty, aktualna_pilka, aktualne_tło, odtwarzaj_point_wav, życia
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
                elif event.key == pygame.K_6 and punkty >= CENY["bg1"]:
                    punkty -= CENY["bg1"]
                    zakupione_tła["bg1"] = True
                    aktualne_tło = "bg1"
                elif event.key == pygame.K_7 and punkty >= CENY["bg2"]:
                    punkty -= CENY["bg2"]
                    zakupione_tła["bg2"] = True
                    aktualne_tło = "bg2"
                elif event.key == pygame.K_8 and punkty >= CENY["bg3"]:
                    punkty -= CENY["bg3"]
                    zakupione_tła["bg3"] = True
                    aktualne_tło = "bg3"
                elif event.key == pygame.K_9 and punkty >= CENY["bg4"]:
                    punkty -= CENY["bg4"]
                    zakupione_tła["bg4"] = True
                    aktualne_tło = "bg4"
                elif event.key == pygame.K_r and punkty >= CENY["regen_życia"]:
                    punkty -= CENY["regen_życia"]
                    życia = 13
                elif event.key == pygame.K_q:
                    return

        ekran.blit(tła[aktualne_tło], (0, 0))
        rysuj_tekst("Sklepik", (szerokość_ekranu // 2 - 50, 50), 48)
        rysuj_tekst(f"Twoje punkty: {punkty}", (100, 100))
        rysuj_tekst("1. Basketball - 400 punktów", (100, 150))
        ekran.blit(pygame.image.load("basketball.png"), (400, 150))  # Przykładowy obrazek miniatury
        rysuj_tekst("2. Football - 525 punktów", (100, 200))
        ekran.blit(pygame.image.load("football.png"), (400, 200))  # Przykładowy obrazek miniatury
        rysuj_tekst("3. Geometry Dash - 1500 punktów", (100, 250))
        ekran.blit(pygame.image.load("geometry_dash.png"), (400, 250))  # Przykładowy obrazek miniatury
        rysuj_tekst("4. Super Mario - 3000 punktów", (100, 300))
        ekran.blit(pygame.image.load("super_mario.png"), (400, 300))  # Przykładowy obrazek miniatury
        rysuj_tekst("5. Point.mp3 - 2000 punktów", (100, 350))
        rysuj_tekst("6. Tło 1 - 500 punktów", (100, 400))
        ekran.blit(pygame.image.load("bg1.png"), (400, 400))  # Przykładowy obrazek miniatury
        rysuj_tekst("7. Tło 2 - 1000 punktów", (100, 450))
        ekran.blit(pygame.image.load("bg2.png"), (400, 450))  # Przykładowy obrazek miniatury
        rysuj_tekst("8. Tło 3 - 1500 punktów", (100, 500))
        ekran.blit(pygame.image.load("bg3.png"), (400, 500))  # Przykładowy obrazek miniatury
        rysuj_tekst("9. Tło 4 - 2000 punktów", (100, 550))
        ekran.blit(pygame.image.load("bg4.png"), (400, 550))  # Przykładowy obrazek miniatury
        rysuj_tekst("R. Regeneracja żyć - 1000 punktów", (100, 600))
        rysuj_tekst("Q. Powrót", (100, 650))
        pygame.display.flip()
        zegar.tick(65)

# Inicjalizacja Pygame
pygame.init()

# Rozdzielczość ekranu
szerokość_ekranu, wysokość_ekranu = 1000, 670
ekran = pygame.display.set_mode((szerokość_ekranu, wysokość_ekranu))

# Tytuł okna
pygame.display.set_caption("Arkanoid by © Bazyli 5.0 June update")

# Zegar
zegar = pygame.time.Clock()

# Ładowanie obrazków i dźwięków
piłka_img = pygame.image.load("ball.png")
basketball_img = pygame.image.load("basketball.png")
football_img = pygame.image.load("football.png")
geometry_dash_img = pygame.image.load("geometry_dash.png")
super_mario_img = pygame.image.load("super_mario.png")

tła = {
    "default": pygame.image.load("background.png"),
    "bg1": pygame.image.load("background1.png"),
    "bg2": pygame.image.load("background2.png"),
    "bg3": pygame.image.load("background3.png"),
    "bg4": pygame.image.load("background4.png")
}

piłki = {
    "default": piłka_img,
    "basketball": basketball_img,
    "football": football_img,
    "geometry_dash": geometry_dash_img,
    "super_mario": super_mario_img
}

pad_img = pygame.image.load("pad.png")
serce = pygame.image.load("heart.png")

# Tworzenie prostokątów
piłka_rect = piłka_img.get_rect()
pad_rect = pad_img.get_rect()
pad_rect.topleft = (szerokość_ekranu // 2, wysokość_ekranu - 50)

# Wczytanie stanu gry
wczytaj_stan_gry()

# Główna pętla gry
gra = True
while gra:
    # Obsługa menu
    akcja = pokaz_menu()
    if akcja == "nowa_gra":
        reset()
        poziom = 1
        życia = 13
        punkty = 500
        zakupione_pilki = {
            "default": True,
            "basketball": False,
            "football": False,
            "geometry_dash": False,
            "super_mario": False
        }
        zakupione_tła = {
            "default": True,
            "bg1": False,
            "bg2": False,
            "bg3": False,
            "bg4": False
        }
        aktualna_pilka = "default"
        aktualne_tło = "default"
        generuj_cegielki()
    elif akcja == "kontynuuj_gre":
        pass
    elif akcja == "sklepik":
        sklepik()
        continue

    # Pętla gry
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                zapisz_stan_gry()
                pygame.quit()
                sys.exit()

        klawisze = pygame.key.get_pressed()
        if klawisze[pygame.K_LEFT]:
            pad_rect.x -= ruch_pada
        if klawisze[pygame.K_RIGHT]:
            pad_rect.x += ruch_pada

        # Aktualizacja pozycji piłki
        piłka_rect.x += ruch_x
        piłka_rect.y += ruch_y

        # Kolizje z krawędziami ekranu
        if piłka_rect.left <= 0 or piłka_rect.right >= szerokość_ekranu:
            ruch_x = -ruch_x
        if piłka_rect.top <= 0:
            ruch_y = -ruch_y
        if piłka_rect.bottom >= wysokość_ekranu:
            życia -= 1
            if życia <= 0:
                rysuj_tekst("Game Over", (szerokość_ekranu // 2 - 100, wysokość_ekranu // 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                gra = False
                break
            else:
                reset()

        # Kolizje z padem
        if piłka_rect.colliderect(pad_rect):
            ruch_y = -ruch_y

        # Kolizje z cegiełkami
        for cegielka in cegielki[:]:
            if piłka_rect.colliderect(cegielka):
                cegielki.remove(cegielka)
                ruch_y = -ruch_y
                punkty += 10
                if odtwarzaj_point_wav:
                    odtworz_dzwiek("point.mp3")
                if not cegielki:
                    if przejscie_na_kolejny_poziom():
                        rysuj_tekst("Gratulacje! Wygrałeś!", (szerokość_ekranu // 2 - 100, wysokość_ekranu // 2))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        gra = False
                        break

        # Rysowanie
        ekran.blit(tła[aktualne_tło], (0, 0))
        ekran.blit(piłki[aktualna_pilka], piłka_rect)
        ekran.blit(pad_img, pad_rect)
        for cegielka in cegielki:
            pygame.draw.rect(ekran, (255, 0, 0), cegielka)
        rysuj_tekst(f"Poziom: {poziom}", (10, 10))
        rysuj_tekst(f"Punkty: {punkty}", (10, 50))
        rysuj_życia()
        pygame.display.flip()
        zegar.tick(65)
        czas_w_grze += 16.67

# Zakończenie gry
zapisz_stan_gry()
pygame.quit()
