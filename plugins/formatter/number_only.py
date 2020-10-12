from systems.plugins.index import BaseProvider

import re


class Provider(BaseProvider('formatter', 'number_only')):

    def format(self, value):
        value = re.sub(r'[^\d]+', '', str(value))

        if not value:
            return None
        return int(value)
