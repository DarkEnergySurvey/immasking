__author__  = "Felipe Menanteau"
__version__ = '0.2.0'
version = __version__

"""
 The DESDM immask module, masking cosmic ray and streaks on
 single-frame CCDs for now.

$Id$
$Rev::                                  $:  # Revision of last commit.
$LastChangedBy::                        $:  # Author of last commit.
$LastChangedDate::                      $:  # Date of last commit.
"""

from . import immasklib
from .immasklib import DESIMA
from .immasklib import elapsed_time
from .immasklib import cmdline

# Other ways... not really used
# CR masking routine only
#from cr_masking import *

# To load the standalone streak masking routines at startup --- not required
#from . import streak_masking
#from .streak_masking import STREAK
#from .streak_masking import cmdline
print "# Module %s v%s is loaded" % (__name__,__version__)

