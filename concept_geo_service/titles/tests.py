from django.test import TestCase
import json
from pyproj import Proj, transform

class TitleResourceTest(TestCase):


    # Polygons URL for test case: https://gist.github.com/anonymous/1abb33df7eae7bdd680b
    def test_contained_by(self):
        self.maxDiff = None
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

        self.assertEqual(rv.status_code, 201)

        rv = self.client.post('/titles-revisions', data=json.dumps({
        "content": {
            "title_number": "AB1235",
            "address": "123 Russia St",
            "extent": {
                "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      102.65625,
                      68.65655498475735
                    ],
                    [
                      112.5,
                      67.06743335108298
                    ],
                    [
                      114.60937499999999,
                      70.61261423801925
                    ],
                    [
                      102.65625,
                      68.65655498475735
                    ]
                  ]
                ]
            }
                }
            }
        }), content_type='application/json')
        self.assertEqual(rv.status_code, 201)

        rv = self.client.get('/titles?partially_contained_by={"type": "Polygon", "coordinates": [[[16.5234375, 15.284185114076445], [2.4609375, 13.239945499286312], [-8.4375, 19.973348786110602], [16.5234375,15.284185114076445]]]}')

        self.assertEqual(json.loads(rv.content), {
                    u"objects": [{
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
                    }]
                })


    def test_near(self):
        self.maxDiff = None
        rv = self.client.post('/titles-revisions', data=json.dumps({
        "content": {
            "title_number": "AB1234",
            "address": "123 Fake St",
              "extent": {
                  "geometry": {
                    "coordinates": [
                      [
                        [
                          [
                            11218.952964794893, 
                            6757320.556413552
                          ], 
                          [
                            11226.959779705123, 
                            6757360.598292298
                          ], 
                          [
                            11230.39621140335, 
                            6757377.785815356
                          ], 
                          [
                            11260.151974394212, 
                            6757372.158190851
                          ], 
                          [
                            11258.063094737634, 
                            6757362.287694273
                          ], 
                          [
                            11248.84782684651, 
                            6757318.709544176
                          ], 
                          [
                            11248.840357580635, 
                            6757318.674177335
                          ], 
                          [
                            11248.42265991821, 
                            6757318.734764772
                          ], 
                          [
                            11230.466359233886, 
                            6757319.8195211645
                          ], 
                          [
                            11218.952964794893, 
                            6757320.556413552
                          ]
                        ]
                      ]
                    ], 
                    "crs": {
                      "properties": {
                        "name": "EPSG:3857"
                      }, 
                      "type": "name"
                    }, 
                    "type": "MultiPolygon"
                  }
                }
            }
        }), content_type='application/json')

        rv = self.client.post('/titles-revisions', data=json.dumps({
        "content": {
            "title_number": "AB1235",
            "address": "123 Russia St",
            "extent": {
                "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      102.65625,
                      68.65655498475735
                    ],
                    [
                      112.5,
                      67.06743335108298
                    ],
                    [
                      114.60937499999999,
                      70.61261423801925
                    ],
                    [
                      102.65625,
                      68.65655498475735
                    ]
                  ]
                ]
            }
                }
            }
        }), content_type='application/json')

        inProj = Proj(init='epsg:3857')
        outProj = Proj(init='epsg:4326')
        x1,y1 =  11218.952964794893, 6757320.556413552
        x2,y2 = transform(inProj,outProj,x1,y1)
        url = '/titles?near={"type": "Point","coordinates": [%s,%s], "crs": {"type": "name","properties": {"name": "EPSG:4326"}}}' % (x2,y2)
        rv = self.client.get( url )
        self.assertEqual(json.loads(rv.content), {
                    u"objects": [{
                        u"title_number": u"AB1234",
                        u"address": u"123 Fake St",
                       u"extent": {
                          u"geometry": {
                            u"coordinates": [
                              [
                                [
                                  [
                                    11218.952964794893, 
                                    6757320.556413552
                                  ], 
                                  [
                                    11226.959779705123, 
                                    6757360.598292298
                                  ], 
                                  [
                                    11230.39621140335, 
                                    6757377.785815356
                                  ], 
                                  [
                                    11260.151974394212, 
                                    6757372.158190851
                                  ], 
                                  [
                                    11258.063094737634, 
                                    6757362.287694273
                                  ], 
                                  [
                                    11248.84782684651, 
                                    6757318.709544176
                                  ], 
                                  [
                                    11248.840357580635, 
                                    6757318.674177335
                                  ], 
                                  [
                                    11248.42265991821, 
                                    6757318.734764772
                                  ], 
                                  [
                                    11230.466359233886, 
                                    6757319.8195211645
                                  ], 
                                  [
                                    11218.952964794893, 
                                    6757320.556413552
                                  ]
                                ]
                              ]
                            ], 
                            u"crs": {
                              u"properties": {
                                u"name": u"EPSG:3857"
                              }, 
                              u"type": u"name"
                            }, 
                            u"type": u"MultiPolygon"
                          }
                        }
                    }]
                })




    def test_not_near(self):
        self.maxDiff = None
        
        rv = self.client.post('/titles-revisions', data=json.dumps({
        "content": {
            "title_number": "AB1234",
            "address": "123 Fake St",
              "extent": {
                  "geometry": {
                    "coordinates": [
                      [
                        [
                          [
                            11218.952964794893, 
                            6757320.556413552
                          ], 
                          [
                            11226.959779705123, 
                            6757360.598292298
                          ], 
                          [
                            11230.39621140335, 
                            6757377.785815356
                          ], 
                          [
                            11260.151974394212, 
                            6757372.158190851
                          ], 
                          [
                            11258.063094737634, 
                            6757362.287694273
                          ], 
                          [
                            11248.84782684651, 
                            6757318.709544176
                          ], 
                          [
                            11248.840357580635, 
                            6757318.674177335
                          ], 
                          [
                            11248.42265991821, 
                            6757318.734764772
                          ], 
                          [
                            11230.466359233886, 
                            6757319.8195211645
                          ], 
                          [
                            11218.952964794893, 
                            6757320.556413552
                          ]
                        ]
                      ]
                    ], 
                    "crs": {
                      "properties": {
                        "name": "EPSG:3857"
                      }, 
                      "type": "name"
                    }, 
                    "type": "MultiPolygon"
                  }
                }
            }
        }), content_type='application/json')

 

        #Norway
        rv = self.client.get('/titles?near={"type": "Point","coordinates": [15.46, 60.9], "crs": {"type": "name","properties": {"name": "EPSG:4326"}}}')
        self.assertEqual(json.loads(rv.content), {
                    u"objects": []
                })
