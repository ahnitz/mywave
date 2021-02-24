""" Reverse chirping waveform model using IMRPhenomD as a a base
"""

# Notes on style:
#
# For example purposes only of how to advertise a waveform model to PyCBC
# Function should take kwargs only, and must accept abitrary kwargs.
# 'newparam' is an example of adding a new argument.
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

def fd_sequence(**kwds):
    from pycbc.waveform import get_fd_waveform_sequence

    if 'approximant' in kwds:
        kwds.pop("approximant")
    hp, hc = get_fd_waveform_sequence(approximant="TaylorF2", **kwds)

    return hp, hc
