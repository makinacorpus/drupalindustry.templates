#/usr/bin/env/python
#
import os
from paste.script.templates import var
from base import BaseTemplate, getdefaults


class DrupalBuildoutTemplate(BaseTemplate):
    """Drupal's buildout template."""
    _template_dir = 'tmpl/buildout'
    defaults = getdefaults('buildout')
    summary = "A Buildout to deploy a Drupal project."

    def pre(self, command, output_dir, vars):
        """Prepare template generation."""
        super(DrupalBuildoutTemplate, self).pre(command, output_dir, vars)
        if not 'with_drush' in vars.keys():
            vars['with_drush'] = self.defaults['drush']


class DrupalModuleTemplate(BaseTemplate):
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


class DrupalLayoutTemplate(BaseTemplate):
    """Drupal's layout template."""
    _template_dir = 'tmpl/layout'
    summary = "A minimal default layout to deploy a Drupal project."


class DrupalApache2VhostTemplate(BaseTemplate):
    """Drupal's Apache2 vhost template."""
    _template_dir = 'tmpl/apache2_vhost'
    defaults = getdefaults('vhost')
    summary = "A minimal Apache2 vhost for a Drupal project."

    vars = [var('vhost_nb', 'Vhost number', default=defaults['vhost_nb']),
            var('vhost_ip', 'Vhost listening IP',
                default=defaults['vhost_ip']),
            var('server_name', 'ServerName', default=defaults['server_name']),
            var('server_alias', 'ServerAlias', default=''),
            ]

    def pre(self, command, output_dir, vars):
        """Prepare template generation."""
        super(DrupalApache2VhostTemplate, self).pre(command, output_dir, vars)
        if not 'server_root' in vars.keys(v):
            vars['project_root'] = os.path.join(os.getcwd(), vars['project'])
        if not 'http_port' in vars.keys():
            vars['http_port'] = self.defaults['http_port']

# vim:set et sts=4 ts=4 tw=80:
