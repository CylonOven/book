import datetime

from ..settings import *


class Site(Site):
    project_name = 'cosi_be_fr'
    is_demo_site = True
    # ignore_dates_after = datetime.date(2019, 05, 22)
    the_demo_date = datetime.date(2015,3, 12)

SITE = Site(globals())
DEBUG = True
