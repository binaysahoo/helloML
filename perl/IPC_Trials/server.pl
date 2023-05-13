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
my $testid = 0; 
# Accept client connections
while (my $client = $server->accept()) {
    print "Client connected\n";
    
    # Read input from the client
    while (my $input = <$client>) {
        chomp $input;
        my $jsondata = decode_json($input); 
        print "Received from client:" . Dumper($jsondata);
        # Process the input as needed
        my $action = $jsondata->{action} // 'testdone';  
        #========================================================================================== 
        # request from client         | response to client
        #------------------------------------------------------------------------------------------
        # { action => "gettest" } | respose: { testcase => "name|NA","status" => "OK" } 
        # { action => "testinfo", pid => 123, rundir => "rundirname", runoption => "" , runlog => "" }   | response { "status => "OK" }
        # { action => "testdone" } | respose: { "status" => "OK" } 
        #========================================================================================== 
        # Send response back to the client
        my $response = { "status" => "OK"}; 
        if ($action =~ /gettest/i ){
          $testid++;
          my $testidx = int(rand(100)) + 1; 
          my $testcase = "testcase_$testidx";
          $testcase = 'NA' if($testid eq 3); 
          $response = { "status" => "OK" , "testcase" => "$testcase" } ; 
        }elsif ($action =~ /testinfo/i){
          print "ACTION:$action INFO:" . Dumper($jsondata) . "\n";
        }elsif ($action =~ /testdone/i){
          print "ACTION:$action | DONE\n";
        }

        print "Action: $action | SENDING:" .encode_json($response) . "\n";
        print $client encode_json($response) . "\n";
    }
    
    close $client;
    print "Client disconnected\n";
}

close $server;

