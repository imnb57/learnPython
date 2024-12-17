import sounddevice as sd
import numpy as np
from synthesizer import Synthesizer

class AudioEngine:
    def __init__(self, synthesizer):
        self.synthesizer = synthesizer
        self.stream = None

    def audio_callback(self, outdata, frames, time, status):
        """Audio stream callback for real-time playback."""
        audio_data = self.synthesizer.mix_audio(frames / self.synthesizer.sample_rate)
        outdata[:] = np.expand_dims(audio_data, axis=1)

    def start(self):
        """Start the audio stream."""
        if self.stream is None:
            self.stream = sd.OutputStream(
                samplerate=self.synthesizer.sample_rate,
                channels=1,
                callback=self.audio_callback
            )
            self.stream.start()

    def stop(self):
        """Stop the audio stream."""
        if self.stream is not None:
            self.stream.stop()
            self.stream.close()
            self.stream = None
