from __future__ import print_function, division, absolute_import

from subscription_manager import ga_loader
ga_loader.init_ga()

from . import rhsm_display
rhsm_display.set_display()
