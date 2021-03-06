from lino.invlib.ns import ns
import os
pp = os.environ.get('VIRTUAL_ENV') + '/bin/per_project'
ns.setup_from_tasks(
    globals(), 'lino_book',
    # tolerate_sphinx_warnings=True,
    blogref_url="http://luc.lino-framework.org",
    coverage_command='{} inv prep test clean --batch bd'.format(pp),
    revision_control_system='git',
    # help_texts_source='docs',
    # help_texts_module='lino_xl.lib.xl',
    cleanable_files=[
        'docs/rss_entry_fragments/*',
        'docs/api/lino.*',
        'docs/api/lino_xl.*',
        'docs/api/lino_book.*'],
    demo_projects=[
        'lino_book.projects.docs.settings.demo',
        'lino_book.projects.belref.settings.demo',
        'lino_book.projects.polly.settings.demo',
        'lino_book.projects.events.settings',
        'lino_book.projects.max.settings.demo',
        'lino_book.projects.i18n.settings',
        'lino_book.projects.min1.settings.demo',
        'lino_book.projects.min2.settings.demo',
        'lino_book.projects.cms.settings.demo',
        'lino_book.projects.apc.settings.demo',
        'lino_book.projects.pierre.settings.demo',
        'lino_book.projects.cosi_ee.settings.demo',
    ])
