# /titles

###Description
Returns titles for a range of geospatial queries

###Supported methods
GET

###Supported queries 

near - Request titles near a EPSG 4326 point.

partially_contained_by - Request titles contained or partially contained by EPSG 3857 polygon.

###Examples queries

/titles?near={"type": "Point","coordinates": [15.46, 60.9], "crs": {"type": "name","properties": {"name": "EPSG:4326"}}}

/titles?partially_contained_by={"type": "Polygon", "coordinates": [[[16.5234375, 15.284185114076445], [2.4609375, 13.239945499286312], [-8.4375, 19.973348786110602], [16.5234375,15.284185114076445]]], "crs": {"type": "name","properties": {"name": "EPSG:3857"}}}}

###Example response body

{

    "objects": [
        {
            "extent": {
                "geometry": {
                    "type": "MultiPolygon",
                    "crs": {
                        "properties": {
                            "name": "EPSG:3857"
                        },
                        "type": "name"
                    },
                    "coordinates": [
                        [
                            [
                                [
                                    14740.209100515895,
                                    6761524.311508592
                                ],
                                [
                                    14740.164439320028,
                                    6761527.75965114
                                ],
                                [
                                    14740.140413774692,
                                    6761529.702233995
                                ],
                                [
                                    14740.066988447501,
                                    6761541.015837337
                                ],
                                [
                                    14739.97283985011,
                                    6761554.385224775
                                ],
                                [
                                    14750.692924338135,
                                    6761554.475385822
                                ],
                                [
                                    14750.884760340481,
                                    6761541.135497569
                                ],
                                [
                                    14751.042579192252,
                                    6761529.948877224
                                ],
                                [
                                    14751.057166881106,
                                    6761527.682924696
                                ],
                                [
                                    14751.07576216814,
                                    6761524.669232471
                                ],
                                [
                                    14749.677381298276,
                                    6761524.64875213
                                ],
                                [
                                    14740.209100515895,
                                    6761524.311508592
                                ]
                            ]
                        ]
                    ]
                }
            },
            "address": "172 Jocelyns, Harlow (CM17 0BZ)",
            "registered_owners": [
                {
                    "address": "172 Jocelyns, Harlow (CM17 0BZ)",
                    "name": "Mmu Ltd"
                }
            ]
        }
    ]
}

###Example client
[This](https://github.com/LandRegistry/concept-my-property/blob/master/static/javascripts/map-lasso-search.js) example allows the user to draw a polygon on a map and displays the set of titles contained within the polygon.


# /titles-revisions

###Description
Accepts Land Registry title revisions

###Methods supported
POST

###Example

POST /titles-revisions 

{

    "content": {

        "title_number": "AB1234",

        "address": "123 Fake St",

        "extent": {

            "geometry": {

                "type": "MultiPolygon",

                "coordinates": [
                    [
                        [
                            [
                                14708.755563011973,
                                6761018.225448865
                            ]
                        ]
                    ]
                ]
            }
        }
    }
}
