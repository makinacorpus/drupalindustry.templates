########################
drupalindustry.templates
########################

PasteScript templates to generate Drupal layouts and configuration files.

This project uses Python tools to automate some tasks in the Drupal development
and deployment workflow.

************
Installation
************

From source
===========

* Install Python. This software was developed with Python 2.6.
* Get the source:
  ::

    git clone https://github.com/makinacorpus/drupalindustry.templates.git
    cd drupalindustry.templates

* Build package, i.e. install dependencies and configure environment:
  ::

    python bootstrap.py -d
    bin/buildout

* You got paster installed locally (not system-wide) as ./bin/paster

*****
Usage
*****

* Get help about paster:
  ::

    bin/paster --help
    bin/paster --help create

  Remember the following scheme:
  ::

    bin/paster create -t TEMPLATE_NAME -o OUTPUT_BASE_DIRECTORY OUTPUT_PROJECT_NAME

* Get the list of available templates:
  ::

    bin/paster create --list-templates

* Create and configure a Drupal host layout:
  ::

    # Create Drupal host layout
    bin/paster create -t drupal_layout mysite
    
    # Generate Apache2 configuration file
    bin/paster create -t drupal_a2_vhost mysite/etc
    cat mysite/etc/*.conf

    # Generate PHP configuration file
    bin/paster create -t drupal_php_ini mysite/etc/php
    cat mysite/etc/php/php.ini

    # Generate drush makefile for your site in etc/drupal/
    # You'd use it with something like bin/drush make etc/drupal/default.make
    bin/paster create -t drush_site_makefile etc/drupal
    ls etc/drupal
    
    # Optionally, generate buildout configuration file for your project...
    # (yes, Drupal users, I know you are wondering what is this for)
    bin/paster create -t drupal_buildout mysite/buildout
    # ... then use it to download and install drush & drush make
    cd mysite/buildout/
    python bootstrap.py -d
    ../bin/buildout
    cd ..
    bin/drush --version
    bin/drush make --version
    cat bin/drush
    cd ..

* Start a new Drupal module:
  ::

    bin/paster create -t drupal_module -o ~/ mymodule
    ls -al ~/mymodule/
    cat ~/mymodule/mymodule.module
    cat ~/mymodule/mymodule.info

**********
Contribute
**********

Add a new template
==================

* Clone this repository
* Install with buildout
* Add a template class in
  src/drupalindustry/templates/package.py
* Create template files in
  src/drupalindustry/templates/tmpl/.
  One directory per template.
  See Cheetah documentation for the syntax.
* If necessary, add default configuration in
  src/drupalindustry/templates/etc/defaults.cfg.
* Register your new template in entry-points section of
  src/drupalindustry.templates/setup.py
* Update your installation registry:
  ::

    bin/buildout -N -o

* Make sure your new template appears is listed by:
  ::

    bin/paster create --list-templates

* Try your new template.
* Commit your changes.
