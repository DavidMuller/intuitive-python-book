import json
import unittest
from tempfile import NamedTemporaryFile


def write_people_json(people, target_file_path):
    people_json = {"people": people}
    with open(target_file_path, mode="w") as f:
        json.dump(obj=people_json, fp=f)


class TestWritePeopleJSON(unittest.TestCase):
    def test_write_people_json(self):
        with NamedTemporaryFile() as tmp_f:
            write_people_json(
                people=["David", "Adaobi"],
                target_file_path=tmp_f.name,
            )

            expected_json = {"people": ["David", "Adaobi"]}
            actual_json = json.load(fp=tmp_f)
            self.assertEqual(expected_json, actual_json)

if __name__ == '__main__':
    unittest.main()
