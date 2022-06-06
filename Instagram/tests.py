from django.test import TestCase
from .models import Post,Profile

# Create your tests here.
class PostTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.self_love= Post(name="joy",id=22,caption="Holla",image="assets/css/images")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.mount_Kenya,Post))
    
    # Testing Save Method
    def test_save_method(self):
        self.self_love.save_post()
        images= Post.objects.all()
        self.assertTrue(len(images) > 0)

    def tearDown(self):
        Post.objects.all().delete()
    
    


class ProfileTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.Brenda= Profile(name="@b_renda",id=22,username="Brenda",date_created="2012-04-23",bio="ppeople nnn")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.ghana,Profile))
    
    # Testing Save Method
    def test_save_method(self):
        self.ghana.save_Location()
        locations= Profile.objects.all()
        self.assertTrue(len(locations) > 0)

    def tearDown(self):
        Profile.objects.all().delete()
        


