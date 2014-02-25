import os
import logging

logger = logging.getLogger(__name__)

class Verilator:

    def __init__(self):
        self.src_files = []
        self.tb_toplevel = ''
        self.verilator_options = []
        self.libs = []
        self.include_files = []
        self.include_dirs = []
        self.tb_private_src_files = []
        self.tb_include_dirs = []
        self.verilator_options = []
        self.top_module = ''
        self.src_type = 'C'
        self.define_files = []

    def load_items(self, items):
        logger.debug('__init__() *Entered*')
        logger.debug("  items=" + str(items))

        for item in items:
            if item == 'src_files':
                self.src_files = items.get(item).split()
            elif item == 'tb_toplevel':
                self.tb_toplevel = items.get(item)
            elif item == 'top_module':
                self.top_module = items.get(item)
            elif item == 'libs':
                self.libs = items.get(item).split()
            elif item == 'include_files':
                self.include_files = items.get(item).split()
                self.include_dirs  = list(set(map(os.path.dirname, self.include_files)))
            elif item == 'tb_private_src_files':
                self.tb_private_src_files = items.get(item).split()
            elif item == 'tb_include_files':
                self.tb_include_files = items.get(item).split()
                self.tb_include_dirs  = list(set(map(os.path.dirname, self.tb_include_files)))
            elif item == 'verilator_options':
                self.verilator_options = items.get(item).split()
            elif item == 'source_type':
                self.src_type = items.get(item)
            elif item == 'define_files':
                self.define_files = items.get(item).split()
            else:
                print("Warning: Unknown item '" + item +"' in verilator section")
        logger.debug('__init__() -Done-')

    def export(self):
        logger.debug('verilator export() *Entered*')
        self.export_files = self.src_files + self.include_files + self.tb_private_src_files
        if self.tb_toplevel != '':
            self.export_files += [self.tb_toplevel]
        logger.debug("  export_files="+str(self.export_files));
        return self.export_files
