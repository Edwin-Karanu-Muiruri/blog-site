import unittest
from app.models import Comment, User
from app import db

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'Edwin',password = 'password', email = 'edwin@mail.com')
        self.new_comment = Comment(blog_id=10101,title='comment',comment='This comment is a test',user = self.user_Edwin)


    def tearDown(self):
            Comment.query.delete()
            User.query.delete()

    def test_check_instance_variables(self):
            self.assertEquals(self.new_comment.blog_id,10101)
            self.assertEquals(self.new_comment.title,'comment')
            self.assertEquals(self.new_comment.comment,'This comment is a test')
            self.assertEquals(self.new_comment.user,self.user_Edwin)

    def test_save_comment(self):
            self.new_comment.save_comment()
            self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

            self.new_comment.save_comment()
            got_comments = comment.get_comments(10101)
            self.assertTrue(len(got_comments) == 1)