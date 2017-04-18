# ridecell-parking-app

Exercise:

Assume that we are building a parking app for SF city and we need two API's.

Build the following REST APIs. (choose Django or Flask)

1. REST API to list all available parking spots. Input params: {lat, lng, radius}
2. REST API to reserve an available parking spot. input params: { parking_spot, time-range }


Optional:
- test cases for the API's
- view existing reservations
- cancel existing reservations
- extend existing reservations.
- provide multiple return formats (JSON, XML)

APIs:
1.)http://127.0.0.1:8000/spotsavailable/ # get:all available parking spots post:new parking spot requested
2.)http://127.0.0.1:8000/occupiedspots/  # get:all occupied spots in parking post:request for another parking spot
3.)http://127.0.0.1:8000/reservedspots/  # get:all reserved parking spots
4.)http://127.0.0.1:8000/spotsnearby/latitude=100&longitude=100&r=10 # get: all spots near by you 
