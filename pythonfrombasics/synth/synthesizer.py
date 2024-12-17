import numpy as np

class Synthesizer:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.oscillators = []
        self.volume = 0.5

    def add_oscillator(self, waveform='sine', frequency=440.0):
        """Add a new oscillator with a specific waveform and frequency."""
        self.oscillators.append({
            'waveform': waveform,
            'frequency': frequency,
            'phase': 0
        })

    def generate_waveform(self, oscillator, duration):
        """Generate a waveform based on the oscillator's settings."""
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        freq = oscillator['frequency']
        if oscillator['waveform'] == 'sine':
            return np.sin(2 * np.pi * freq * t)
        elif oscillator['waveform'] == 'square':
            return np.sign(np.sin(2 * np.pi * freq * t))
        elif oscillator['waveform'] == 'triangle':
            return 2 * np.abs(2 * ((freq * t) % 1) - 1) - 1
        elif oscillator['waveform'] == 'sawtooth':
            return 2 * ((freq * t) % 1) - 1

    def mix_audio(self, duration):
        """Mix all active oscillators into a single audio stream."""
        mix = np.zeros(int(self.sample_rate * duration))
        for osc in self.oscillators:
            mix += self.generate_waveform(osc, duration)
        return (self.volume * mix / max(len(self.oscillators), 1)).astype(np.float32)

    def set_volume(self, volume):
        """Set global volume."""
        self.volume = max(0.0, min(volume, 1.0))
