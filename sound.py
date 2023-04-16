import pygame


def maze_sound():
    pygame.mixer.init()  # initialize the mixer module


def sound_move():
    # Load the sound file
    move_sound = pygame.mixer.Sound(r'Sound\move.wav')
    # Play the sound
    move_sound.play()


def sound_bg():
    # Load the sound file
    move_sound = pygame.mixer.Sound(r'Sound\background.wav')
    # Play the sound
    move_sound.play(loops=-1)


def sound_death():
    # Load the sound file
    move_sound = pygame.mixer.Sound(r'Sound\death.wav')
    # Play the sound
    move_sound.play(loops=-1)


def sound_ate():
    # Load the sound file
    eat_sound = pygame.mixer.Sound(r'Sound\eat.wav')
    # Play the sound
    eat_sound.play()


def sound_win():
    # Load the sound file
    win_sound = pygame.mixer.Sound(r'Sound\win.wav')
    # Play the sound
    win_sound.play()


def sound_loose():
    # Load the sound file
    loose_sound = pygame.mixer.Sound(r'Sound\loose.wav')
    # Play the sound
    loose_sound.play()
