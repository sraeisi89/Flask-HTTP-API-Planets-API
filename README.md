Planets API
Create a HTTP API using Flask that returns JSON data about planets. Planets can be looked
up by name.

Endpoints

GET /planets/<name>
Returns the volume and the mass of the planet in human readable format, and the number of
its moons. It should return 404 Not Found status code if such planet does not exist.
Example request
curl http://localhost:5000/planets/Neptune
  
Example response
{
"mass": "1.02413 * 10^26 kg",
"volume": "6.254 * 10^13 km3",
"moons": 14
}
  
GET /usage
Renders a HTML page that shows how many times each planet has been queried since the
server started running.

Example output
• Earth: looked up 3 times
• Jupiter: looked up 2 times
• Neptune: looked up 5 times
  
In the implementation of the endpoints you should use other 3rd party APIs to retrieve data.
Use the following API: https://api.le-systeme-solaire.net/en/
