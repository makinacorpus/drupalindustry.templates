# coding=utf8
import os
from datetime import date
import sys

from paste.script.templates import var

from base import BaseTemplate, getdefaults


def guess_project_dir():
    """Try to guess and return absolute path to project dir."""
    project_dir = sys.argv[0]  # Assume we are running bin/paster
    project_dir = os.path.abspath(project_dir)
    project_dir = os.path.dirname(os.path.dirname(project_dir))
    project_dir = os.path.normpath(project_dir)
    return project_dir


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
            var('project_root', 'Project root', default=guess_project_dir()),
            var('logs_dir', 'Logs directory', default=os.path.join(guess_project_dir(), 'var', 'log', 'apache2')),
            var('tmp_dir', 'Temporary directory', default=os.path.join(guess_project_dir(), 'var', 'tmp')),
            ]
    
    def pre(self, command, output_dir, vars):
        """Prepare template generation."""
        super(DrupalApache2VhostTemplate, self).pre(command, output_dir, vars)
        if not 'http_port' in vars.keys():
            vars['http_port'] = self.defaults['http_port']

class DrupalNginxVhostTemplate(BaseTemplate):
    """Drupal's Nginx vhost template."""
    _template_dir = 'tmpl/nginx_vhost'
    defaults = getdefaults('nginxvhost')
    summary = "A Nginx vhost for a Drupal7 project."

    vars = [var('vhost_nb', 'Vhost number', default=defaults['vhost_nb']),
            var('vhost_ip', 'Vhost listening IP',
                default=defaults['vhost_ip']),
            var('server_name', 'ServerName', default=defaults['server_name']),
            var('server_alias', 'ServerAlias', default=defaults['server_alias']),
            var('project_root', 'Project root', default=guess_project_dir()),
            var('http_port', 'HTTP port', default=defaults['http_port']),
            var('nb_worker', 'Number of workers (put number of CPU)', default=int(defaults['nb_worker'])),
            var('worker_cpu_affinity', 'Workers CPU affinity (4CPU, 4 workers => 1000 0100 0010 0001)', default=defaults['worker_cpu_affinity']),
            var('worker_connections', 'Connections by worker (nb worker * nb conn  = max conn)', default=int(defaults['worker_connections']))
            ]

    def pre(self, command, output_dir, vars):
        """Prepare template generation."""
        super(DrupalNginxVhostTemplate, self).pre(command, output_dir, vars)

class DrupalPHPFpmTemplate(BaseTemplate):
    """Drupal's PHP-FPM chrooted pool configuration template."""
    _template_dir = 'tmpl/php_fpm'
    defaults = getdefaults('phpfpm')
    summary = "A php-fpm chrooted pool (fastcgi) for a Drupal7 project."

    vars = [var('pool_name', 'PHP FPM Pool nickname (short name of the project)', default=defaults['pool_name']),
            var('project_root', 'Project root', default=guess_project_dir()),
            var('pm_max_children', 'FPM Pool Size: maximum process', default=int(defaults['pm_max_children'])),
            var('pm_start_servers', 'FPM Pool Size: starting process', default=int(defaults['pm_start_servers'])),
            var('pm_min_spare_servers', 'FPM Pool Size: minimum process doing nothing', default=int(defaults['pm_min_spare_servers'])),
            var('pm_max_spare_servers', 'FPM Pool Size: maximum process doing nothing', default=int(defaults['pm_max_spare_servers'])),
            var('pm_max_requests', 'FPM Pool: max number of request in a process lifetime', default=int(defaults['pm_max_requests'])),
            var('display_errors'
              , 'Should we display errors inline (set 0 in Production!)'
              , default=int(defaults['display_errors'])),
            var('error_reporting'
              , "Error level :\nE_ALL & ~E_NOTICE -> 6135\nE_ALL -> 6143\nE_ALL^E_STRICT -> 8191\nreally all -> -1"
              , default=int(defaults['error_reporting'])),
            var('upload_max_filesize', 'max size for uploaded files', default=defaults['upload_max_filesize']),
            var('max_input_time', 'max time allowed to received the request (may be long if big uploads)', default=defaults['max_input_time']),
            var('request_terminate_timeout', 'maximum time to build HTTP answer in the PHP process', default=defaults['request_terminate_timeout']),
            var('memory_limit', 'Memory Limit per process', default=defaults['memory_limit']),
            var('allow_url_fopen', 'allow_url_fopen (bad, avoid if you can)', default=int(defaults['allow_url_fopen'])),
            var('apc', 'Do you have APC?', default=defaults['apc']),
            var('apc_stat', 'APC: should APC test the file modification (remove it in production)', default=int(defaults['apc_stat'])),
            var('apc_stat_ctime', 'APC: should APC test the file modification ctime also (remove it in production)', default=int(defaults['apc_stat_ctime'])),
            var('apc_num_files_hint', 'APC: How many files in the source code (this is an hint to help APC)', default=int(defaults['apc_num_files_hint'])),
            var('apc_user_entries_hint', 'APC: How many entries in the APC cache (this is an hint to help APC)', default=int(defaults['apc_user_entries_hint'])),
            var('apc_ttl'
              , 'APC: default time to live in cache for apc, read generated conf, setting anything different than 0 may lead to strange things in dev'
              , default=int(defaults['apc_ttl'])),
            var('apc_rfc1867', 'APC: RFC1867 upload progress support in APC', default=int(defaults['apc_rfc1867'])),
            var('apc_shm_size', 'APC: The default shared memory size (32M) is ridiculous but altering it needs altering sysctl.conf', default=int(defaults['apc_shm_size']))
            ]

    def pre(self, command, output_dir, vars):
        """Prepare template generation."""
        super(DrupalPHPFpmTemplate, self).pre(command, output_dir, vars)

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
