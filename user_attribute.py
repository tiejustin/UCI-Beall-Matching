class Project:

    def __init__(self, name="", industry="", description="", mentor=[]):
        self.name = name
        self.industry = industry
        self.description = description
        self.mentor = mentor

    def get_name(self):
        return self.name

    def get_industry(self):
        return self.industry

    def get_description(self):
        return self.description

    def get_mentor(self):
        return self.mentor

    def add_mentors(self, mentor_list):
        self.mentor = []
        for i in mentor_list:
            self.mentor.append(i)

