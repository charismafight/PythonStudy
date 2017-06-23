import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        myrow = [0, 0, 4, 0]
        print(max(myrow))
        mytable = [[myrow] * 3]
        self.move_left(myrow, 2)
        self.assertEqual(myrow, [4, 0, 0, 0])
        a = max(map(max, *mytable))
        self.assertEqual(a, 4)
        return

    def move_left(self, row, i):
        if i == 0 or row[i] == 0:
            return
        if row[i - 1] == 0:
            row[i], row[i - 1] = 0, row[i]
            self.move_left(row, i - 1)


if __name__ == '__main__':
    unittest.main()
