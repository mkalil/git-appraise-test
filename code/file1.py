import os.path

from jupyter_server.config_manager import BaseJSONConfigManager, recursive_update
from jupyter_core.paths import jupyter_config_dir, jupyter_config_path
from traitlets import Unicode, Instance, List, observe, default
from traitlets.config import LoggingConfigurable


class ConfigManager(LoggingConfigurable):
    """Config Manager used for storing notebook frontend config"""

    # Public API

    def get(self, section_name):
        """Get the config from all config sections."""
        config = {}
        # step through back to front, to ensure front of the list is top priority
        for p in self.read_config_path[::-1]:
            cm = BaseJSONConfigManager(config_dir=p)
            recursive_update(config, cm.get(section_name))
        return config

    def set(self, section_name, data):
        """Set the config only to the user's config."""
        return self.write_config_manager.set(section_name, data)

    def update(self, section_name, new_data):
        """Update the config only to the user's config."""
        return self.write_config_manager.update(section_name, new_data)

    # Private API

    read_config_path = List(Unicode())

    @default('read_config_path')
    def _default_read_config_path(self):
        return [os.path.join(p, 'labconfig') for p in jupyter_config_path()]

    write_config_dir = Unicode()

    @default('write_config_dir')
    def _default_write_config_dir(self):
        return os.path.join(jupyter_config_dir(), 'labconfig')

