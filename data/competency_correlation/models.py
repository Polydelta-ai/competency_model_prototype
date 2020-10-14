from systems.models.index import Model


class CompetencyCorrelation(Model('competency_correlation')):

    def __str__(self):
        return "{}/{} ({})".format(self.competency1.name, self.competency2.name, self.id)
