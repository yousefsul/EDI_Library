import os
import unittest


edi_file_path = '../edi_files/client_2731928905_110920211234_GhnyQfieU8W3k_53589.837'


class MyTestCase(unittest.TestCase):
    def test_file_exists(self):
        pass
        # if os.path.exists(edi_file_path):
        #     self.assertEqual(True, True)
        # else:
        #     self.assertEqual(False, True)

    def test_final_result(self):
        pass
        # with open(edi_file_path, 'r') as edi_f:
        #     edi_temp_file = (edi_f.readlines())
        # with open("tmp.837", "w") as new_file:
        #     edi_temp = new_file.write('Hello from the temp file')
        #
        # if edi_temp_file == edi_temp:
        #     self.assertEqual(False, False)
        # if edi_temp_file == edi_temp:
        #     self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
