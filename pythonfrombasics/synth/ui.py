from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, 
    QComboBox, QSlider, QWidget, QLabel, QHBoxLayout
)
from PyQt5.QtCore import Qt
from synthesizer import Synthesizer
from audio import AudioEngine

class SynthUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.synth = Synthesizer()
        self.audio = AudioEngine(self.synth)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("3x Osc Synthesizer")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Oscillator Controls
        osc_controls = QHBoxLayout()
        
        self.waveform_selector = QComboBox()
        self.waveform_selector.addItems(["sine", "square", "triangle", "sawtooth"])
        osc_controls.addWidget(QLabel("Waveform:"))
        osc_controls.addWidget(self.waveform_selector)

        self.frequency_slider = QSlider(Qt.Horizontal)
        self.frequency_slider.setRange(20, 2000)
        self.frequency_slider.setValue(440)
        self.frequency_slider.valueChanged.connect(self.update_frequency_label)
        osc_controls.addWidget(QLabel("Frequency:"))
        osc_controls.addWidget(self.frequency_slider)
        
        self.frequency_label = QLabel("440 Hz")
        osc_controls.addWidget(self.frequency_label)

        layout.addLayout(osc_controls)

        # Add Oscillator Button
        add_osc_button = QPushButton("Add Oscillator")
        add_osc_button.clicked.connect(self.add_oscillator)
        layout.addWidget(add_osc_button)

        # Play/Stop Buttons
        play_button = QPushButton("Play")
        play_button.clicked.connect(self.audio.start)
        layout.addWidget(play_button)

        stop_button = QPushButton("Stop")
        stop_button.clicked.connect(self.audio.stop)
        layout.addWidget(stop_button)

        # Set Main Widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_frequency_label(self):
        frequency = self.frequency_slider.value()
        self.frequency_label.setText(f"{frequency} Hz")

    def add_oscillator(self):
        waveform = self.waveform_selector.currentText()
        frequency = self.frequency_slider.value()
        self.synth.add_oscillator(waveform, frequency)
