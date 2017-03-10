


def reverse(a):
    
    if isinstance(a,str):
        
        newstr=''
        for index in reversed(range(0,len(a))):
    
            newstr= newstr + a[index]
        return newstr
    else:
        raise TypeError
        #print type(type(a).__name__)


print type(reverse('test'))



import unittest

class reverseTest(unittest.TestCase):
    
    def setUp(self):
        self.data='test'
         
    def test_reverse(self):
        verify=[]
        verify.extend(list(reversed('test')))
        print verify
        
        verify=''.join(verify)
        data=self.data
        self.assertEqual(reverse(data),verify)
        #self.assertEqual(True,True,"not match")
    def test_assert_raises(self):
         
         self.assertRaises(TypeError,reverse,123)
        
if __name__ == '__main__':
    unittest.main()
