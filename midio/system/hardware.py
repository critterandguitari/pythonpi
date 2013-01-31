
class HardwareInput:
    
    next_patch = False
    knob1 = 200
    knob2 = 200
    knob3 = 200
    clear_screen = False
    note_on = False
    note_off = False

    note_ch = 1
    note_velocity = 0
    note_note = 60
    
    def parse_serial(self, line):
        array = line.split(',')
        print array
     
        # basic parse next command
        if len(array) == 1:
            if array[0] == "n" :
                self.next_patch = True
                print "NEXT"

        # basic parse of knob array
        if len(array) == 4 :
            if array[0] == "k" :
                if array[1].isdigit() :
                    self.knob1 = int(array[1])
                if array[2].isdigit() :
                    self.knob2 = int(array[2])
                if array[3].isdigit() :
                    self.knob3 = int(array[3])

        # basic parse sd key (this is supposed to be mapped to shutdowh -h now)
        if len (array) == 1:
            if array[0] == "sd": 
                self.clear_screen = True
        
        # basic parse note on command
        if len(array) == 4:
            if array[0] == "no" :
                self.note_on = True
                if array[1].isdigit() :
                    self.note_ch = int(array[1])
                if array[2].isdigit() :
                    self.note_note = int(array[2])
                if array[3].isdigit() :
                    self.note_velocity = int(array[3])
 
        # basic parse note on command
        if len(array) == 4:
            if array[0] == "nf" :
                self.note_off = True
                if array[1].isdigit() :
                    self.note_ch = int(array[1])
                if array[2].isdigit() :
                    self.note_note = int(array[2])
                if array[3].isdigit() :
                    self.note_velocity = int(array[3])

 

 

    def clear_flags(self):
        self.next_patch = False
        self.clear_screen = False
        self.note_on = False
        self.note_off = False
      


