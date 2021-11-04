from enum import Enum
import random

class Segment(Enum):
    SEGMENT_SPACE       = '   '
    SEGMENT_TOP         = ' _ '
    SEGMENT_MIDRIGHT    = ' _|'
    SEGMENT_MIDLEFT     = '|_ '
    SEGMENT_MIDBOTH     = '|_|'
    SEGMENT_LINELEFT    = '|  '
    SEGMENT_LINERIGHT   = '  |'
    SEGMENT_LINEBOTH    = '| |'

class Pattern:

    PATTERN = {'1':[Segment.SEGMENT_SPACE,Segment.SEGMENT_LINELEFT,Segment.SEGMENT_LINELEFT],
               '2':[Segment.SEGMENT_TOP,Segment.SEGMENT_MIDRIGHT,Segment.SEGMENT_MIDLEFT],
               '3':[Segment.SEGMENT_TOP, Segment.SEGMENT_MIDRIGHT, Segment.SEGMENT_MIDRIGHT],
               '4':[Segment.SEGMENT_SPACE, Segment.SEGMENT_MIDBOTH, Segment.SEGMENT_LINERIGHT],
               '5':[Segment.SEGMENT_TOP, Segment.SEGMENT_MIDLEFT, Segment.SEGMENT_MIDRIGHT],
               '6':[Segment.SEGMENT_TOP, Segment.SEGMENT_MIDLEFT, Segment.SEGMENT_MIDBOTH],
               '7':[Segment.SEGMENT_TOP, Segment.SEGMENT_LINERIGHT, Segment.SEGMENT_LINERIGHT],
               '8':[Segment.SEGMENT_TOP, Segment.SEGMENT_MIDBOTH, Segment.SEGMENT_MIDBOTH],
               '9':[Segment.SEGMENT_TOP, Segment.SEGMENT_MIDBOTH, Segment.SEGMENT_MIDRIGHT],
               '0':[Segment.SEGMENT_TOP, Segment.SEGMENT_LINEBOTH, Segment.SEGMENT_MIDBOTH]}

class DisplayLCD(Pattern):

    def __init__(self, number=1):
        self.number = number

    @property
    def digits_to_convert(self):
        return {f'{len(str(self.number))}':list(str(self.number))}

    def __repr__(self) -> str:
        return f'The number is {self.number} and it has a length of {len(str(self.number))} digits'

    @property
    def display_lcd_number(self):

        numbers = list(*self.digits_to_convert.values())

        # Concatenate the patterns lists of digits
        lcd_result=[]
        for i in range(0,len(numbers)):
            lcd_result += Pattern.PATTERN[numbers[i]]
       
        line=''
        for k in range(0,3):
            for i in range(k,len(lcd_result),3):
                line += lcd_result[i].value
            print(line)
            line=''

if __name__ == '__main__':

    lcd =DisplayLCD(655)
    print(lcd)
    lcd.display_lcd_number
