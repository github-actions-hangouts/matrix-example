import unittest, os.path

class TestSum(unittest.TestCase):

    def test_create_file(self):
        with open('test.txt','a') as file:
            file.write("test")		
            file.close()
        self.assertTrue(os.path.exists('Test.txt'))


if __name__ == '__main__':
    unittest.main()