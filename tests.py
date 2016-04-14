import unittest

import kiseru
from kiseru import ArgumentError


class ClassTest(unittest.TestCase):
    def _makeOne(self, func):
        return kiseru.Kiseru(func)

    def test_ok(self):
        doggy = self._makeOne(lambda: 'inu is dog')
        split = self._makeOne(lambda x: x.split())
        capitalize = self._makeOne(lambda x: [i[0].upper() + i[1:] for i in x])
        join = self._makeOne(lambda x: ' '.join(x))

        self.assertEqual(doggy() | split | capitalize | join, 'Inu Is Dog')

    def test_fail_with_not_callable_argument(self):
        with self.assertRaises(ArgumentError):
            self._makeOne('str')


class DecoratorTest(unittest.TestCase):
    def _callFUT(self):
        return kiseru.kiseru

    def test_ok(self):
        @self._callFUT()
        def kitten():
            return 'neko is cat'

        @self._callFUT()
        def kebab(x):
            return '-'.join(x.split())

        @self._callFUT()
        def does_cat_hide(x):
            return 'cat' in x
        self.assertTrue(kitten() | kebab | does_cat_hide)


if __name__ == '__main__':
    unittest.main()
