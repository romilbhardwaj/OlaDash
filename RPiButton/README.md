This is the geekier alternative to the Amazon Dash - hook up a push switch to RPi GPIO and use that as a trigger to a HTTP endpoint.
Make sure to setup your OlaDash server first and configure the server address in WebButton.py Add WebButton.py to run at startup by adding this line to your /etc/rc.local

(sleep 5;python <Address to WebButton.py>)&

Dependencies - RPi.GPIO and urllib2.