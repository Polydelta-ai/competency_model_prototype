from systems.plugins.index import BaseProvider


class Provider(BaseProvider('source', 'correlation')):

    def load(self):
        file_data = pandas.read_csv(
            settings.MANAGER.index.get_module_file(self.field_file),
            sep = self.field_separator,
            engine = 'python'
        )
        return pandas.DataFrame(file_data, columns = self.import_columns).drop_duplicates(self.import_columns)
