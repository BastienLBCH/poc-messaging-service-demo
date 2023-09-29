import unittest


def suite():   
    return unittest.TestLoader().discover("appname.unittests_messages", pattern="*.py")