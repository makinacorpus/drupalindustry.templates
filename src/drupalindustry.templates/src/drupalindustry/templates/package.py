#/usr/bin/env/python
#
import os
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


class DrupalLayoutTemplate(MyTemplate):
    """Drupal's layout template."""
    _template_dir = 'tmpl/layout'
    summary = "A minimal default layout to deploy a Drupal project."


class DrupalApache2VhostTemplate(MyTemplate):
    """Drupal's Apache2 vhost template."""
    _template_dir = 'tmpl/apache2_vhost'
    defaults = getdefaults('vhost')
    summary = "A minimal Apache2 vhost for a Drupal project."

    vars = [var('vhost_nb', 'Vhost Number', default=defaults['vhost_nb']),
            var('vhost_ip', 'Vhost Listening IP',
                default=defaults['vhost_ip']),
            var('server_name', 'ServerName', default=defaults['server_name']),
            var('server_alias', 'ServerAlias', default=''),
            ]

    def pre(self, command, output_dir, vars):
        """."""
        if not 'server_root' in vars.keys():
            vars['project_root'] = os.path.join(os.getcwd(), vars['project'])
        if not 'http_port' in vars.keys():
            vars['http_port'] = self.defaults['http_port']
        self.boolify(vars)

# vim:set et sts=4 ts=4 tw=80:
