import random
import tkinter as tk

WIDTH = 400
HEIGHT = 600
PLAYER_SPEED = 20
OBSTACLE_SPEED = 5
TICK_MS = 25

root = None
canvas = None
player = None
score_text = None
obstacles = []
score = 0
game_over = False


def move_left(event):
    if game_over:
        return
    x1, _, _, _ = canvas.coords(player)
    dx = max(-PLAYER_SPEED, -x1)
    canvas.move(player, dx, 0)


def move_right(event):
    if game_over:
        return
    _, _, x2, _ = canvas.coords(player)
    dx = min(PLAYER_SPEED, WIDTH - x2)
    canvas.move(player, dx, 0)


def spawn_obstacle():
    size = random.randint(20, 40)
    x1 = random.randint(0, WIDTH - size)
    obs = canvas.create_rectangle(x1, 0, x1 + size, size, fill="red")
    obstacles.append(obs)


def rects_overlap(a, b):
    # a and b are [x1, y1, x2, y2]
    return not (a[2] <= b[0] or a[0] >= b[2] or a[3] <= b[1] or a[1] >= b[3])


def end_game():
    global game_over
    game_over = True
    canvas.create_text(
        WIDTH // 2, HEIGHT // 2,
        fill="white", font=("Arial", 24, "bold"),
        text=f"Game Over\nScore: {score}"
    )


def game_loop():
    global score

    if game_over:
        return

    if random.random() < 0.05:
        spawn_obstacle()

    player_coords = canvas.coords(player)

    for obs in list(obstacles):
        canvas.move(obs, 0, OBSTACLE_SPEED)
        obs_coords = canvas.coords(obs)

        if rects_overlap(player_coords, obs_coords):
            end_game()
            return

        if obs_coords[1] > HEIGHT:
            canvas.delete(obs)
            obstacles.remove(obs)
            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")

    root.after(TICK_MS, game_loop)


def main():
    global root, canvas, player, score_text, obstacles, score, game_over

    root = tk.Tk()
    root.title("Simple Dodger")

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
    canvas.pack()

    player = canvas.create_rectangle(
        WIDTH // 2 - 20, HEIGHT - 40,
        WIDTH // 2 + 20, HEIGHT - 20,
        fill="cyan"
    )

    obstacles = []
    score = 0
    game_over = False

    score_text = canvas.create_text(
        10, 10, anchor="nw", fill="white", font=("Arial", 14), text="Score: 0"
    )

    root.bind("<Left>", move_left)
    root.bind("<Right>", move_right)

    game_loop()
    root.mainloop()

import random
import tkinter as tk

WIDTH = 400
HEIGHT = 600
PLAYER_SPEED = 20
OBSTACLE_SPEED = 5
TICK_MS = 25

# Game state (initialized in main)
root = None
canvas = None
player = None
score_text = None
obstacles = []
score = 0
game_over = False


def move_left(event):
    if game_over:
        return
    x1, _, _, _ = canvas.coords(player)
    dx = max(-PLAYER_SPEED, -x1)
    canvas.move(player, dx, 0)


def move_right(event):
    if game_over:
        return
    _, _, x2, _ = canvas.coords(player)
    dx = min(PLAYER_SPEED, WIDTH - x2)
    canvas.move(player, dx, 0)


def spawn_obstacle():
    size = random.randint(20, 40)
    x1 = random.randint(0, WIDTH - size)
    obs = canvas.create_rectangle(x1, 0, x1 + size, size, fill="red")
    obstacles.append(obs)


def rects_overlap(a, b):
    # a and b are [x1, y1, x2, y2]
    return not (a[2] <= b[0] or a[0] >= b[2] or a[3] <= b[1] or a[1] >= b[3])


def end_game():
    global game_over
    game_over = True
    canvas.create_text(
        WIDTH // 2, HEIGHT // 2,
        fill="white", font=("Arial", 24, "bold"),
        text=f"Game Over\nScore: {score}"
    )


def game_loop():
    global score

    if game_over:
        return

    if random.random() < 0.05:
        spawn_obstacle()

    player_coords = canvas.coords(player)

    for obs in list(obstacles):
        canvas.move(obs, 0, OBSTACLE_SPEED)
        obs_coords = canvas.coords(obs)

        if rects_overlap(player_coords, obs_coords):
            end_game()
            return

        if obs_coords[1] > HEIGHT:
            canvas.delete(obs)
            obstacles.remove(obs)
            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")

    root.after(TICK_MS, game_loop)


def main():
    global root, canvas, player, score_text, obstacles, score, game_over

    root = tk.Tk()
    root.title("Simple Dodger")

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
    canvas.pack()

    player = canvas.create_rectangle(
        WIDTH // 2 - 20, HEIGHT - 40,
        WIDTH // 2 + 20, HEIGHT - 20,
        fill="cyan"
    )

    obstacles = []
    score = 0
    game_over = False

    score_text = canvas.create_text(
        10, 10, anchor="nw", fill="white", font=("Arial", 14), text="Score: 0"
    )

    root.bind("<Left>", move_left)
    root.bind("<Right>", move_right)

    game_loop()
    root.mainloop()


if __name__ == "__main__":
    main()