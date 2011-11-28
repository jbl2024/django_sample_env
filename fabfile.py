from fabric.api import *
from fabric.utils import puts
from fabric.contrib.files import sed, uncomment, append
env.hosts = ['server.example.com',]
env.user = "sample_project"

WEBSITE_PATH = "sample_project"
GIT_PATH = "forge@git.example.com:sample_project.git")
BRANCH = "master"

def syncdb():
    """Create database or syncdb
    """
    with lcd("%s" % WEBSITE_PATH):
        local('./manage.py syncdb')

def migrate():
    """Migrate database
    """
    with lcd("%s" % WEBSITE_PATH):
        local('./manage.py migrate')

def vtenv_helpers():
    """Uncomment some virtualenv helpers
    """
    with lcd("%s" % WEBSITE_PATH):
        local('sed -i -e "s/# activate_this =/activate_this =/g" manage.py deploy/deploy.wsgi')
        local('sed -i -e "s/# execfile/execfile/g" manage.py deploy/deploy.wsgi')

def local_settings():
    """Add local_settings.py
    """
    import os.path
    if not os.path.exists("%s/local_settings.py" % WEBSITE_PATH):
        puts("File local_settings.py not found : I create it")
        with lcd("%s" % WEBSITE_PATH):
            import random;
            key = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])
            local('echo "SECRET_KEY = \'%s\'" > local_settings.py' % key)

def test():
    """Test application
    """
    with lcd("%s" % WEBSITE_PATH):
        local('./manage.py test')

def collectstatic():
    """Command collect static
    """
    with lcd("%s" % WEBSITE_PATH):
        local('./manage.py collectstatic --noinput')

def update():
    """Update env : syncdb, migrate, collectstatic, test
    """
    syncdb()
    migrate()
    collectstatic()
    test()

def prepare():
    """Prepare django env for first install
    """
    local_settings()
    vtenv_helpers()
    update()

def install():
    """Remote install
    """
    with cd("root"):
        run("git clone %s ." % GIT_PATH)
        if BRANCH != "master":
            run("git branch %s origin/%s" % (GIT_BRANCH, GIT_BRANCH))
        run("git pull -u origin")
        run("./vtenv.sh")
        run("./fab prepare")

def deploy():
    """Update distant django env
    """
    with settings(warn_only=True):
        if run("test -d root/%s" % WEBSITE_PATH).failed:
            with settings(warn_only=False):
                install()
    with cd("root"):
        run("git pull")
        run("./vtenv.sh")
    with cd("root/%s" % WEBSITE_PATH):
        run("./manage.py syncdb")
        run("./manage.py migrate")
        run("./manage.py collectstatic --noinput")
        run("./manage.py test")
        run("touch deploy/deploy.wsgi")

