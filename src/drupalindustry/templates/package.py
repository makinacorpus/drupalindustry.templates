# coding=utf8
import os
from datetime import date

from paste.script.templates import var

from base import BaseTemplate, getdefaults


class DrupalBuildoutBootstrapTemplate(BaseTemplate):
    """Drupal's buildout boostrap template.

    Buildout bootstrap includes bootstrap.py and minimal buildout configuration
    file to installs drupalindustry.templates package.
    """
    _template_dir = 'tmpl/buildout_bootstrap'
    summary = "Bootstrap script and configuration file for buildout + " \
              "drupalindustry.templates package."
    vars = []


class DrupalBuildoutTemplate(BaseTemplate):
    """Drupal's buildout template."""
    _template_dir = 'tmpl/buildout'
    defaults = getdefaults('buildout')
    summary = "A Buildout to deploy a Drupal project."
    vars = [var('with_drush', 'Generate drush script', default=defaults['with_drush']),
            var('with_sphinx', 'Use sphinx as documentation tool', default=defaults['with_sphinx']),
            var('with_jenkins', 'Install Jenkins continuous integration server?', default=defaults['with_jenkins']),
            var('php', 'Which php? Empty string to let drush guess.', default=defaults['php']),
            var('drupal_root', 'Path to Drupal root.', default=defaults['drupal_root']),
            ]


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
        if not 'server_root' in vars.keys():
            vars['project_root'] = os.path.join(os.getcwd(), vars['project'])
        if not 'http_port' in vars.keys():
            vars['http_port'] = self.defaults['http_port']


class DrupalPHPIniTemplate(BaseTemplate):
    """PHP configuration file template."""
    _template_dir = 'tmpl/php_ini'
    summary = "A php.ini file for a Drupal project."

    vars = []

    def pre(self, command, output_dir, vars):
        """Prepare template generation."""
        super(DrupalPHPIniTemplate, self).pre(command, output_dir, vars)


class DrushSiteMakefileTemplate(BaseTemplate):
    """Template to generate a drush makefile for a site installation."""
    _template_dir = 'tmpl/drush_site_makefile'
    defaults = getdefaults('drush_site_makefile')
    summary = "A minimal drush makefile to install a site based on a profile."

    vars = [var('site', 'Site name', default=defaults['site']),
            var('api_version', 'API version', default=defaults['api_version']),
            var('core_version', 'Drupal core version', default=defaults['core_version']),
            var('with_profile', 'Install a profile?', default=defaults['with_profile']),
            var('profile_download_type', 'Profile download type', default=defaults['profile_download_type']),
            var('profile_download_url', 'Profile download URL', default=defaults['profile_download_url']),
            var('profile_download_branch', 'Profile download branch', default=defaults['profile_download_branch']),
            var('with_developer_tools', 'Install developer tools?', default=defaults['with_developer_tools']),
            ]

    def pre(self, command, output_dir, vars):
        """Prepare template generation."""
        super(DrushSiteMakefileTemplate, self).pre(command, output_dir, vars)


class DrupalSiteDocumentationTemplate(BaseTemplate):
    """Template to initiate the documentation of a Drupal project (site)."""
    _template_dir = 'tmpl/docs'
    defaults = getdefaults('docs')
    summary = "Documentation quickstart for a Drupal project."

    vars = [var('project_title', 'Project title', default=''),
            var('project_slug', 'Project machine name (alphanumeric and underscores)', default=''),
            var('author_name', 'Author name', default=''),
            var('author_email', 'Author email', default=''),
            var('version', 'Short version (i.e. 1.0)', default=defaults['version']),
            var('release', 'Full version (i.e. 1.0.1beta2)', default=defaults['release']),
            var('language', 'Language', default=defaults['language']),
            ]

    def pre(self, command, output_dir, vars):
        """Prepare template generation."""
        vars['year'] = '%s' % date.today().year
        super(DrupalSiteDocumentationTemplate, self).pre(command, output_dir, vars)

# vim:set et sts=4 ts=4 tw=80:
