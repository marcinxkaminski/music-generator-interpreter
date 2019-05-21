
from components.MusicGeneratorListener import MusicGeneratorListener
from components.MusicGeneratorParser import MusicGeneratorParser
from components.sequence import *
from components.generator import Generator

class Listener(MusicGeneratorListener):     

    def __init__(self):
        self.sequences = {}

    def enterSequence_stmt(self, ctx:MusicGeneratorParser.Sequence_stmtContext):
        pass

    def parseInstrument(self, instrument, builder):
        builder.withInstrument(instrument.INSTRUMENT().getText())
        for tone in instrument.tone():
            builder.withTone(instrument.INSTRUMENT().getText(), tone.TONE_NAME().getText(), tone.NOTE_LENGTH().getText())

    def parseBar(self, bar, metrum: tuple):
        builder = Bar.BarBuilder().withMetrum(metrum)
        for instrument in bar.instruments():
            self.parseInstrument(instrument, builder)
        return builder.build()

    def parseBars(self, bars: list, metrum: tuple):
        parsedBars = []
        for bar in bars.bar():
            parsedBars.append(self.parseBar(bar, metrum))
        return parsedBars

    def exitSequence_stmt(self, ctx:MusicGeneratorParser.Sequence_stmtContext):
        metrum = (int(ctx.metrum().NON_ZERO_NUMBER(0).getText()), int(ctx.metrum().NON_ZERO_NUMBER(1).getText()))
        bars = self.parseBars(ctx.bars(), metrum)
        self.sequences[ctx.ID().getText()] = Sequence(metrum, bars)

    def enterTrack(self, ctx:MusicGeneratorParser.TrackContext):
        generator = Generator(ctx.ID().getText(), int(ctx.tempo().NON_ZERO_NUMBER().getText()))

        for sequence in ctx.sequences().sequence_call():
            sequenceId = sequence.ID().getText()
            if sequenceId in self.sequences:
                repeatAmount = 1
                if sequence.NON_ZERO_NUMBER() is not None:
                    repeatAmount = int(sequence.NON_ZERO_NUMBER().getText())
                generator.addSequence(self.sequences[sequenceId], repeatAmount=repeatAmount)
            else:
                raise Exception("Undefined sequence: " + sequenceId + ".") 
        generator.generate()
