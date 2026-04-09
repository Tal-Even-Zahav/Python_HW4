''' Exercise #4. Python for Engineers.'''


class Minibar:
    def __init__(self, drinks={}, snacks={}):
        self.drinks = drinks
        self.snacks = snacks
        self.bill = 0

    def __repr__(self):
        if self.bill == 0:
            return ("Drinks: " + ", ".join(self.drinks.keys()) + "\nSnacks: " + ", ".join(self.snacks) + "\nNo bill yet")
        else:
            return ("Drinks: " + ", ".join(self.drinks.keys()) + "\nSnacks: " + ", ".join(self.snacks) + "\nBill: " + str(self.bill))

    def eat(self, snack):
        snack = snack.lower()
        if snack in self.snacks:
            self.bill += self.snacks.pop(snack, 0)
        elif not self.snacks:
            print("No snacks left")
        else:
            print("The snack " + snack + " was not found.")

    def drink(self, drink):
        drink = drink.lower()
        if drink in self.drinks:
            self.drinks[drink] -= 1
            self.bill += 20
            if self.drinks[drink] == 0:
                del self.drinks[drink]
        elif not self.drinks:
            print("No drinks left")
        else:
            print("The drink " + drink + " was not found.")

#########################################
# Question 2 - do not delete this comment
#########################################
class Room:
    def __init__(self, minibar, number, guests, clean_level, is_suite, satisfaction=0.5):
        self.minibar = minibar
        self.number = int(number)
        self.guests = []
        for name in guests:
            self.guests.append(name.lower())
        self.clean_level = clean_level
        self.is_suite = is_suite
        self.satisfaction = satisfaction
        if self.is_error_type():
            print("TypeError")
        if self.is_error_value():
            print("ValueError")


    def is_error_type(self):
        c = 0
        for name in self.guests:
            if type(name) != str:
                c = c + 1
        if type(self.clean_level) != int:
            clean_level = int(self.clean_level)
            c = c+1
        if type(self.is_suite) != bool:
            c = c+1
        if type(self.satisfaction) != float and self.satisfaction != (0 or 1):
            self.satisfaction = float(satisfaction)
            c = c+1
        if c > 0 :
            return True
        else:
            return False

    def is_error_value(self):
        d = 0
        room_infloor = self.number - (self.number//100)*100
        if self.number < 100 or self.number > 930 or room_infloor > 30 or room_infloor == 0:
            d +=1
        if self.satisfaction < 0 or self.satisfaction > 1:
            self.satisfaction = 0.5
            d +=1
        if d > 0:
            return True
        else:
            return False


    def __repr__(self):
        guests_info = ""
        if self.guests == []:
            guests_info ="Guests: empty"
        else:
            guests_info = "Guests: " + ", ".join(sorted(self.guests))
        return f"Room number: {self.number}\n{guests_info}\nClean level: {self.clean_level}\nIs suite: {self.is_suite}\nSatisfaction: {self.satisfaction}\nMinibar:\n{self.minibar}"

    def is_occupied(self):
        if self.guests != []:
            return True
        else:
            return False

    def clean(self):
        self.clean_level = min(15, self.clean_level + 1 + int(self.is_suite))

    def better_than(self, other):
        if self.is_suite and not other.is_suite:
            return True
        if not self.is_suite and other.is_suite:
            return False
        else:
            if self.number//100 > other.number// 100:
                return True
            if self.number // 100 < other.number // 100:
                return False
            else:
                if self.clean_level > other.clean_level:
                    return True
                if self.clean_level < other.clean_level:
                    return False
                else:
                    return False

    def check_in(self, guests):
        if self.guests == []:
            self.guests.extend(name.lower() for name in guests)
            self.satisfaction = 0.5
        else:
            print("Cannot check-in new guests to an occupied room")

    def check_out(self):
        if self.guests != []:
            self.guests = []
            self.minibar.bill = 0
        else:
            print("cannot check-out an empty room")
    
    def move_to(self, other):
        if self.guests == []:
            print("Cannot move guests from an empty room")
        if other.guests != []:
            print("Cannot move guests to an occupied room")
        else:
            other.guests = self.guests
            other.minibar.bill = self.minibar.bill
            self.minibar.bill = 0
            if not self.better_than(other):
                other.satisfaction = min(1.0,self.satisfaction+0.1)
            else:
                other.satisfaction = self.satisfaction
            self.guests = []


#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
            
    def __repr__(self):
        return f"{self.name} Hotel has: {self.occupied_num()} occupied rooms."

    def occupied_num(self):
        f=0
        for room in self.rooms:
            if room.guests != []:
                f +=1
        return f"{f}/{len(self.rooms)}"

    def check_in(self, guests, is_suite):
        for room in self.rooms:
            if room.guests == [] and room.is_suite == is_suite:
                room.guests.extend(name.lower() for name in guests)
                return room
        else:
            return None

    def check_out(self, guest):
        for room in self.rooms:
            if guest.lower() in room.guests:
                room.check_out()
                return room
        else:
            return None

    def upgrade(self, guest):
        for room1 in self.rooms:
            if guest.lower() in room1.guests:
                for room2 in self.rooms:
                    if room2.guests == [] and room2.better_than(room1):
                        room1.move_to(room2)
                        return room2
        else:
            return None



    def send_cleaner(self, guest):
        for room in self.rooms:
            if guest.lower() in room.guests:
                room.clean()
                return room
        else:
            return None



#########################################
# Question 4 - do not delete this comment
#########################################

class Roman:
    
    def get_int_from_roman(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_string = self.roman_value.strip('-')
        int_val = 0
        for counter in range(len(roman_string)):
            if counter > 0 and rom_val[roman_string[counter]] > rom_val[roman_string[counter - 1]]:
                int_val += rom_val[roman_string[counter]] - 2 * rom_val[roman_string[counter - 1]]
            else:
                int_val += rom_val[roman_string[counter]]
        int_val = -int_val if self.is_neg else int_val
        return int_val
    
    def get_roman_from_int(self):
        num = self.int_value if not self.is_neg else -self.int_value
        roman_num = '' if not self.is_neg else '-'
        counter = 0
        
        roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        int_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        while num > 0:
            for _ in range(num // int_vals[counter]):
                roman_num += roman_char[counter]
                num -= int_vals[counter]
            counter += 1
        return roman_num
    
    def __init__(self, input_value):
        if type(input_value) == int:
            self.int_value = input_value
            if input_value < 0:
                self.is_neg = True
            else:
                self.is_neg = False
            self.roman_value = self.get_roman_from_int()
        if type(input_value) == str:
            self.roman_value = input_value
            if input_value.startswith("-"):
                self.is_neg = True
            else:
                self.is_neg = False
            self.int_value = self.get_int_from_roman()

    def __repr__(self):
        return f"int: {self.int_value}; Roman Numeral: '{self.roman_value}'"

    def __neg__(self):
        return Roman(-self.int_value)

    def __add__(self, other):
        if type(other) == int:
            num = self.int_value + other
            if num == 0:
                return("Unsupported result")
            else:
                return Roman(num)
        if type(other) == Roman:
            num = self.int_value + other.int_value
            if num == 0:
                return("Unsupported result")
            else:
                return Roman(num)

    def __lt__(self, other):
        if type(self) and type(other) == Roman:
            if self.int_value < other.int_value:
                return True
            else:
                return False
        if type(self) == Roman and type(other) == int :
            if self.int_value < other:
                return True
            else:
                return False
        if type(self) == int and type(other) == Roman:
            if self < other.int_value:
                return True
            else:
                return False
    
    def __gt__(self, other):
        if type(self) and type(other) == Roman:
            if self.int_value > other.int_value:
                return True
            else:
                return False
        if type(self) == Roman and type(other) == int:
            if self.int_value > other:
                return True
            else:
                return False
        if type(self) == int and type(other) == Roman:
            if self > other.int_value:
                return True
            else:
                return False
    

    def __floordiv__(self, other):
        if type(other) == int:
            num = self.int_value // other
            if num == 0:
                return("Unsupported result")
            else:
                return Roman(num)
        if type(other) == Roman:
            num = self.int_value // other.int_value
            if num == 0:
                return("Unsupported result")
            else:
                return Roman(num)




if __name__ == '__main__':
    def test_hotel():
        m1 = Minibar({'coke': 10, 'lemonade': 1}, {'bamba': 8, 'mars': 12})
        m2 = Minibar({'beer': 10, 'lemonade':4}, {'m&m': 6})
        rooms = [Room(m2, 514, [], 5, True),
                 Room(m2, 210, ["Ronen", "Shir"], 6, True),
                 Room(m1, 102, ["Liat"], 7, False),
                 Room(m2, 223, [], 6, True)]
        h = Hotel("Dan", rooms)
        test_sep = '\n------------------'
        print('PRINT m1:\n', m1, test_sep, sep="")
        print('PRINT m2:\n', m2, test_sep, sep="")
        print('PRINT h:\n', h, test_sep, sep="")
        liat_room = h.send_cleaner('Liat')
        print('CALL: h.send_cleaner("Liat")\n', liat_room, test_sep, sep="")
        print('CALL: liat_room.eat("bamba")\n', liat_room.minibar.eat("bamba"), test_sep, sep="")
        print('PRINT liat_room.minibar:\n', liat_room.minibar, test_sep, sep="")
        print('CALL: liat_room.drink("lemonade")\n', liat_room.minibar.drink("lemonade"), test_sep, sep="")
        print('PRINT liat_room.minibar:\n', liat_room.minibar, test_sep, sep="")
        print('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")

        print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
        print('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
        print('CALL: h.check_in(["Alice", "Wonder"], True)\n',
              h.check_in(["Alice", "Wonder"], True), test_sep, sep="")
        print('CALL: h.check_in(["Alex"], True)\n', h.check_in(["Alex"], True), test_sep,
              sep="")
        print('PRINT h:\n', h, test_sep, sep="")
        print('CALL: h.check_in(["Oded", "Shani"], False)\n',
              h.check_in(["Oded", "Shani"], False), test_sep, sep="")
        print('CALL: h.check_in(["Oded", "Shani"], False)',
              h.check_in(["Oded", "Shani"], False), test_sep, sep="")
        print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
        print('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
        print('PRINT h:\n', h, test_sep, sep="")


    # After you are done implementing all classes and methods, you can compare the results with the file test_hotel_output.txt
    test_hotel()

    print('==== Q4: Basic tests/output====')
    r2 = Roman(2)
    print(Roman(2))
    print(repr(r2))
    print('====')
    print(-Roman("IV"))
    print('====')
    r5 = Roman(2) + 3
    print(r5)
    print(repr(r5))
    print(repr(Roman(6) // -5))

    #my checks
    print(Roman(5) + Roman(6))
    print(Roman('V')+ 6)
    print(Roman(5)+Roman(-6))
    print(Roman('V') + (-5))
    print(Roman(7) > Roman(6))
    print(Roman('L') > 6)
    print(5 > 3)
    print( 8 > Roman(6))
    print(Roman(6) // Roman(5))
    print(Roman('VI') // 5)
    print(Roman(6) //Roman('-V'))
    print(Roman(6) // -5)