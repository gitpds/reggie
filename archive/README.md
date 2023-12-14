PDS.AI ReadMe File and documentations

How does this shit work

This is how this shit works

 Text :

1) Message is sent to +19206774622
2) Twilio receives the message 
    a. Messaging Service Name - gpt3-pdschat
    b. Messaging Service SID -  MGac9cfb62ef8a565570a6d15c2f823e08
3) Twilio Webhook Routes the request
    a. HTTP POST
    b. https://gpt-pdsbot-lhygnhlj3a-uc.a.run.app/textpdsbot
4) Google Cloud Console receives the POST
    a. GCP Project - pdsbot
    b. Billing Account - pdsbillingaccount
5) Request is routed to app.py file
    a. pdsbot.py function imported 
    b. Uses Flask for server backend **FIXME
    c. Calls in openai
    d. 
6) /textpdsbot function called
    a. Invokes the 'ask' function (from pdsbot.py), passes the incoming message and chat_log, and stores the response in the variable 'answer'
    b. Invokes the 'append_interaction_to_chat_log' function (from pdsbot.py), and passes the original incoming message, the answer, and the chat log **FIXME (I think there is a problem here)
7) The function returns the answer to the Twilio function 'MessagingResponse()'
    a. The code currently assigns the MessagingResponse() function to the variable msg before invoking it to pass the answer
8) The '/textpdsbot' function terminates, returning the msg as a string
9) Twilio Receives the answer return message **FIXME
10) Twilio forwards the answer return message **FIXME (I have no idea how these two things happen)








 Voice:
 #FIXME There is also an option for Voice Webhooks

 Worth Noting
 **TODO the '/' endpoint runs the basic Davinci tutorial


 Database:

psql -h 34.69.14.27 -p 5432 -U gptme-db gitpds-db


Build is completing, So I know all my packages are loading properly
Run Builds properly, and so does name my pet, so the issue is in the loop of text message.
Additionally have everything working on CD again

# reggie
