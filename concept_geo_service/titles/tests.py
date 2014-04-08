from django.test import TestCase
import json

class TitleResourceTest(TestCase):


    # Polygons URL for test case: https://gist.github.com/anonymous/1abb33df7eae7bdd680b
    def test_contained_by(self):

        rv = self.client.post('/titles-revisions', data=json.dumps({
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

        rv = self.client.get('/titles?partially_contained_by={"type": "Polygon", "coordinates": [[[16.5234375, 15.284185114076445], [2.4609375, 13.239945499286312], [-8.4375, 19.973348786110602], [16.5234375,15.284185114076445]]]}')

        self.assertEqual(json.loads(rv.content), {
                    u"content": {
                        u"title_number": u"AB1234",
                        u"address": u"123 Fake St",
                    u"extent": {
                        u"geometry": {
                        u"type": u"Polygon",
                        u"coordinates": [
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
