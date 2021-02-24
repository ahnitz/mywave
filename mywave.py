""" Reverse chirping waveform model using IMRPhenomD as a a base
"""
from scipy import signal
from scipy.interpolate import interp1d
import numpy

def fd(taper_start=None, taper_end=None, **kwds):
    from pycbc.waveform import get_fd_waveform
    from pycbc.waveform.utils import fd_taper

    flow = kwds['f_lower']
    fhigh = kwds['f_final']

    if 'approximant' in kwds:
        kwds.pop("approximant")
    hp, hc = get_fd_waveform(approximant="TaylorF2", **kwds)

    if taper_start:
        hp = fd_taper(hp, flow, flow + taper_start, side='left')
        hc = fd_taper(hc, flow, flow + taper_start, side='left')

    if taper_end:
        hp = fd_taper(hp, fhigh - taper_end, fhigh, side='right')
        hc = fd_taper(hc, fhigh - taper_end, fhigh, side='right')

    return hp, hc
        
window = signal.get_window(('kaiser', 8.0), 1e5)
window_left = window[:len(window)//2]
window_right = window[len(window)//2:]

xl = numpy.arange(0, len(window_left)) / float(len(window_left))
winl = interp1d(xl, window_left)

xr = numpy.arange(0, len(window_right)) / float(len(window_right))
winr = interp1d(xr, window_right)

def fd_sequence(taper_start=None, taper_end=None, **kwds):
    from pycbc.waveform import get_fd_waveform_sequence

    if 'approximant' in kwds:
        kwds.pop("approximant")
    hp, hc = get_fd_waveform_sequence(approximant="TaylorF2", **kwds)

    sam = kwds['sample_points']
    flow = sam[0]
    fhigh = sam[-1]
    
    if taper_start:
        l, r = numpy.searchsorted(sam, [flow, flow + taper_start])
        fval = sam[l:r]
        x = (fval - flow) / taper_start
        w = winl(x)
        hp[l:r] *= w
        hc[l:r] *= w

    if taper_end:
        l, r = numpy.searchsorted(sam, [fhigh - taper_end, fhigh])
        fval = sam[l:r]
        x = (fval - fhigh + taper_end) / taper_end
        w = winr(x)
        hp[l:r] *= w
        hc[l:r] *= w

    return hp, hc
