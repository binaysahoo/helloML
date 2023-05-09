#!/usr/bin/perl

use strict;
use warnings;
use Socket;

# Fork a child process
my $pid = fork();

if ($pid == 0) {
    # Child process
    print "Child process: PID $$\n";

    # Set up a socket
    socket(my $socket, AF_INET, SOCK_STREAM, getprotobyname('tcp')) or die "Socket failed: $!";
    print "Child process: Socket created\n";
    # Perform further operations with the socket
    # ...
    takerest("CHILD"); 

    exit;
} elsif (defined $pid) {
    # Parent process
    print "Parent process: PID $$\n";
    print "Child process ID: $pid\n";
    takerest("PARENT"); 

    # Parent process specific actions

    waitpid($pid, 0);
} else {
    die "Failed to fork: $!";
}

print "Process $$ finished\n";


sub takerest {
    my $owner = shift;
    print "TAKING REST | user:$owner for a while\n"; 
    my $idx = 0; 
    while(1){
      $idx++;
      print "Sleeping ... | user:$owner idx:$idx\n";
      if ($idx eq 20){
        last; 
      }
      sleep 2;      
    }
    print "No Money | Exiting !";
}
