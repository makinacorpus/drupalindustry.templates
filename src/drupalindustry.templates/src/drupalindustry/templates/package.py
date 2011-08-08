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

# vim:set et sts=4 ts=4 tw=80:
