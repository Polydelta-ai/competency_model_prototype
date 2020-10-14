from systems.commands.index import Command

import pandas as pd
import numpy as np
import tensorflow_hub as hub


class Correlations(Command('competency.correlations')):

    def exec(self):
        self.info("Loading Tensorflow model from: {}".format(self.tensorflow_model))
        google_use = hub.load(self.tensorflow_model)
        names = list(self._competency.field_values('name'))

        def find_similarities(input):
            if isinstance(input, str):
                values = list(self._competency.field_values(input))
            else:
                values = input

            embeddings = google_use(values)
            return pd.DataFrame(
                np.inner(embeddings, embeddings),
                index = names,
                columns = names
            )

        self.info("Calculating competency name similarities")
        name_similarity = find_similarities(names)

        self.info("Calculating competency definition similarities")
        definition_similarity = find_similarities('definition')

        self.info("Calculating final competency similarities")
        similarity = (self.name_weight * name_similarities) + ((1 - self.name_weight) * definition_similarities)

        for competency_name in name_similarities.columns:
            self.info("Saving competency correlations for: {}".format(competency_name))
            competency = self._competency.retrieve(competency_name)

            series = similarity[competency_name]
            sorted_series = series.sort_values(ascending = False)[1:self.top_competencies + 1]

            for related_competency_name, correlation in sorted_series.items():
                related_competency = self._competency.retrieve(related_competency_name)

                relationship, created = self._competency_correlation.model.objects.get_or_create(
                    competency1 = competency,
                    competency2 = related_competency
                )
                relationship.correlation = correlation
                relationship.save()

                competency.competency_correlations.add(relationship)

        self.success("Sucessfully completed competency correlations")
