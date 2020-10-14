from django.conf import settings

from systems.plugins.index import BaseProvider

import pandas as pd


class Provider(BaseProvider('source', 'xls_file')):

    def load(self):
        return pd.read_excel(
            settings.MANAGER.index.get_module_file(self.field_file),
            self.field_sheet
        )
