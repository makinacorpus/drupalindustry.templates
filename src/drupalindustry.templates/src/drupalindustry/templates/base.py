#/usr/bin/env/python
#
import ConfigParser
import os.path
from paste.script.templates import Template

_dir, _f = os.path.split(os.path.abspath(__file__))
DEFAULT_CONFIG_FILE = os.path.join(_dir, 'etc', 'defaults.cfg')
BOOLEANS = ['False', 'True', '1', '0']


def getdefaults(section, cfg=DEFAULT_CONFIG_FILE):
    """Get default values for template vars."""
    Config = ConfigParser.ConfigParser()
    Config.read(cfg)
    options = Config.items(section)
    settings = dict(options)

    # setting real bool values in settings
    for option in options:
        if option[1] in BOOLEANS:
            settings[option[0]] = Config.getboolean(section, option[0])
    return settings


class MyTemplate(Template):
    """Base template."""
    use_cheetah = True

    def boolify(self, vars):
        """."""
        unset = ['none', 'false', '0', 'n']
        for key in vars.keys():
            if isinstance(vars[key], basestring):
                if vars[key].lower() in unset:
                    vars[key] = False

    def pre(self, command, output_dir, vars):
        """."""
        self.boolify(vars)

# vim:set et sts=4 ts=4 tw=80:
