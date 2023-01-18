def print_outline():
    print('-'*40)

class Card():
    def __init__(self):
        self.last_name = ''
        self.first_name = ''
        self.job_title = ''
        self.id = ''
        self.email = ''
        self.phone_num = ''
        self.f_first_name = ''
        self.f_last_name = ''
        self.f_email = ''
        self.f_job_title = ''

        self.eye = ''
        self.hair = ''
        self.bmonth = ''
        self.train = ''
        self.f_bmonth = ''


    def get_info(self):
        self.first_name = input('First name: ')
        self.last_name = input('Last name: ')
        self.email = input('Email address: ')
        self.phone_num = input('Phone number: ')
        self.job_title = input('Job title: ')
        self.id = input('ID Number: ')

    def format_info(self):
        self.f_first_name = self.first_name.title()
        self.f_last_name = self.last_name.upper()
        self.f_email = self.email.lower()
        self.f_job_title = self.job_title.title()
        self.f_bmonth = self.bmonth.title()

    def print_card(self):
        print_outline()
        print(f'{self.f_last_name}, {self.f_first_name} '
              f'\n{self.f_job_title} \n'
              f'ID: {self.id} '
              f'\n\n{self.f_email} '
              f'\n{self.phone_num}'
              f'\n\n{self.hair:<16} {self.eye}')
        print_outline()


def main():
    card1 = Card()
    card1.get_info()
    card1.format_info()
    print('\nThe ID Card is:')
    card1.print_card()


main()


