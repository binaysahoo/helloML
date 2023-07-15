#!/usr/bin/perl -d

use strict;
use warnings;

my $number = 42;

print "The number is: $number\n";

# Example subroutine
sub foo {
    my $bar = shift;

    print "Inside foo()\n";
    print "Received argument: $bar\n";
}

foo("Hello, world!");

print "End of script\n";

