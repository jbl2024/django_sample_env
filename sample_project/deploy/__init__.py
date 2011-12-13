# REALLY UGLY THING
# =================
from os.path import abspath, dirname, join
deploy = join(abspath(dirname(__file__)), 'deploy.wsgi')
execfile(deploy)
