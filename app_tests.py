
import os
import app
import unittest
import tempfile
import json

class GeoServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    # Polygons URL for test case: https://gist.github.com/anonymous/1abb33df7eae7bdd680b
    def test_contained_by(self):
        rv = self.app.post('/titles-revisions', data=json.dumps({
        "content": {
            "title_number": "AB1234",
            "address": "123 Fake St",
            "extent": {
                "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            1.0546875,
                            16.720385051694
                        ],
                        [
                            3.076171875,
                            16.214674588248542
                        ],
                        [
                            2.373046875,
                            15.029685756555674
                        ],
                        [
                            1.0546875,
                            16.720385051694
                        ]
                    ]
                ]
            }
                }
            }
        }), content_type='application/json')

        rv = self.app.get('/titles?partially_contained_by={ type": "Polygon", "coordinates": [[[16.5234375, 15.284185114076445], [2.4609375, 13.239945499286312], [-8.4375, 19.973348786110602], [              16.5234375,15.284185114076445]          ]]      }')                         

        self.assertEqual(json.loads(rv.data), {
                    "content": {                    
                        "title_number": "AB1234",
                        "address": "123 Fake St",
                    "extent": {
                        "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    1.0546875,
                                    16.720385051694
                                ],
                                [
                                    3.076171875,
                                    16.214674588248542
                                ],
                                [
                                    2.373046875,
                                    15.029685756555674
                                ],
                                [
                                    1.0546875,
                                    16.720385051694
                                ]
                            ]
                        ]
                    }
                        }
                    }
                })





 

if __name__ == '__main__':
    unittest.main()        