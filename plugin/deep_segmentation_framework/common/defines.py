import os

PLUGIN_NAME = 'DeepSegmentationFramework'
LOG_TAB_NAME = PLUGIN_NAME


# enable some debugging options (e.g. printing exceptions) - set in terminal before running qgis
IS_DEBUG = os.getenv("IS_DEBUG", 'False').lower() in ('true', '1', 't')
