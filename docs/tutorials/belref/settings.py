from lino_book.projects.belref.settings import *


class Site(Site):
    default_ui = 'lino.modlib.extjs'

SITE = Site(globals())

DEBUG = True

