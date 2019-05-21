
class Tone:

    def __init__(self, toneId, length):
        self.toneId = toneId.lower()
        self.length = length

    def getId(self):
        return self.toneId

    def getLength(self):
        return self.length

class Bar:

    def __init__(self, instruments: dict):
        self.instruments = instruments

    class BarBuilder:

        def __init__(self):
            self.metrum = ()
            self.instruments = {}

        def withMetrum(self, metrum: tuple):
            self.metrum = metrum
            return self

        def withInstrument(self, instrument: str):
            self.instruments[instrument] = []
            return self

        def withTone(self, instrument: str, tone: str, note: str):
            
            self.instruments[instrument].append((tone.lower()+"*", 1 if len(note) == 1 else int(note[1:])))
            return self

        def calculateNoteSumForTones(self, instrument):
            noteSum = 0
            for tone in self.instruments[instrument]:
                note = tone[1]
                noteSum += 1/note 
            return noteSum

        def validateInstrumentTones(self):
            correctNoteSum = self.metrum[0] * (1/self.metrum[1])
            for instrument in self.instruments:
                currentNoteSum = self.calculateNoteSumForTones(instrument)        
                if correctNoteSum != currentNoteSum:
                    raise Exception("Invalid notes sum for given metrum.")

        def build(self):
            self.validateInstrumentTones()
            return Bar(self.instruments)


class Sequence:

    def __init__(self, metrum, bars):
        self.metrum = metrum
        self.bars = bars

    def setMetrum(self, metrum: tuple):
        self.metrum = metrum

    def setBars(self, bars: list):
        self.bars = bars

    def __str__(self):
        return str(self.metrum[0]) + "/" + str(self.metrum[1])
