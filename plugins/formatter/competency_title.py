from systems.plugins.index import BaseProvider

import re


class Provider(BaseProvider('formatter', 'competency_title')):

    def format(self, value):
        return value
