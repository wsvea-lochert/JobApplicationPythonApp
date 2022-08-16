# main.py
# Code written by William Svea-Lochert
import requests


class Education:
    def __init__(self, record: dict):
        """
        Initializes the education class
        :param record: dictionary with the education record
        """
        self.record = record
        self.school, self.field, self.graduation, self.grades = self.set_edu()

    def set_edu(self):
        """
        Sets the education record
        :return: returns the records
        """
        return self.record['school'], self.record['field'], self.record['graduation'], self.record['grades']

    def print_edu(self):
        """
        Prints the education record
        """
        print('# ------------------------------------------------ #')
        print(f'Skole: {self.school}')
        print(f'Studie: {self.field}')
        print(f'Fullført: {self.graduation}')
        print('--------------------------------------------------')
        for grade in self.grades:
            print(f'{grade:<40} | \t{self.grades[grade]}\t|')


class Job:
    def __init__(self, record: dict):
        """
        Initializes the job class
        :param record: dictionary with the job record
        """
        self.record = record
        self.company, self.position, self.start, self.end, self.description = self.set_job()

    def set_job(self):
        """
        Sets the job record
        :return: returns the records
        """
        return self.record['company'], self.record['position'], self.record['start'], self.record['end'], self.record['description']

    def print_job(self):
        """
        Prints the job record
        """
        print('# ------------------------------------------------ #')
        print(f'Bedrift: {self.company}')
        print(f'Stilling: {self.position}')
        print(f'Start: {self.start}')
        print(f'{self.description}')


class Projects:
    def __init__(self, record: dict):
        """
        Initializes the projects class
        """
        self.record = record
        self.name, self.employer, self.authors, self.description, self.link = self.set_projects()

    def set_projects(self):
        """
        Sets the projects record
        :return: returns the records
        """
        return self.record['name'], self.record['employer'], self.record['authors'], self.record['description'], self.record['link']

    def print_projects(self):
        """
        Prints the projects record
        """
        print('# ------------------------------------------------ #')
        print(f'Prosjekt: {self.name}')
        print(f'Bedrift: {self.employer}')
        print('Forfattere:', ', '.join(self.authors))

        # split the description into lines
        description = self.description.split('. ')
        for line in description:
            print(f'{line:<40}.')
        print(f'Link: {self.link}')


class Person:
    def __init__(self):
        """
        Get the data from the API and make a list of Education objects
        """
        self.json = self.get_json()
        self.education = self.make_education()
        self.jobs = self.make_job()
        self.projects = self.make_projects()

        self.name = self.json['name']
        self.age = self.json['age']
        self.motivation = self.json['motivation']
        self.programming_languages = self.json['programming_languages']
        self.website = self.json['website']

    @staticmethod
    def get_json():
        """
        Get the json from the API
        :return:
        """
        url = "https://wsvea-lochert.github.io/william.json"
        r = requests.get(url)
        return r.json()

    def make_education(self):
        """
        Make a list of Education objects
        :return:
        """
        ed_list = []
        ed_dict = self.json['education']

        for ed in ed_dict:
            ed_list.append(Education(ed_dict[ed]))

        return ed_list

    def get_edu(self):
        """
        Print all the education
        """
        print("                     Min Utdanning                  ")
        for ed in self.education:
            ed.print_edu()

    def make_job(self):
        """
        Make a list of Job objects
        :return:
        """
        job_list = []
        job_dict = self.json['job_experience']

        for job in job_dict:
            job_list.append(Job(job_dict[job]))

        return job_list

    def get_job(self):
        """
        Print all the jobs
        """
        for job in self.jobs:
            if job is not None:
                job.print_job()

    def make_projects(self):
        """
        Make a list of Project objects
        :return:
        """
        pro_list = []
        pro_dict = self.json['projects']

        for pro in pro_dict:
            pro_list.append(Projects(pro_dict[pro]))

        return pro_list

    def get_projects(self):
        """
        Print all the projects
        """
        for pro in self.projects:
            if pro is not None:
                pro.print_projects()

    def get_motivation(self):
        """
        Prints the motivation
        """
        print('# ------------------------------------------------ #')
        # split self.motivation into lines
        motivation = self.motivation.split('. ')
        for line in motivation:
            print(f'{line:<40}.')
        print('# ------------------------------------------------ #')

    def get_hobby(self):
        """
        Prints the hobbies
        """
        print('# ------------------------------------------------ #')
        # print hobbies on one line
        print(f'Mine hobbyer: {", ".join(self.json["hobby"])}')
        print('# ------------------------------------------------ #')

    def get_programming_languages(self):
        """
        Prints the programming languages
        """
        print('# ------------------------------------------------ #')
        # print programming languages on one line
        print(f'Språk jeg har erfaring med: {", ".join(self.programming_languages)}')
        print('# ------------------------------------------------ #')

    def who_am_i(self):
        """
        Prints the name and motivation
        """
        print('# ------------------------------------------------ #')
        print(f'Mitt navn er {self.name} jeg er født {self.age} og er 24 år gammel.'
              f'\nJeg er fra Drøbak, og bor også her for øyeblikket.'
              f'\nLink til min side: {self.website}')
        print('# ------------------------------------------------ #')


def create_space():
    for i in range(0, 20):
        print()


def main():
    will = Person()
    print("Hei, velkommen til denne jobbsøknadden!")
    while True:
        user_input = input("1: Hvem er jeg? \n2: Utdanning \n3: Arbeidserfaring \n4: Motivasjon \n5: Hobby \n6: Programmerings språk \n7: Prosjekter \n8: Avslutt \nVelg et alternativ: ")
        if user_input == '1':
            create_space()
            will.who_am_i()
        elif user_input == '2':
            create_space()
            will.get_edu()
        elif user_input == '3':
            create_space()
            will.get_job()
        elif user_input == '4':
            create_space()
            will.get_motivation()
        elif user_input == '5':
            create_space()
            will.get_hobby()
        elif user_input == '6':
            create_space()
            will.get_programming_languages()
        elif user_input == '7':
            create_space()
            will.get_projects()

        elif user_input == '8':
            print("Takk for at du tittet innom, håper å høre fra deg!")
            break
        else:
            create_space()
            print("Ugyldig valg. prøv igjen.")
            continue

        input("Trykk enter for å fortsette...")
        create_space()


# call main function
if __name__ == "__main__":
    main()

