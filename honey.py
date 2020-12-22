from twilio.rest import Client 
 
account_sid = 'AC8ef4ae3ca55f0d9c4d15115f83bb570b' 
auth_token = '05258cec3c217a808b7b26fae83d443f' 
client = Client(account_sid, auth_token) 
def send_l():

    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Your appointment is coming up on July 21 at 3PM',      
                                to='whatsapp:+917002106145' 
                            ) 
    
    print(message.sid)