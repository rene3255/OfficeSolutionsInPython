from enum import Enum, unique


class DefaultValue(Enum):
    
    """
    Mon 01 Nov 2021 it's 20:26 ~ RSC

    [x] This class uses Enum to establish consts
        that no change during executions and
        these are used in all script code.
    """
    CLD_VTL_DFLT_VAL = 3
    CLD_HZL_DFLT_VAL = 2

class Pattern:

    def __init__(self, convert_number_to_lcd=2, lcd_height=5, lcd_width  = 3) -> None:
        self.convert_number_to_lcd = convert_number_to_lcd
        self.lcd_height = lcd_height
        self.lcd_width = lcd_width

    
    def which_number_to_lcd(self, the_num, the_height, the_width):
        self.convert_number_to_lcd= the_num
        self.lcd_height = the_height
        self.lcd_width = the_width

    
    def digits_to_convert(self):
        return  {f'{len(str(self.convert_number_to_lcd))}':list(map(int,(str(self.convert_number_to_lcd))))}
    
    def build_digit_lcd(self):

        SEGMENT_SPACE       = ' '+' '*self.lcd_width+' '
        SEGMENT_TOP         = ' '+'_'*self.lcd_width+' '
        SEGMENT_MIDRIGHT    = ' '+'_'*self.lcd_width+'|'
        SEGMENT_MIDLEFT     = '|'+'_'*self.lcd_width+' '
        SEGMENT_MIDBOTH     = '|'+'_'*self.lcd_width+'|'
        SEGMENT_LINELEFT    = '|'+' '*self.lcd_width+' '
        SEGMENT_LINERIGHT   = ' '+' '*self.lcd_width+'|'
        SEGMENT_LINEBOTH    = '|'+' '*self.lcd_width+'|'
            
    
        PATTERN = {'1':[SEGMENT_SPACE,SEGMENT_LINELEFT,SEGMENT_LINELEFT],
                   '2':[SEGMENT_TOP,SEGMENT_MIDRIGHT,SEGMENT_MIDLEFT],
                   '3':[SEGMENT_TOP, SEGMENT_MIDRIGHT, SEGMENT_MIDRIGHT],
                   '4':[SEGMENT_SPACE, SEGMENT_MIDBOTH, SEGMENT_LINERIGHT],
                   '5':[SEGMENT_TOP, SEGMENT_MIDLEFT, SEGMENT_MIDRIGHT],
                   '6':[SEGMENT_TOP, SEGMENT_MIDLEFT, SEGMENT_MIDBOTH],
                   '7':[SEGMENT_TOP, SEGMENT_LINERIGHT, SEGMENT_LINERIGHT],
                   '8':[SEGMENT_TOP, SEGMENT_MIDBOTH, SEGMENT_MIDBOTH],
                   '9':[SEGMENT_TOP, SEGMENT_MIDBOTH, SEGMENT_MIDRIGHT],
                   '0':[SEGMENT_TOP, SEGMENT_LINEBOTH, SEGMENT_MIDBOTH]}


        ratio=self.get_ratio
        
                
        for i in range(0,len(PATTERN)):

            if str(i) == '1':
                if ratio:
                    x=0
                    for r in range(ratio):
                        PATTERN[str(i)].insert(1+x,SEGMENT_LINELEFT)
                        PATTERN[str(i)].insert(3+x,SEGMENT_LINELEFT)
                        x+=1

            if str(i) == '2':
                if ratio:
                    x=0
                    for r in range(ratio):
                        PATTERN[str(i)].insert(1+x,SEGMENT_LINERIGHT)
                        PATTERN[str(i)].insert(3+x,SEGMENT_LINELEFT)
                        x+=1

            if str(i) == '3':
                if ratio:
                    x=0
                    for r in range(ratio):
                        PATTERN[str(i)].insert(1+x, SEGMENT_LINERIGHT)
                        PATTERN[str(i)].insert(3+x, SEGMENT_LINERIGHT)
                        x+=1

            if str(i) == '4':
                if ratio:
                    x=0
                    for r in range(ratio):
                        PATTERN[str(i)].insert(1+x,SEGMENT_LINEBOTH)
                        PATTERN[str(i)].insert(3+x,SEGMENT_LINERIGHT)
                        x+=1
            if str(i) == '5':
                if ratio:
                    x=0
                    for r in range(ratio):
                        PATTERN[str(i)].insert(1+x,SEGMENT_LINELEFT)
                        PATTERN[str(i)].insert(3+x,SEGMENT_LINERIGHT)
                        x+=1

            if str(i) == '6':
                if ratio:
                    x=0
                    for r in range(ratio):
                        PATTERN[str(i)].insert(1+x, SEGMENT_LINELEFT)
                        PATTERN[str(i)].insert(3+x, SEGMENT_LINEBOTH)
                        x+=1
            if str(i) == '7':
                if ratio:
                    x=0
                    for r in range(ratio):
                        PATTERN[str(i)].insert(1+x, SEGMENT_LINERIGHT)
                        PATTERN[str(i)].insert(3+x, SEGMENT_LINERIGHT)
                        x+=1
            if str(i) == '8':
                if ratio:
                    x=0
                    for r in range(ratio):
                        PATTERN[str(i)].insert(1+x, SEGMENT_LINEBOTH)
                        PATTERN[str(i)].insert(3+x, SEGMENT_LINEBOTH)
                        x+=1

            if str(i) == '9':
                if ratio:
                    x=0
                    for r in range(ratio):
                        PATTERN[str(i)].insert(1+x, SEGMENT_LINEBOTH)
                        PATTERN[str(i)].insert(3+x, SEGMENT_LINERIGHT)
                        x+=1
            if str(i) == '0':
                if ratio:
                    x=0
                    for r in range(ratio):
                        PATTERN[str(i)].insert(1+x, SEGMENT_LINEBOTH)
                        PATTERN[str(i)].insert(3+x, SEGMENT_LINEBOTH)
                        x+=1

        numbers = list(str(self.convert_number_to_lcd))
        # Concatenate the patterns lists of digits
        lcd_result=[]
        len_numbers = len(numbers)
        for i in range(0,len_numbers):
            lcd_result += PATTERN[numbers[i]]
          
        line=''
        for k in range(0,(ratio*2+DefaultValue.CLD_VTL_DFLT_VAL.value)):
            for i in range(k,len(lcd_result), (ratio*2+DefaultValue.CLD_VTL_DFLT_VAL.value)):
                line += lcd_result[i]
            print(line)
            line=''
        
    @property
    def get_ratio(self)-> int:
        return self.lcd_height - DefaultValue.CLD_VTL_DFLT_VAL.value
 
lcd_x = Pattern()
lcd_x.which_number_to_lcd(the_num=3905, the_height=5, the_width=3)
lcd_x.build_digit_lcd()

