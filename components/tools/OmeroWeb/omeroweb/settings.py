#!/usr/bin/env python
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# #                Django settings for OMERO.web project.               # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 
# 
# Copyright (c) 2008 University of Dundee. 
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# Author: Aleksandra Tarkowska <A(dot)Tarkowska(at)dundee(dot)ac(dot)uk>, 2008.
# 
# Version: 1.0
#

import os.path
import sys
import datetime
import logging
import omero
import omero.clients

# LOGS
# NEVER DEPLOY a site into production with DEBUG turned on.

# Debuging mode. 
# A boolean that turns on/off debug mode.
DEBUG = False # handler404 and handler500 works only when False
TEMPLATE_DEBUG = DEBUG

# Configure logging and set place to store logs.
INTERNAL_IPS = ()
LOGGING_LOG_SQL = False

# LOG path
# Logging levels: logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR logging.CRITICAL
LOGDIR = os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), '../'), '../'), '../'), 'var'), 'log').replace('\\','/')

if DEBUG:  
    LOGDIR = os.path.join(os.path.dirname(__file__), 'log').replace('\\','/')  
    LOGFILE = ('OMEROweb-dev.log')
    LOGLEVEL = logging.DEBUG
else:
    LOGFILE = ('OMEROweb.log')
    LOGLEVEL = logging.INFO
    
if not os.path.isdir(LOGDIR):
    try:
        os.mkdir(LOGDIR)
    except Exception, x:
        exctype, value = sys.exc_info()[:2]
        raise exctype, value

import logconfig
logger = logconfig.get_logger(os.path.join(LOGDIR, LOGFILE), LOGLEVEL)

# Database settings
DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'db.sqlite3'   # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Test database name
TEST_DATABASE_NAME = 'test-db.sqlite3'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/appmedia/omeroweb/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'
FIRST_DAY_OF_WEEK = 0     # 0-Monday, ... 6-Sunday

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/appmedia/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_appmedia/omeroweb/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@@k%g#7=%4b6ib7yr1tloma&g0s2nni6ljf!m0h&x9c712c7yj'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'djangologging.middleware.LoggingMiddleware',
)

ROOT_URLCONF = 'omeroweb.urls'

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (
    os.path.join(os.path.join(os.path.dirname(__file__), 'feedback'), 'templates').replace('\\','/'),
    os.path.join(os.path.join(os.path.dirname(__file__), 'webadmin'), 'templates').replace('\\','/'),
    os.path.join(os.path.join(os.path.dirname(__file__), 'webclient'), 'templates').replace('\\','/'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'omeroweb.feedback',
    'omeroweb.webadmin',
    'omeroweb.webclient',
    'omeroweb.webgateway',
    'omeroweb.webtest',
)

FEEDBACK_URL = "qa.openmicroscopy.org.uk:80"

IGNORABLE_404_ENDS = ('*.ico')

# Cache
CACHE_BACKEND = 'file:///var/tmp/django_cache'
CACHE_TIMEOUT = 86400

# Cookies config
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # False
SESSION_COOKIE_AGE = 86400 # 1 day in sec (86400)

# file upload settings
FILE_UPLOAD_TEMP_DIR = '/tmp'
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440 #default 2621440

DEFAULT_IMG = os.path.join(os.path.dirname(__file__), 'media', 'omeroweb', "images", 'image128.png').replace('\\','/')
DEFAULT_USER = os.path.join(os.path.dirname(__file__), 'media', 'omeroweb', "images", 'personal32.png').replace('\\','/')

# CUSTOM CONFIG
try:
    import custom_settings
except ImportError:
    sys.stderr.write("Error: Can't find the file 'custom_settings.py' in the directory containing %r." \
        "It appears you've customized things.\nYou'll have to run 'bin/omero web [settings|superuser|syncdb]', " \
        "passing it your settings module.\n(If the file custom_settings.py does indeed exist, " \
        "it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

try:
    ADMINS = custom_settings.ADMINS
except:
    pass
try:
    EMAIL_HOST = custom_settings.EMAIL_HOST
except:
    pass
try:
    EMAIL_HOST_PASSWORD = custom_settings.EMAIL_HOST_PASSWORD
except:
    pass
try:
    EMAIL_HOST_USER = custom_settings.EMAIL_HOST_USER
except:
    pass
try:
    EMAIL_PORT = custom_settings.EMAIL_PORT
except:
    pass
try:
    EMAIL_SUBJECT_PREFIX = custom_settings.EMAIL_SUBJECT_PREFIX
except:
    pass
try:
    EMAIL_USE_TLS = custom_settings.EMAIL_USE_TLS
except:
    pass
try:
    SERVER_EMAIL = custom_settings.SERVER_EMAIL
except:
    pass

SEND_BROKEN_LINK_EMAILS = True
EMAIL_SUBJECT_PREFIX = '[OMERO.web] '

# APPLICATIONS CONFIG
try:
    if custom_settings.APPLICATION_HOST.endswith("/"):
        APPLICATION_HOST=custom_settings.APPLICATION_HOST
    else:
        APPLICATION_HOST=custom_settings.APPLICATION_HOST+"/"
except:
    logger.error("custom_settings.py has not been configured. APPLICATION_HOST is not set.\n" ) 
    sys.stderr.write("custom_settings.py has not been configured. APPLICATION_HOST is not set.\n")
    sys.exit(1)
