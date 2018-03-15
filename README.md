# PhoneClient

Clicking a tel: link in an application such as Firefox can start a pop-up window with these elements in the GUI: the phone number to be called, a "Call" button that places a phone call, details about the country in which the phone number is registered and another button to save the number to an address book. 
The application is to be developed as a standalone Python script which will be invoked as a MIME handler. 
The script will not need to understand how to dial the phone calls: when somebody clicks the "Call" button, the script can run another script such as sipdial in reSIProcate.
