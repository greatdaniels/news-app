import unittest
from app.models import Sources

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

    def test_check_instance_variables(self):
        '''
        Test case to check if the objects are instansiated correctly
        '''
        self.assertEquals(self.new_source.id, 'abc-news')
        self.assertEquals(self.new_source.name, 'ABC news')
        self.assertEquals(self.new_source.description, 'Your trusted source for breaking news')
        self.assertEquals(self.new_source.url, "https://abcnews.go.com")
        self.assertEquals(self.new_source.category, 'general')
        self.assertEquals(self.new_source.language, 'en')
        self.assertEquals(self.new_source.country, 'us')

