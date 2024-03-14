import pygame
import random
import math
import threading

class Application:
    def __init__(self, number_of_nodes=20, title="NET 19"):

        def internal(self, number_of_nodes=20,title="NET 19"):
            self.number_of_nodes = number_of_nodes
            # Initialize Pygame
            pygame.init()

            # Set up the window
            self.window = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

            pygame.display.set_caption("Floating Nodes")
            programIcon = pygame.image.load('./resources/images/icon.png')

            pygame.display.set_icon(programIcon)

            # Colors
            self.BLACK = (0, 0, 0)
            self.GREY = (45, 49, 58)
            self.WHITE = (255, 255, 255)
            self.NODE_COLOR = (255, 0, 0)
            self.nodes = []

            self.font = pygame.font.SysFont(None, 80)
            self.heading = self.font.render(title, True, self.WHITE)

            # Main loop
            self.running = True
            self.run()

        threading.Thread(target=internal, args=(self, number_of_nodes, title)).start()

    def run(self):
        while self.running:
            if self.number_of_nodes <0:
                self.number_of_nodes = 0
            self.WIDTH, self.HEIGHT = pygame.display.get_surface().get_size()
            self.window.fill(self.GREY)
            padding = 40  # Adjust the padding value as needed
            self.window.blit(self.heading, self.heading.get_rect(midtop=(self.window.get_rect().centerx, padding)))


            if len(self.nodes) < self.number_of_nodes:
                # Create nodes
                for _ in range(self.number_of_nodes-len(self.nodes)):
                    x = random.randint(0, self.WIDTH)
                    y = random.randint(0, self.HEIGHT)
                    radius = random.randint(2, 5)
                    self.nodes.append(self.Node(self, x, y, radius))
            elif len(self.nodes) > self.number_of_nodes:
                # Remove nodes
                self.nodes = self.nodes[:self.number_of_nodes]

            # Move and draw nodes
            for node in self.nodes:
                node.move()
                node.draw(self.window)

            for i in range(len(self.nodes)):
                for j in range(i + 1, len(self.nodes)):
                    node1 = self.nodes[i]
                    node2 = self.nodes[j]
                    distance = math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
                    if distance < 100:  # Adjust this threshold as needed
                        pygame.draw.line(self.window, self.NODE_COLOR, (int(node1.x), int(node1.y)),
                                         (int(node2.x), int(node2.y)), 1)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

            # Adjust frame rate
            pygame.time.delay(2)

    class Node:
        def __init__(self, parent, x, y, radius):
            self.parent = parent
            self.x = x
            self.y = y
            self.radius = radius
            self.speed_x = random.uniform(-0.2, 0.2)
            self.speed_y = random.uniform(-0.2, 0.2)

        def move(self):
            self.x += self.speed_x
            self.y += self.speed_y

            if self.x < 0 or self.x > self.parent.WIDTH:
                self.speed_x *= -1
            if self.y < 0 or self.y > self.parent.HEIGHT:
                self.speed_y *= -1

        def draw(self, surface):
            pygame.draw.circle(
                surface, self.parent.NODE_COLOR, (int(self.x), int(self.y)), self.radius
            )


# # Create an instance of the Application class and run the program
# app = Application()

# while True:
#     add = input("[A] Add nodes. [R] Remove nodes.\n")
#     if add.lower() == "a":
#         app.number_of_nodes+=1
#     else:
#         app.number_of_nodes -=1
