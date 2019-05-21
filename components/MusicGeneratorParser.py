# Generated from MusicGenerator.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("^\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\6\2\33")
        buf.write("\n\2\r\2\16\2\34\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\6\6\60\n\6\r\6\16\6\61")
        buf.write("\3\7\3\7\3\7\6\7\67\n\7\r\7\16\78\3\7\3\7\3\b\3\b\3\b")
        buf.write("\6\b@\n\b\r\b\16\bA\3\b\3\b\3\t\3\t\3\t\5\tI\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\6\13T\n\13\r\13\16\13")
        buf.write("U\3\f\3\f\3\f\3\f\5\f\\\n\f\3\f\2\2\r\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\2\2\2Z\2\32\3\2\2\2\4\36\3\2\2\2\6&\3\2\2\2")
        buf.write("\b*\3\2\2\2\n/\3\2\2\2\f\63\3\2\2\2\16<\3\2\2\2\20H\3")
        buf.write("\2\2\2\22J\3\2\2\2\24S\3\2\2\2\26W\3\2\2\2\30\33\5\4\3")
        buf.write("\2\31\33\5\22\n\2\32\30\3\2\2\2\32\31\3\2\2\2\33\34\3")
        buf.write("\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\3\3\2\2\2\36\37")
        buf.write("\7\3\2\2\37 \7\21\2\2 !\7\4\2\2!\"\5\b\5\2\"#\7\5\2\2")
        buf.write("#$\5\n\6\2$%\7\6\2\2%\5\3\2\2\2&\'\7\7\2\2\'(\7\b\2\2")
        buf.write("()\7\20\2\2)\7\3\2\2\2*+\7\20\2\2+,\7\t\2\2,-\7\20\2\2")
        buf.write("-\t\3\2\2\2.\60\5\f\7\2/.\3\2\2\2\60\61\3\2\2\2\61/\3")
        buf.write("\2\2\2\61\62\3\2\2\2\62\13\3\2\2\2\63\64\7\n\2\2\64\66")
        buf.write("\7\4\2\2\65\67\5\16\b\2\66\65\3\2\2\2\678\3\2\2\28\66")
        buf.write("\3\2\2\289\3\2\2\29:\3\2\2\2:;\7\6\2\2;\r\3\2\2\2<=\7")
        buf.write("\r\2\2=?\7\b\2\2>@\5\20\t\2?>\3\2\2\2@A\3\2\2\2A?\3\2")
        buf.write("\2\2AB\3\2\2\2BC\3\2\2\2CD\7\13\2\2D\17\3\2\2\2EF\7\16")
        buf.write("\2\2FI\7\17\2\2GI\7\17\2\2HE\3\2\2\2HG\3\2\2\2I\21\3\2")
        buf.write("\2\2JK\7\f\2\2KL\7\21\2\2LM\7\4\2\2MN\5\6\4\2NO\7\5\2")
        buf.write("\2OP\5\24\13\2PQ\7\6\2\2Q\23\3\2\2\2RT\5\26\f\2SR\3\2")
        buf.write("\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2V\25\3\2\2\2W[\7\21")
        buf.write("\2\2XY\7\4\2\2YZ\7\20\2\2Z\\\7\6\2\2[X\3\2\2\2[\\\3\2")
        buf.write("\2\2\\\27\3\2\2\2\n\32\34\618AHU[")
        return buf.getvalue()


class MusicGeneratorParser ( Parser ):

    grammarFileName = "MusicGenerator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sequence'", "'{'", "','", "'}'", "'BPM'", 
                     "':'", "'/'", "'bar'", "';'", "'track'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INSTRUMENT", 
                      "TONE_NAME", "NOTE_LENGTH", "NON_ZERO_NUMBER", "ID", 
                      "WS" ]

    RULE_statements = 0
    RULE_sequence_stmt = 1
    RULE_tempo = 2
    RULE_metrum = 3
    RULE_bars = 4
    RULE_bar = 5
    RULE_instruments = 6
    RULE_tone = 7
    RULE_track = 8
    RULE_sequences = 9
    RULE_sequence_call = 10

    ruleNames =  [ "statements", "sequence_stmt", "tempo", "metrum", "bars", 
                   "bar", "instruments", "tone", "track", "sequences", "sequence_call" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    INSTRUMENT=11
    TONE_NAME=12
    NOTE_LENGTH=13
    NON_ZERO_NUMBER=14
    ID=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequence_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicGeneratorParser.Sequence_stmtContext)
            else:
                return self.getTypedRuleContext(MusicGeneratorParser.Sequence_stmtContext,i)


        def track(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicGeneratorParser.TrackContext)
            else:
                return self.getTypedRuleContext(MusicGeneratorParser.TrackContext,i)


        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = MusicGeneratorParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MusicGeneratorParser.T__0]:
                    self.state = 22
                    self.sequence_stmt()
                    pass
                elif token in [MusicGeneratorParser.T__9]:
                    self.state = 23
                    self.track()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MusicGeneratorParser.T__0 or _la==MusicGeneratorParser.T__9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sequence_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MusicGeneratorParser.ID, 0)

        def metrum(self):
            return self.getTypedRuleContext(MusicGeneratorParser.MetrumContext,0)


        def bars(self):
            return self.getTypedRuleContext(MusicGeneratorParser.BarsContext,0)


        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_sequence_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence_stmt" ):
                listener.enterSequence_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence_stmt" ):
                listener.exitSequence_stmt(self)




    def sequence_stmt(self):

        localctx = MusicGeneratorParser.Sequence_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sequence_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(MusicGeneratorParser.T__0)
            self.state = 29
            self.match(MusicGeneratorParser.ID)
            self.state = 30
            self.match(MusicGeneratorParser.T__1)
            self.state = 31
            self.metrum()
            self.state = 32
            self.match(MusicGeneratorParser.T__2)
            self.state = 33
            self.bars()
            self.state = 34
            self.match(MusicGeneratorParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TempoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NON_ZERO_NUMBER(self):
            return self.getToken(MusicGeneratorParser.NON_ZERO_NUMBER, 0)

        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_tempo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTempo" ):
                listener.enterTempo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTempo" ):
                listener.exitTempo(self)




    def tempo(self):

        localctx = MusicGeneratorParser.TempoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tempo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(MusicGeneratorParser.T__4)
            self.state = 37
            self.match(MusicGeneratorParser.T__5)
            self.state = 38
            self.match(MusicGeneratorParser.NON_ZERO_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetrumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NON_ZERO_NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(MusicGeneratorParser.NON_ZERO_NUMBER)
            else:
                return self.getToken(MusicGeneratorParser.NON_ZERO_NUMBER, i)

        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_metrum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetrum" ):
                listener.enterMetrum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetrum" ):
                listener.exitMetrum(self)




    def metrum(self):

        localctx = MusicGeneratorParser.MetrumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_metrum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(MusicGeneratorParser.NON_ZERO_NUMBER)
            self.state = 41
            self.match(MusicGeneratorParser.T__6)
            self.state = 42
            self.match(MusicGeneratorParser.NON_ZERO_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BarsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicGeneratorParser.BarContext)
            else:
                return self.getTypedRuleContext(MusicGeneratorParser.BarContext,i)


        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_bars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBars" ):
                listener.enterBars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBars" ):
                listener.exitBars(self)




    def bars(self):

        localctx = MusicGeneratorParser.BarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.bar()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MusicGeneratorParser.T__7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruments(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicGeneratorParser.InstrumentsContext)
            else:
                return self.getTypedRuleContext(MusicGeneratorParser.InstrumentsContext,i)


        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_bar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBar" ):
                listener.enterBar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBar" ):
                listener.exitBar(self)




    def bar(self):

        localctx = MusicGeneratorParser.BarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(MusicGeneratorParser.T__7)
            self.state = 50
            self.match(MusicGeneratorParser.T__1)
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                self.instruments()
                self.state = 54 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MusicGeneratorParser.INSTRUMENT):
                    break

            self.state = 56
            self.match(MusicGeneratorParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstrumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTRUMENT(self):
            return self.getToken(MusicGeneratorParser.INSTRUMENT, 0)

        def tone(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicGeneratorParser.ToneContext)
            else:
                return self.getTypedRuleContext(MusicGeneratorParser.ToneContext,i)


        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_instruments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruments" ):
                listener.enterInstruments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruments" ):
                listener.exitInstruments(self)




    def instruments(self):

        localctx = MusicGeneratorParser.InstrumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_instruments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MusicGeneratorParser.INSTRUMENT)
            self.state = 59
            self.match(MusicGeneratorParser.T__5)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.tone()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MusicGeneratorParser.TONE_NAME or _la==MusicGeneratorParser.NOTE_LENGTH):
                    break

            self.state = 65
            self.match(MusicGeneratorParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ToneContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTE_LENGTH(self):
            return self.getToken(MusicGeneratorParser.NOTE_LENGTH, 0)

        def TONE_NAME(self):
            return self.getToken(MusicGeneratorParser.TONE_NAME, 0)

        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_tone

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTone" ):
                listener.enterTone(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTone" ):
                listener.exitTone(self)




    def tone(self):

        localctx = MusicGeneratorParser.ToneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tone)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MusicGeneratorParser.TONE_NAME]:
                self.state = 67
                self.match(MusicGeneratorParser.TONE_NAME)
                self.state = 68
                self.match(MusicGeneratorParser.NOTE_LENGTH)
                pass
            elif token in [MusicGeneratorParser.NOTE_LENGTH]:
                self.state = 69
                self.match(MusicGeneratorParser.NOTE_LENGTH)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TrackContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MusicGeneratorParser.ID, 0)

        def tempo(self):
            return self.getTypedRuleContext(MusicGeneratorParser.TempoContext,0)


        def sequences(self):
            return self.getTypedRuleContext(MusicGeneratorParser.SequencesContext,0)


        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_track

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrack" ):
                listener.enterTrack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrack" ):
                listener.exitTrack(self)




    def track(self):

        localctx = MusicGeneratorParser.TrackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_track)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MusicGeneratorParser.T__9)
            self.state = 73
            self.match(MusicGeneratorParser.ID)
            self.state = 74
            self.match(MusicGeneratorParser.T__1)
            self.state = 75
            self.tempo()
            self.state = 76
            self.match(MusicGeneratorParser.T__2)
            self.state = 77
            self.sequences()
            self.state = 78
            self.match(MusicGeneratorParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SequencesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sequence_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MusicGeneratorParser.Sequence_callContext)
            else:
                return self.getTypedRuleContext(MusicGeneratorParser.Sequence_callContext,i)


        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_sequences

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequences" ):
                listener.enterSequences(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequences" ):
                listener.exitSequences(self)




    def sequences(self):

        localctx = MusicGeneratorParser.SequencesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sequences)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.sequence_call()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MusicGeneratorParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sequence_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MusicGeneratorParser.ID, 0)

        def NON_ZERO_NUMBER(self):
            return self.getToken(MusicGeneratorParser.NON_ZERO_NUMBER, 0)

        def getRuleIndex(self):
            return MusicGeneratorParser.RULE_sequence_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence_call" ):
                listener.enterSequence_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence_call" ):
                listener.exitSequence_call(self)




    def sequence_call(self):

        localctx = MusicGeneratorParser.Sequence_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sequence_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(MusicGeneratorParser.ID)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MusicGeneratorParser.T__1:
                self.state = 86
                self.match(MusicGeneratorParser.T__1)
                self.state = 87
                self.match(MusicGeneratorParser.NON_ZERO_NUMBER)
                self.state = 88
                self.match(MusicGeneratorParser.T__3)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





