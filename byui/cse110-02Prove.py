class Story:
    def __init__(self):
        self.adjective = ''
        self.animal = ''
        self.verb = ''
        self.exclamation = ''
        self.verb2 = ''
        self.verb3 = ''

    def get_info(self):
        self.adjective = input('Adjective: ')
        self.animal = input('Animal: ')
        self.verb = input('Present participle verb: ')
        self.exclamation = input('Exclamation: ')
        self.verb2 = input('Base verb: ')
        self.verb3 = input('Base verb: ')

    def print_story(self):
        print(f'''The other day, I was really in trouble. It all started when I saw a very
{self.adjective} {self.animal} {self.verb} down the hallway. "{self.exclamation}!" I yelled. But all
I could think to do was to {self.verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {self.verb3}
right in front of my family.''')


story1 = Story()
story1.get_info()
story1.print_story()
