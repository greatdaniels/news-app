import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):
    '''
    Class to test the behaviour of the articles class
    '''
    def setUp(self):
        self.new_article = Articles('fox.com','Dan', 'Amat victoria kuram', 'consistency is key', 'https://fox.com', 'https://fox.com/images', '2020-10-12T11:31:03Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_check_instance_variables(self):
        self.assertEqual(self.new_article.source, 'fox.com')
        self.assertEquals(self.new_article.author, 'Dan')
        self.assertEquals(self.new_article.title, 'Amat victoria kuram')
        self.assertEquals(self.new_article.description, 'consistency is key')
        self.assertEquals(self.new_article.url, 'https://fox.com')
        self.assertEquals(self.new_article.urlToImage,'https://fox.com/images')
        self.assertEquals(self.new_article.publishedAt, '2020-10-12T11:31:03Z')

