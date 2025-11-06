from ligotools.utils import whiten, write_wavfile, reqshift, make_psd_window
import numpy as np

def test_whiten():
    dt=np.float64(0.000244140625)
    strain=np.sin(2*np.pi*50*np.arange(0, 1, dt)) # make a test sine wave
    interp_psd=lambda f: np.ones_like(f) # takes f and returns 1 for every frequency

    whiten_test = whiten(strain, interp_psd, dt)

    assert len(whiten_test) == len(strain) # assert the output is the same length as the input
    assert np.all(np.isfinite(whiten_test)) # assert there are no NaN numbers

def test_make_psd_window():
    fs=4096
    #overlap_percentage=0.5
    NFFT, psd_window, NOVL = make_psd_window(fs)

    assert NFFT==4*fs # NFFT should be 4 times fs

    assert len(psd_window)==NFFT # assert length of the window is the same length as the NFFT

    assert NOVL==NFFT//2 # default overlap should be 50%