
import os
from pysynth import make_wav
from components.sequence import *


class Generator:
    
    def __init__(self, trackName: str, tempo: int):
        self.trackName = trackName
        self.instruments = {}
        self.tempo = tempo


    def accumulateTones(self, bar: Bar):
        toneSum = {}
        for instrument in bar.instruments:
            if instrument not in toneSum:
                toneSum[instrument] = []
            toneSum[instrument] += bar.instruments[instrument]
        return toneSum


    def addTones(self, toneSum, repeatAmount):
        for instrument in toneSum:
            if instrument not in self.instruments:
                self.instruments[instrument] = []
            for i in range(repeatAmount):
                self.instruments[instrument] += toneSum[instrument]


    def accumulateBarTones(self, bar: Bar):
        toneSum = self.accumulateTones(bar)
        return toneSum

    def addSequence(self, sequence: Sequence, repeatAmount = 1):
        sequenceToneSum = {}
        for bar in sequence.bars:
            barToneSum = self.accumulateBarTones(bar)
            for instrument in barToneSum:
                if instrument not in sequenceToneSum:
                    sequenceToneSum[instrument] = []
                sequenceToneSum[instrument] += barToneSum[instrument]

        self.addTones(sequenceToneSum, repeatAmount)


    def generate(self):
        
        for instrument in self.instruments:
            trackDir = "./tmp/" + self.trackName 
            if not os.path.exists(trackDir):
                os.makedirs(trackDir)

            make_wav(tuple(self.instruments[instrument]), fn = trackDir + "/" + instrument + ".wav", bpm = self.tempo)