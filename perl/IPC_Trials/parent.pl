#!/usr/bin/perl

use strict;
use warnings;

print "Parent process started\n";

# Fork a child process
my $pid = fork();

if ($pid == 0) {
    # Child process
    exec 'perl', 'child.pl';
} elsif (defined $pid) {
    # Parent process
    print "PID:$pid\n";
    # Send input to the child process via STDIN
    print "Parent sending data to child\n";
    print STDIN "Hello, child process!\n";
    print STDIN "quit\n";  # Send a specific input to terminate the child process
    
    # Read the response from the child process via STDOUT
    while (my $response = <STDIN>) {
        chomp $response;
        print "Parent received: $response\n";
    }

    waitpid($pid, 0);  # Wait for the child process to terminate
} else {
    die "Failed to fork: $!";
}

print "Parent process terminated\n";

