use strict;
use warnings;
use IO::Socket::UNIX;
use JSON;
use Data::Dumper;

my $socket_path = '/tmp/mysocket.sock';
my $client = IO::Socket::UNIX->new(
    Type => SOCK_STREAM,
    Peer => $socket_path
) or die "Failed to create client socket: $!";


for my $idx (1..10){
  my $data = { action => "name", idx => $idx };
  my $json_data = encode_json($data);

  print $client "$json_data\n";
  
  #shutdown($client, 1);    # incase SEND DATA SOCKET to be CLOSED and RECEIVE to remain OPEN
  print "CLIENT SEND idx:$idx\n";  
  my $resp = read_socket($client);
  print "RESPONSE: " . Dumper($resp); 
  sleep 1; 
} 

sub read_socket(){
   my $socket  = shift;  
   while (my $response = <$socket> ) {
      chomp $response;
      my $res = decode_json($response);
      return $res;
  }

}



close $client;

