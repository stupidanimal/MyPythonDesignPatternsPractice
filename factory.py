from abc import ABCMeta,abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print('Personal Section')

class AlbumSection(Section):
    def describe(self):
        print('Album Section')

class PatentSection(Section):
    def describe(self):
        print('PatenSection')

class PublicationSection(Section):
    def describe(self):
        print('Publication Section')


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSections(self,section):
        self.sections.append(section)

class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PulicationSection())

class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile = eval('facebook')()
    psections = profile.getSections()
    for x in psections:
        x.describe()





print('this is the end of program')