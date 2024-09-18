import pygame

class PhysicsEntity: #physics class
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos) #helps to create different list for its position for easy entity, a list because it can change
        self.size = size
        self.velocity = [0, 0] #used to represent the rate of change and position / speed

    def update(self, movement=(0,0)):
        frame_movement = movement[0] + self.velocity[0],movement [1] + self.velocity[1]
        #how much of movement we want to make for the frame, creating a vector representing how much the entitiy
        # should be moved in the frame based on hwo much we want to force it to move in this frame
        # + how much there already is in velocity; multipel controls based on how things move

        self.pos[0] += frame_movement[0] #updating x position based on frame position
        self.pos[1] += frame_movement[1] #updating y position based on frame position

    def render (self, surf):
        surf.blit(self.game.assets['player'], self.pos)
