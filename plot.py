from pathlib import PosixPath
from numpy import fromfile, int64
from scipy.io.wavfile import read as read_wav
from matplotlib.pyplot import subplots, tight_layout, show


def graph_heartpair(ecg_dir: PosixPath, pcg_dir: PosixPath) -> None:
    datos_dat = fromfile(ecg_dir, dtype=int64)
    frec_muestreo, datos_wav = read_wav(pcg_dir)

    fig, axs = subplots(2, 1, figsize=(10, 8))

    axs[0].plot(datos_dat)
    axs[0].set_title("Datos del archivo .dat")

    axs[1].plot(datos_wav)
    axs[1].set_title("Datos del archivo .wav")

    tight_layout()
    show()
