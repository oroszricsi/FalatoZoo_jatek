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
def draw_text(text, font, color, surface, x, y):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        rendered = font.render(line, True, color)
        surface.blit(rendered, (x, y + i * 32))

def draw_button(text, rect, state_color):
    pygame.draw.rect(screen, state_color, rect, border_radius=12)
    pygame.draw.rect(screen, BLACK, rect, width=2, border_radius=12)
    draw_text(text, SMALL_FONT, BLACK, screen, rect.x + 15, rect.y + 15)

def show_question(q, idx, selected=None):
    screen.fill(WHITE)
    draw_text(f"{idx+1}/5. kérdés", BIG_FONT, PRIMARY, screen, 60, 30)
    draw_text(q["question"], FONT, BLACK, screen, 60, 100)

    buttons = []
    mouse = pygame.mouse.get_pos()
    for i, option in enumerate(q["options"]):
        rect = pygame.Rect(100, 180 + i * 90, 800, 70)
        if selected is not None:
            if i == q["answer"]:
                color = CORRECT
            elif i == selected:
                color = WRONG
            else:
                color = NEUTRAL
        else:
            color = HOVER if rect.collidepoint(mouse) else NEUTRAL
        draw_button(f"{chr(65+i)}) {option}", rect, color)
        buttons.append(rect)
    pygame.display.flip()
    return buttons

def show_result(score):
    screen.fill(WHITE)
    draw_text("Kvíz vége!", BIG_FONT, PRIMARY, screen, 380, 250)
    draw_text(f"Eredmény: {score} / 5", FONT, BLACK, screen, 390, 320)
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()
    sys.exit()


random.shuffle(questions)
selected_questions = questions[:5]
score = 0

for idx, q in enumerate(selected_questions):
    selected = None
    answered = False
    while not answered:
        buttons = show_question(q, idx, selected)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, btn in enumerate(buttons):
                    if btn.collidepoint(event.pos):
                        selected = i
                        if i == q["answer"]:
                            score += 1
                        show_question(q, idx, selected)
                        pygame.display.flip()
                        pygame.time.wait(1500)
                        answered = True
        clock.tick(30)

show_result(score)
