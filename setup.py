from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='drupalindustry.templates',
      version=version,
      description="Templates to deploy a Drupal project",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords="pastescript templates to deploy Drupal's project",
      author='Jean-Philippe Camguilhem',
      author_email='jpc_at_makina-corpus.com',
      url='https://github.com/makinacorpus/drupalindustry.templates',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages=['drupalindustry'],
      include_package_data=True,
      #data_files = [('drupalindustry/templates/etc', ['src/drupalindustry/templates/etc/defaults.cfg'])],
      zip_safe=False,
      install_requires=['setuptools', 'PasteScript', 'Cheetah'],
      entry_points=""" # -*- Entry points: -*-
      [paste.paster_create_template]
      drupal_buildout_bootstrap = drupalindustry.templates.package:DrupalBuildoutBootstrapTemplate
      drupal_buildout = drupalindustry.templates.package:DrupalBuildoutTemplate
      drupal_module = drupalindustry.templates.package:DrupalModuleTemplate
      drupal_layout = drupalindustry.templates.package:DrupalLayoutTemplate
      drupal_a2_vhost = drupalindustry.templates.package:DrupalApache2VhostTemplate
      drupal_nginx_vhost = drupalindustry.templates.package:DrupalNginxVhostTemplate
      drupal_php_ini = drupalindustry.templates.package:DrupalPHPIniTemplate
      drush_site_makefile = drupalindustry.templates.package:DrushSiteMakefileTemplate
      drupal_site_docs = drupalindustry.templates.package:DrupalSiteDocumentationTemplate
      """,
      )
