from systems.commands.index import Command
from utility.data import get_identifier

import pandas as pd
import numpy as np
import tensorflow_hub as hub


class Classify(Command('course.classify')):

    def exec(self):
        self.info("Loading Tensorflow model from: {}".format(self.tensorflow_model))
        google_use = hub.load(self.tensorflow_model)

        self.info("Calculating competency name similarities")
        competency_names = list(self._competency.field_values('name'))
        competency_name_embeddings = google_use(competency_names)

        self.info("Calculating competency definition similarities")
        competency_definitions = list(self._competency.field_values('definition'))
        competency_definition_embeddings = google_use(competency_definitions)

        def find_similarities(text, embeddings):
            text_embedding = google_use([text])
            use_similarity = np.inner(embeddings, text_embedding)
            return pd.Series(use_similarity.T[0], index = [*competency_names])

        for course in self._course.all():
            self.info("Calculating course name competency matches for {}".format(course.name))
            name_similarity = find_similarities(course.name, competency_name_embeddings)

            self.info("Calculating course description competency matches for {}".format(course.name))
            definition_similarity = find_similarities(course.description, competency_definition_embeddings)

            self.info("Calculating final course competency matches for {}".format(course.name))
            similarity = (self.name_weight * name_similarity) + ((1 - self.name_weight) * definition_similarity)
            sorted_series = similarity.sort_values(ascending = False)[0:self.top_competencies]

            for related_competency_name, correlation in sorted_series.items():
                self.info("Saving course competency correlations for: {}".format(related_competency_name))
                related_competency = self._competency.retrieve(related_competency_name)

                relationship, created = self._course_correlation.model.objects.get_or_create(
                    course = course,
                    competency = related_competency
                )
                relationship.correlation = correlation
                relationship.save()

                course.course_correlations.add(relationship)

        self.success("Sucessfully completed course classification")
