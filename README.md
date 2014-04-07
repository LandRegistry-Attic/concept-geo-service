Provides titles for a range of geospatial queries.

/titles?near={"type": "Point","coordinates": [-105.01621,39.57422]}

/titles?contained_by={  "type": "multi_polygon", "coordinates": [[[[30, 20], [45, 40], [10, 40], [30, 20]]], [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],[[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]]}

Example response body:

{

    "title_number" : "SY938123",

    "address": "123 Fake St",

    "postcode": "ABC12 3CD",

    "registered_owners": [

        {

            "name": "A N Other",

            "address": "123 Fake St"

        },

        {

            "name": "B Other",

            "address": "123 Fake St"

        }

    ],

    "lenders": [

        {

            "name": "Acme Bank PLC"

        }

    ],

    "extent" : 

    {

        "type": "multi_polygon", 

        "coordinates": [

            [

                [[30, 20], [45, 40], [10, 40], [30, 20]]

            ], 

            [

                [[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]

            ]

        ]

    }

}



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