from django.conf import settings
from django.core.files.storage import Storage

class MyStorage(Storage):
	""" Check out what to do here: https://docs.djangoproject.com/en/1.7/howto/custom-file-storage/
	"""
    def __init__(self, option=None):
        if not option:
            option = settings.CUSTOM_STORAGE_OPTIONS
    def _open(self,name, mode='rb'):
    	"""
    	Must be overridden
    	"""
    	pass
    def _save(self,name, content):
    	"""
    	must be overridden
    	"""
    	pass