# Web_Hosting_service
Simple Web server 
The Simple Web Server and Client project aims to develop a basic web server and client using 
Python programming language. The server will serve static HTML pages to the client on 
request, and the client will be able to make GET and POST requests to the server. Additionally, 
the client will have the option to register new websites with the server, which will be stored in 
a database for future use. The project will utilize Flask web development framework and 
threading to handle multiple requests simultaneously. This report will cover the project's 
methodology, requirements analysis, system design, implementation, testing, and results, and 
provide a conclusion and references used during the development process. 


GET Method: 
The GET method is used to retrieve data from a server. When a client makes a GET request, 
the request URL contains parameters in the form of key-value pairs. The server retrieves 
the requested data and sends it back to the client in the response body. GET requests are 
typically used to retrieve data that does not change frequently, such as web pages, images, 
or documents. 


POST Method: 
The POST method is used to send data to a server to create or update a resource. When a 
client makes a POST request, the request data is sent in the request body. The server 
receives the data and performs the necessary actions to create or update the resource. 
POST requests are typically used to submit data that changes frequently, such as user input 
or form submissions. 


Some key differences between GET and POST methods are: 

Data Encoding: In GET method, data is encoded in the URL, while in POST method, data 
is encoded in the request body. 
Security: GET requests are less secure than POST requests because data is visible in the 
URL, which can be intercepted and modified. POST requests are more secure as data is not 
visible in the URL. 
Caching: GET requests can be cached by web browsers and servers, while POST 
requests cannot be cached. 

In summary, GET requests are used to retrieve data from a server, while POST requests 
are used to send data to a server for creation or update of a resource. Both methods are 
essential in HTTP communication and are widely used in web development. 


Simple Web Server- Our application: 

The GET method will be used to request static HTML pages from the server. For example, 
when a client enters a URL into their web browser, the browser will send a GET request 
to the server for that specific HTML page. The server will then respond with the 
requested HTML page, which will be displayed in the client's web browser. 

The POST method will be used to submit data from the client to the server. For example, 
when a client submits a form on a web page, the data entered into the form will be sent 
to the server using a POST request. The server will then receive the data and store it in a 
database for future retrieval. 

So, in summary, the GET method will be used for retrieving static HTML pages, while 
the POST method will be used for submitting data from the client to the server.
