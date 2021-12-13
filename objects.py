class character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 10
        self.strength = 0
    def get_health(self):
        print(self.name + " is at " + str(self.health) + " health")
        return self.health
    def get_strength(self):
        print(self.name + " is at " + str(self.strength) + " strength")
        return self.strength
    def get_name(self):
        print(self.name + " is my name")
        return self.name
    def get_age(self):
        print(str(self.age) + " is my age")
        return self.age
class hero(character):
    def __init__(self, name, age):
        character.__init__(self, name, age)
        self.stormlight= 100
        self.health = 100
        self.strength = 100
    def use_lash_1(self):
       self.stormlight -= 5
       print ("Stormlight level of " + self.name + " is " + str(self.stormlight) + " from lash 1 used")
    def get_stormlight(self):
        print(self.name + "is @ the stormlight level of" + str(self.stormlight))
        return self.stormlight
    def get_order(self):
        print(self.name + " is a Windrunner")
    def get_oaths(self):
        print("""
Life before Death
Strength before Weakness
Journey before Destination

""")
     
    def use_lash_3(self):
        self.stormlight -= 25
        print ("Stormlight level of " + self.name + "is " + str(self.stormlight) + " from lash 2 used")
    def use_lash_2(self):
       self.stormlight -= 10
       print ("Stormlight level of " + self.name + " is " + str(self.stormlight) + " from lash 2 used")
class villain(character):
    def __init__(self, name, age):
        character.__init__(self, name, age)
        self.resistance = 66
        self.health = 100
        self.strength = 50
    def get_resistance(self):
        print("Resistance level of " + self.name + " @" + str(self.resistance))
        return self.resistance
class boss(villain):
    def __init__(self, name, age):
        villain.__init__(self, name, age)
        self.resistance = 70
        self.voidlight = 150
        self.health = 100
        self.strength = 200
    def get_voidlight(self):
        print("Voidlight level of " + self.name + " @" + str(self.voidlight))
        return self.voidlight
#end of classes
#definitions
def intro_credits():
    print('''
    Underneath Urithiru : A Fan Based Creation
    All character and ideas are from the Stormlight Archive written by Brandon Sanderson''')
    print('''
    Current books in the Cosmere(which includes the Stormlight Archive) are:
    
    
        From the planet Nalthis:
            Warbreaker
        
        From the planet Roshar:
            The Stormlight Archive: The Way of Kings
            The Stormlight Archive: Words of Radiance
            The Stormlight Archive: Oathbringer
            The Stormlight Archive: Rhythm of War
        
        From the planet Scadrial:
            
            Era 1:
                Mistborn: The Final Empire
                The Well of Ascension
                The Hero of Ages
            Era 2:
                Wax and Wayne: The Alloy of Law
                Wax and Wayne: Shadows of Self
                Wax and Wayne: The Bands of Mourning
                Wax and Wayne: The Lost Metal(Unreleased)
        
        From the planet Sel:
            Elantris
            The Emperor's Soul
        
        From the planet Taldian:
            White Sand
            
        )
        ''')
        
def test1():
    d = hero("Tanavast", 90)
    f = villain("Moash", 88)
    g = boss("Odium", 999)
    d.use_lash_3()
    while d.stormlight > 10 :
        d.use_lash_1()
        d.stormlight +=3
        d.use_lash_2()
    d.get_order()
    d.get_name()
    d.get_age()
    d.get_oaths()
    d.get_health()
    d.get_strength()
    f.get_name()
    f.get_age()
    f.get_resistance()
    f.get_health()
    f.get_strength()
    g.get_name()
    g.get_age()
    g.get_resistance()
    g.get_voidlight()
    g.get_health()
    g.get_strength()
def test2():
    
    c1()
    c2()
    c3()
    c4()
def c1():
    s = character("BobTheCharacter", 1)
    s.get_name()
    s.get_age()
    s.get_health()
    s.get_strength()
def c2():
    d = hero("BobtheHero", 2)
    d.get_name()
    d.get_age()
    d.get_health()
    d.get_strength()
    d.get_stormlight()
    d.use_lash_1()
    d.use_lash_2()
    d.use_lash_3()
    d.get_order()
    d.get_oaths()
def c3():
    f = villain("BobTheVillain", 3)
    f.get_name()
    f.get_age()
    f.get_health()
    f.get_strength()
    f.get_resistance()
def c4():
    g = boss("BobTheBoss", 4)
    g.get_name()
    g.get_age()
    g.get_health()
    g.get_strength()
    g.get_resistance()
    g.get_voidlight()

def Start1():
    intro_credits()
    x = raw_input("Press Enter to Continue(to Test #2):")
    if x == "":
        test2()
    y = raw_input("Press Enter to Continue(to Test #1):")
    if x == "":
        test1()
#end of definitions
#start
#ww = raw_input("Press Enter to begin:")
#if ww == "":
    #Start1() 


