from systems.models.index import Model


class CourseCorrelation(Model('course_correlation')):

    def __str__(self):
        return "{}/{} ({})".format(self.course.name, self.competency.name, self.id)
