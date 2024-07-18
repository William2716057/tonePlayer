import numpy as np
import sounddevice as sd

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
