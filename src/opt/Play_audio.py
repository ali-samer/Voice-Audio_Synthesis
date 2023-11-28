import pygame


def play_audio(filename):
    """
    Play an audio file synchronously using Pygame.

    Parameters:
    - filename (str): Path to the audio file to be played.

    Example:
    play_audio('one.wav')
    """
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()


# Example usage:
"""
play_audio('one.wav')
"""
