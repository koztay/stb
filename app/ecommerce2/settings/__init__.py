# Aşağıdaki komutlar manage.py içerisinden settings file
# belirlemeye engel oluyor, o nedenle kapattım...

from .base import *

try:
    from .local import *
except:
    pass

try:
    from .new_theme import *
except:
    pass

try:
    from .new_theme_production import *
except:
    pass
