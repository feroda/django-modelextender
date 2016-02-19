# Copyright: Luca Ferroni 2011
# Author: Luca Ferroni <luca@befair.it>
# License: GNU Affero General Public License, version 3

# This file is released as part of the django-modelextender repo
# at https://github.com/feroda/django-modelextender/


class ModelExtender(object):
    """
    Utility class to be inherited to extend a Django model.

    Extension is done with object attrs that starts by prefix
    whose name is defined in the __class__.ext_prefix attr
    """

    ext_prefix = "_ext_"

    def add_method_to_class(self, cls, method_name):
        """Add method to the Django model (cls).

        Original method, if present, is saved in self._orig_+ 'method_name'
        """

        # print("Aggiungo il metodo %s" % method_name)
        setattr(self, '_orig_' + method_name, getattr(cls, method_name, None))

        meth = getattr(self.__class__, method_name)
        try:
            func = meth.__func__
        except AttributeError:
            func = meth

        l = len(self.__class__.ext_prefix)
        orig_method_name = method_name[l:]
        setattr(cls, orig_method_name, func)

    def contribute_to_class(self, cls, name):
        """Check methods to be added and invoke the add method."""

        for method_name in dir(self):
            if method_name.startswith(self.__class__.ext_prefix):
                self.add_method_to_class(cls, method_name)
