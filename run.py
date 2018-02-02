""" Run Yelp Flask App Locally """
# --- core python imports
import os
import sys
# --- core python imports

VENV_ACTIVE = hasattr(sys, 'real_prefix')


def _activate():
    """ Activates virtual environment. """
    if VENV_ACTIVE:
        return None
    # construct virtual environment path.
    this = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(this, 'venv/bin/activate_this.py')

    # check if we can activate the virtual environment at standard location.
    if not os.path.isfile(path):
        print '[ERROR] Seems like you have not activated your virtual environment.'
        print '[ERROR] I tried to load from the standard location, but was not able to find it.'
        print 'Please create a virtual environment at: {0}'.format('{0}/venv'.format(this))
        sys.exit(1)

    # activate the virtual environment.
    execfile(path, dict(__file__=path))


def _run():
    """ Imports the app and runs it. """
    from yelp import app
    app.run(debug=True)


if __name__ == '__main__':
    _activate()
    _run()
