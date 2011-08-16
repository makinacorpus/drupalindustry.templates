#/usr/bin/env/python
#

from paste.script.templates import var
from base import MyTemplate, getdefaults


class DrupalBuildoutTemplate(MyTemplate):
    """Drupal's buildout template."""
    _template_dir = 'tmpl/buildout'
    defaults = getdefaults('buildout')
    summary = "A Buildout to deploy a Drupal project."

    def pre(self, command, output_dir, vars):
        """."""
        if not 'with_drush' in vars.keys():
            vars['with_drush'] = self.defaults['drush']
        self.boolify(vars)


class DrupalModuleTemplate(MyTemplate):
    """Template to generate a new Drupal module."""
    _template_dir = 'tmpl/module'
    summary = "A blank Drupal module."
    defaults = getdefaults('module')

    def __init__(self, name):
        super(DrupalModuleTemplate, self).__init__(name)
        self.vars = [
            var('name', 'Human-readabale name'),
            var('description', 'Description of the module'),
            var('core_version', 'Core version', default=self.defaults['core_version']),
            var('version', 'Version of the module', default=self.defaults['version']),
            var('package', 'Package', default=self.defaults['package']),
        ]

    def pre(self, command, output_dir, vars):
        self.boolify(vars)

# vim:set et sts=4 ts=4 tw=80:
