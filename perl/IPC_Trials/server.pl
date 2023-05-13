#!/usr/bin/perl

use strict;
use warnings;
use IO::Socket::UNIX;

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
        print "Received from client: $input\n";
        
        # Process the input as needed
        
        # Send response back to the client
        my $response = "Server response for: $input\n";
        print $client $response;
        print "Sent to client: $response\n";
    }
    
    close $client;
    print "Client disconnected\n";
}

close $server;

