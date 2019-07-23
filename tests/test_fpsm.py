import unittest
import fpsm


class TestFpsm(unittest.TestCase):
    l1 = [1, 2, 3, 4, 5]
    l2 = range(2, 11)
    l3 = 'hello world'

    def test_head(self):
        self.assertEqual(fpsm.head(self.l1), 1)
        self.assertEqual(fpsm.head(self.l2), 2)
        self.assertEqual(fpsm.head(self.l3), 'h')

    def test_tail(self):
        self.assertEqual(fpsm.tail(self.l1), [2, 3, 4, 5])
        self.assertEqual(fpsm.tail(self.l2), list(range(3, 11)))
        self.assertEqual(fpsm.tail(self.l3), 'ello world')

    def test_init(self):
        self.assertEqual(fpsm.init(self.l1), [1, 2, 3, 4])
        self.assertEqual(fpsm.init(self.l2), list(range(2, 10)))
        self.assertEqual(fpsm.init(self.l3), 'hello worl')

    def test_last(self):
        self.assertEqual(fpsm.last(self.l1), 5)
        self.assertEqual(fpsm.last(self.l2), 10)
        self.assertEqual(fpsm.last(self.l3), 'd')

    def test_take(self):
        self.assertEqual(fpsm.take(3, self.l1), [1, 2, 3])
        self.assertEqual(fpsm.take(2, self.l2), [2, 3])
        self.assertEqual(fpsm.take(4, self.l3), 'hell')

    def test_null(self):
        self.assertEqual(fpsm.null([]), True)
        self.assertEqual(fpsm.null(range(10)), False)

    def test_foldl(self):
        self.assertEqual(fpsm.foldl(lambda x, y: 2 * x + y, [1, 1, 0]), 6)

    def test_foldr(self):
        self.assertEqual(fpsm.foldr(lambda x, y: x + y * 2, [1, 0, 1]), 5)

    def test_concat(self):
        self.assertEqual(fpsm.concat([[1,2,3], [4,5,6]]), list(range(1, 7)))

    def test_concat_map(self):
        self.assertEqual(fpsm.concat_map(lambda x: [0, x], [[1,2,3,4,5,6]]), [0,1,0,2,0,3,0,4,0,5,0,6])


if __name__ == '__main__':
    unittest.main()
