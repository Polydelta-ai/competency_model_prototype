from systems.models.index import Model


class Competency(Model('competency')):

    def __str__(self):
        return "{} ({})".format(self.name, self.id)
