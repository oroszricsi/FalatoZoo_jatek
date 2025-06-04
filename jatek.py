import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Állatos Kvíz")

FONT = pygame.font.SysFont("segoeui", 26)
SMALL_FONT = pygame.font.SysFont("segoeui", 20)
BIG_FONT = pygame.font.SysFont("segoeui", 36, bold=True)

WHITE = (250, 250, 250)
BLACK = (30, 30, 30)
PRIMARY = (72, 133, 237)       
HOVER = (100, 160, 255)
CORRECT = (67, 160, 71)        
WRONG = (219, 68, 55)          
NEUTRAL = (230, 230, 230)

clock = pygame.time.Clock()


questions = [
    {"question": "Melyik kutyafajta híres arról, hogy eredetileg vakvezetőként képezték ki először?",
     "options": ["Golden Retriever", "Német juhászkutya", "Labrador Retriever", "Border Collie"], "answer": 1},
    {"question": "Melyik kisemlős hajlamos a „fogtúlnövésre”, ha nem rág eleget?",
     "options": ["Csincsilla", "Degu", "Nyúl", "Hörcsög"], "answer": 2},
    {"question": "A kutyák hány hangjelet ismerhetnek fel, ha jól képzettek?",
     "options": ["20–40", "50–100", "100–200", "200 felett"], "answer": 3},
    {"question": "Miért veszélyes a hagyma fogyasztása a kutyák számára?",
     "options": ["Puffadást okoz", "Májleállást okoz", "Vérszegénységet okoz", "Lázat okoz"], "answer": 2},
    {"question": "Mi a „zoomies” másik neve a kutyás viselkedéstanban?",
     "options": ["FRAP", "Játékos agresszió", "Szorongásos pörgés", "Stresszroham"], "answer": 0},
    {"question": "Melyik élelmiszer veszélyes macskákra a teobromin miatt?",
     "options": ["Csokoládé", "Szőlő", "Kávé", "Hagyma"], "answer": 0},
    {"question": "Melyik háziállat képes a bőrén keresztül lélegezni is?",
     "options": ["Díszhal", "Kaméleon", "Béka", "Papagáj"], "answer": 2},
    {"question": "Melyik kutyafajta oroszlánvadászatra lett tenyésztve?",
     "options": ["Rottweiler", "Basenji", "Rhodesian Ridgeback", "Dalmata"], "answer": 2},
    {"question": "Melyik nem javasolt játék kölyökkutyának?",
     "options": ["Gumicsont", "Kötéljáték", "Kemény műanyag labda", "Plüss"], "answer": 2},
    {"question": "Melyik kutyafajta nem ugat, hanem „énekel”?",
     "options": ["Husky", "Basenji", "Csau-csau", "Shiba Inu"], "answer": 1},
    {"question": "A macskák hányféle hangot képesek kiadni?",
     "options": ["10–20", "30–40", "50–60", "Több mint 100"], "answer": 3},
    {"question": "Melyik vitamin túlzott bevitele mérgező kutyáknak?",
     "options": ["C-vitamin", "D-vitamin", "B-vitamin", "K-vitamin"], "answer": 1},
    {"question": "Mi jellemző a Border Collie-ra?",
     "options": ["Lassú tanulás", "Nagyon intelligens", "Átlagos, makacs", "Nehezen motiválható"], "answer": 1},
    {"question": "A papagájok miért rágcsálnak dolgokat?",
     "options": ["Fogzás", "Játék", "Csőr karbantartása", "Éhség"], "answer": 2},
    {"question": "Melyik kisállat társas lény, nem javasolt egyedül tartani?",
     "options": ["Hörcsög", "Papagáj", "Tengerimalac", "Kaméleon"], "answer": 2},
    {"question": "A kutyák mennyi ideig őriznek meg egy szagot?",
     "options": ["Pár perc", "Órákig", "Napokig", "Akár évekig"], "answer": 3},
    {"question": "Mi a neve a macskák „hátpúposító” reflexének?",
     "options": ["Harci reflex", "Vadászreflex", "Félelmi reflex", "Ijedtségi válasz"], "answer": 2},
    {"question": "Melyik nem mérgező kutyák számára?",
     "options": ["Szőlő", "Avokádó", "Áfonya", "Csokoládé"], "answer": 2},
    {"question": "Melyik állat használ bajuszt tapintásra?",
     "options": ["Papagáj", "Nyúl", "Tengerimalac", "Mindhárom"], "answer": 3},
    {"question": "A kutyák miért ásnak a fekhelyükön?",
     "options": ["Játék", "Fészekkészítés", "Elbújni", "Hűteni magukat"], "answer": 1},
]

