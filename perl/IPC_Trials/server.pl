#!/usr/bin/perl

use strict;
use warnings;
use IO::Socket::UNIX;
use JSON;
use Data::Dumper;

my $socket_path = '/tmp/mysocket.sock';

# Create a server socket
my $server = IO::Socket::UNIX->new(
    Local  => $socket_path,
    Type   => SOCK_STREAM,
    Listen => 1,
) or die "Couldn't create server socket: $!";

print "Server is listening on $socket_path\n";

# Accept client connections
while (my $client = $server->accept()) {
    print "Client connected\n";
    
    # Read input from the client
    while (my $input = <$client>) {
        chomp $input;
        my $jsondata = decode_json($input); 

        print "Received from client:" . Dumper($jsondata);
        
        # Process the input as needed
        
        # Send response back to the client
        my $response = {"message"=>"Success","action"=>"send_case","case_name"=>"unit_FPGA/", "req" => $jsondata}; 
        print $client encode_json($response) . "\n";
        print "Sent to client: $response\n";
    }
    
    close $client;
    print "Client disconnected\n";
}

close $server;

