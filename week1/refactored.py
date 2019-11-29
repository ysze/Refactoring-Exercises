import itertools

import scipy.io.wavfile as wavfile
import numpy as np

DTMF_LOW_FREQUENCIES = [697, 770, 852, 941]
DTMF_HIGH_FREQUENCIES = [1209, 1336, 1477]
DTMF_FREQUENCIES_MAP = {
    digit: frequencies
    for digit, frequencies in zip(
        "1 2 3 4 5 6 7 8 9 * 0 #".split(),
        itertools.product(DTMF_LOW_FREQUENCIES, DTMF_HIGH_FREQUENCIES),
    )
}


def dialer(filename, frame_rate, sequence, duration):
    tones = [
        tone
        for digit in sequence
        for tone in average_waveforms(
            waveform(frequency, duration, frame_rate)
            for frequency in DTMF_FREQUENCIES_MAP[digit]
        )
    ]
    wavfile.write(filename, frame_rate, np.asarray(tones))


def waveform(frequency, duration, frame_rate):
    return np.sin(
        2 * np.pi * frequency * np.linspace(0, duration, duration * frame_rate)
    )


def average_waveforms(waveforms):
    return np.mean(waveforms, axis=0)
