from fusesoc.provider import Provider
from fusesoc.utils import pr_info, pr_warn
import subprocess
import os.path
import sys
import tarfile
import zipfile
import shutil
import logging

logger = logging.getLogger(__name__)

if sys.version_info[0] >= 3:
    import urllib.request as urllib
else:
    import urllib

class ProviderURL(Provider):
    def __init__(self, config):
        logger.debug('__init__() *Entered*')
        self.url      = config.get('url')
        self.filetype = config.get('filetype')
        if 'corename' in config:
            self.version = config.get('corename')
        else:
            self.version = '----'
        logger.debug('__init__() -Done-')

    def fetch(self, local_dir, core_name):
        logger.debug('fetch() *Entered*')
        status = self.status(local_dir)
        if '----' in self.version:
            self.corename = core_name
        else:
            self.corename = self.version

        if status == 'empty':
            try:
                self._checkout(local_dir, self.corename)
                return True
            except RuntimeError:
                raise
        elif status == 'modified':
            self.clean_cache()
            try:
                self._checkout(local_dir, self.corename)
                return True
            except RuntimeError:
                raise
        elif status == 'outofdate':
            self._update()
            return True
        elif status == 'downloaded':
            return False
        else:
            pr_warn("Provider status is: '" + status + "'. This shouldn't happen")
            return False

    def _checkout(self, local_dir, core_name):
        logger.debug('_checkout() *Entered*')
        pr_info("Checking out " + self.url + " to " + local_dir)
        (filename, headers) = urllib.urlretrieve(self.url)
        (cache_root, core) = os.path.split(local_dir)

        if self.filetype == 'tar':
            t = tarfile.open(filename)
            t.extractall(os.path.join(cache_root, core_name))
        elif self.filetype == 'zip':
            with zipfile.ZipFile(filename, "r") as z:
                z.extractall(os.path.join(cache_root, core_name))
        elif self.filetype == 'simple':
            # Splits the string at the last occurrence of sep, and
            # returns a 3-tuple containing the part before the separator,
            # the separator itself, and the part after the separator.
            # If the separator is not found, return a 3-tuple containing
            # two empty strings, followed by the string itself
            segments = self.url.rpartition('/')
            self.path = os.path.join(cache_root, core_name)
            os.makedirs(self.path)
            self.path = os.path.join(self.path, segments[2])
            shutil.copy2(filename, self.path)
        else:
            raise RuntimeError("Unknown file type '" + self.filetype + "' in [provider] section")

        logger.debug('_checkout() -Done-')

    def status(self, local_dir):
        logger.debug('status() *Entered*')
        if not os.path.isdir(local_dir):
            return 'empty'
        else:
            return 'downloaded'
