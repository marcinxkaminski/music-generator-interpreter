
grammar MusicGenerator;


/* rules */ 

statements: (sequence_stmt | track)+ ;

sequence_stmt: 'sequence' ID '{' metrum ',' bars '}' ;

tempo: 'BPM' ':' NON_ZERO_NUMBER ;

metrum: NON_ZERO_NUMBER '/' NON_ZERO_NUMBER ;

bars: (bar)+ ;

bar: 'bar' '{' (instruments)+ '}' ;

instruments: INSTRUMENT ':' (tone)+ ';' ;

tone: ((TONE_NAME NOTE_LENGTH) | NOTE_LENGTH) ;

track: 'track' ID '{' tempo ',' sequences '}' ; 

sequences: (sequence_call)+ ; 

sequence_call: ID ('{' NON_ZERO_NUMBER '}')? ;


/* tokens/terminal */


INSTRUMENT: ('Piano' | 'Synth') ;

TONE_NAME: ('E' | 'F' | 'F#' | 'G' | 'G#' | 'A' | 'A#' | 'B' | 'C' | 'C#' | 'D' | 'D#') [1-8] ;

NOTE_LENGTH: '*' (' ' | '2' | '4' | '8' | '16');

NON_ZERO_NUMBER: [1-9] [0-9]*;

ID: [A-Za-z]+ [0-9]* ;

WS: [ \t\r\n]+ -> skip ;