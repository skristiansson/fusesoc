fusesoc_PYTHON =        \
 fusesoc/__init__.py           \
 fusesoc/config.py             \
 fusesoc/core.py               \
 fusesoc/coremanager.py        \
 fusesoc/fusesocconfigparser.py \
 fusesoc/plusargs.py           \
 fusesoc/system.py             \
 fusesoc/utils.py              \
 fusesoc/verilog.py            \
 fusesoc/vpi.py

fusesocdir = $(pkgpythondir)

provider_PYTHON =      \
 fusesoc/provider/__init__.py  \
 fusesoc/provider/github.py    \
 fusesoc/provider/opencores.py \
 fusesoc/provider/url.py

providerdir = $(fusesocdir)/provider

section_PYTHON = \
 fusesoc/section/__init__.py

sectiondir = $(fusesocdir)/section

simulator_PYTHON =      \
 fusesoc/simulator/__init__.py  \
 fusesoc/simulator/icarus.py    \
 fusesoc/simulator/modelsim.py  \
 fusesoc/simulator/simulator.py \
 fusesoc/simulator/verilator.py

simulatordir = $(fusesocdir)/simulator


build_PYTHON =      \
 fusesoc/build/__init__.py  \
 fusesoc/build/backend.py    \
 fusesoc/build/quartus.py    \
 fusesoc/build/ise.py

builddir = $(fusesocdir)/build

EXTRA_DIST = INSTALL

SUBDIRS = bin
