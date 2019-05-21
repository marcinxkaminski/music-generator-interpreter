import os
import wave
import numpy as np

from music.log import get_logger
from pysndfx import AudioEffectsChain

logger = get_logger(__name__)

def _bin_to_int(bin):
    as_int = 0
    for char in bin[::-1]:
        as_int <<= 8
        as_int += ord(char)
    return as_int

def decorate(track, track_out=None, delete_after=True):
    if not track:
        logger.error(
            'Track that should be decorated mus be properly specified.')
        raise FileNotFoundError(
            'Track that should be decorated mus be properly specified.')

    fx = (
        AudioEffectsChain()
        .equalizer(frequency=7300, q=1.0, db=-1)
        .highpass(frequency=310)
        .lowpass(frequency=16000)
        .delay(gain_in=1,
                gain_out=1,
                delays=list((500, 500)),
                decays=list((0.05, 0.05)))
        .reverb(reverberance=20,
               hf_damping=50,
               room_scale=80,
               stereo_depth=100,
               pre_delay=25,
               wet_gain=0,
               wet_only=False)
        .gain(-4)
        .normalize()
    )

    outfile = track_out or '{}_decorated.wav'.format(track)

    fx(track, outfile)
    logger.info('Decorated %s', track)

    if delete_after:
        os.remove(track)
        logger.info('Removed %s after decorating.', track)


def merge(tracks, track_out=None, delete_after=True):
    if not tracks:
        logger.error(
            'Tracks that should be merged must be properly specified.')
        raise FileNotFoundError(
            'Tracks that should be merged must be properly specified.')

    outfile = track_out or '{}_merge.wav'.format(tracks[0])

    wavs = [wave.open(track) for track in tracks]
    frames = [wav.readframes(wav.getnframes()) for wav in wavs]
    samples = [np.frombuffer(f, dtype='<i2') for f in frames]
    samples = [samp.astype(np.float64) for samp in samples]
    n = min(map(len, samples))
    mix = samples[0][:n] + samples[1][:n]

    with wave.open(outfile, 'w') as output:
        output.setparams(wavs[0].getparams())
        output.writeframes(mix.astype('<i2').tobytes())

    logger.info('Merged tracks into %s', outfile)

    if delete_after:
        for track in tracks:
            os.remove(track)
        logger.info('Removed merged tracks.')

    return outfile
