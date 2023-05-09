#!/usr/bin/perl

use strict;
use warnings;
use IO::Socket::UNIX;

my $socket_path = '/tmp/mysocket.sock';

# Connect to the server socket
my $socket = IO::Socket::UNIX->new(
    Peer => $socket_path,
    Type => SOCK_STREAM,
) or die "Couldn't connect to server socket: $!";

# Send input to the server
my @inputs = ("Hello", "World", "quit");
foreach my $input (@inputs) {
    print $socket "$input\n";
    print "Sent to server: $input\n";
    
    # Read response from the server
    my $response = <$socket>;
    chomp $response;
    print "Received from server: $response\n";
    sleep 1; 
    last if $input eq 'quit';  # Terminate the client if 'quit' is sent
}

close $socket;

