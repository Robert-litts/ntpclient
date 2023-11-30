from socket import AF_INET, SOCK_DGRAM # For setting up the UDP packet.
import sys
import socket
import struct, time # To unpack the packet sent back and to convert the seconds to a string.

host = "time-a-g.nist.gov"; # The server.
port = 123; # Port.
read_buffer = 1024; # The size of the buffer to read in the received UDP packet.
address = ( host, port ); # Tuple needed by sendto.
data = '\x1b' + 47 * '\0' #48 Byte Message: First byte, 0x1B = Leap Indicator (0), Version Number (3), Mode (3) (00 011 011); 47 remaining null bytes
data_encoded = data.encode("utf-8")

epoch = 2208988800; # Time in seconds for UNIX Epoch Jan, 1970 - 00:00h (UTC) - 1/1/1900- 00:00h.
#(70*365 + 17)*86400 = 2208988800 --> Accounts for 70 years, 365 days per year, 17 leap years, 86,400 seconds/day
#https://www.rfc-editor.org/rfc/rfc868

client = socket.socket( AF_INET, SOCK_DGRAM ); # Internet, UDP

client.sendto(data_encoded, address)

data_encoded, address = client.recvfrom( read_buffer ); # Get the response and put it in data and put the send socket address into address.

t = struct.unpack( "!12I", data_encoded )[ 10 ]; # Unpack the binary data and get the seconds out.

t -= epoch; # Calculate seconds since the epoch.

print("Time = %s" % time.ctime( t )); # Print the seconds as a formatted string.


#** Updated by Robert Litts for Python 3, 2023 **

'''

(C) 2014 David Lettier.

http://www.lettier.com/

NTP client.

'''
