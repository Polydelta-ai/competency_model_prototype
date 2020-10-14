from systems.models.index import Model


class Course(Model('course')):

    def __str__(self):
        return "{} ({})".format(self.name, self.course_code)
