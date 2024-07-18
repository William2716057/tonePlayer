import numpy as np
import sounddevice as sd

message = input("Enter message: ")

letter_to_frequency = {
    'a': 261.63,  # C4
    'b': 277.18,  # C#4/Db4
    'c': 293.66,  # D4
    'd': 311.13,  # D#4/Eb4
    'e': 329.63,  # E4
    'f': 349.23,  # F4
    'g': 369.99,  # F#4/Gb4
    'h': 392.00,  # G4
    'i': 415.30,  # G#4/Ab4
    'j': 440.00,  # A4
    'k': 466.16,  # A#4/Bb4
    'l': 493.88,  # B4
    'm': 523.25,  # C5
    'n': 554.37,  # C#5/Db5
    'o': 587.33,  # D5
    'p': 622.25,  # D#5/Eb5
    'q': 659.25,  # E5
    'r': 698.46,  # F5
    's': 739.99,  # F#5/Gb5
    't': 783.99,  # G5
    'u': 830.61,  # G#5/Ab5
    'v': 880.00,  # A5
    'w': 932.33,  # A#5/Bb5
    'x': 987.77,  # B5
    'y': 1046.50, # C6
    'z': 1108.73  # C#6/Db6
}

def generate_tone(frequency, duration, sample_rate=44100, amplitude=0.5):

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave

def play_tone(frequency, duration):

    sample_rate = 44100  # Sample rate in Hz
    tone = generate_tone(frequency, duration, sample_rate)
    sd.play(tone, samplerate=sample_rate)
    sd.wait()  # Wait until sound has finished playing

if __name__ == "__main__":
    frequency = 440.0  # Frequency in Hz (A4 note)
    duration = 0.5     # Duration in seconds
    play_tone(frequency, duration)
