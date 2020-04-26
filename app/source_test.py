import unittest
from .models import sources
Sources = sources.Sources

class SourceTest(unittest.TestCase):
    '''
    to test behavior of Source class
    '''
    def setUp(self):
        '''
        setUo method runs before each test
        '''
        self.new_source = Sources('abc-news','ABC news','Your trusted source for breaking news',"https://abcnews.go.com","general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

if __name__ == '__main__':
    unittest.main()