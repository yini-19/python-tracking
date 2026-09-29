# Sending a message on WhatsApp
"""
Client: WhatsApp
Server: code or system responsible for processing the message and returning feedback and authenticating users
the message carries the method which is a post method, 
and a url path to the user where the message is to be sent, 
Headers: user credentials
body: the message to be sent

the response contains header, body and status code. 
the server sends back a status code, 
and the app decides what to draw on screen because of it
"""
# Balance check
"""
1. the client is the bank app
2. server is the code responsible for verifying user and checking for the balance and  returns the balance
3. the request is a get method, and it carries a url path. it has header and no body
4. the response will contain the status code and the body which is the balance and header 
which contains the user credentials
"""
# A 'create task' request will contain
"""
1. method-describes the action whether a post or get
2. header-describes who is asking
3. url/path-describes which resource
4. Body-is the message
"""

