import sys
import os
from antlr4.FileStream import FileStream
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.tree.Tree import ParseTreeWalker  
from music.fs import read
from music.log import get_logger
from music.audio import decorate, merge
from components.Listener import Listener
from components.MusicGeneratorLexer import MusicGeneratorLexer
from components.MusicGeneratorParser import MusicGeneratorParser

logger = get_logger(__name__)


def compile(inputFile):
    input_stream = FileStream(inputFile)
    lexer = MusicGeneratorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MusicGeneratorParser(stream)
    tree = parser.statements()
    printer = Listener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


def getTrackFileNames(dirPath):

    filenames = []
    for _, _, files in os.walk(dirPath): 
        for filename in files:
            filenames += [dirPath + "/" + filename]

    return filenames

def mixFiles():
    baseDir = "./tmp"
    logger.info(baseDir)
    for _, dirs, _ in os.walk(baseDir):

        logger.info(dirs)
        for trackName in dirs:
            files = getTrackFileNames(baseDir + "/" + trackName)
            outputFilename = "./" + trackName + ".wav"
            logger.info("Mixing " + trackName + "...")
            decorate(merge(files, delete_after=True), track_out=outputFilename, delete_after=True)
            logger.info("Mixing finished.")


def cleanWorkspace():
    baseDir = "./tmp"
    for _, dirs, _ in os.walk(baseDir):
        for dirName in dirs:
            os.rmdir("{}/{}".format(baseDir, dirName))


def create(file_path):
    logger.info('Starting compilation ...')

    try:
        compile(file_path)
        logger.info("Pre-processing finished.")
        mixFiles()
        logger.info('Compilation finished.')
        cleanWorkspace()

    except Exception as ex:
        logger.error(repr(ex))
        logger.error('Compilation failed.')
    