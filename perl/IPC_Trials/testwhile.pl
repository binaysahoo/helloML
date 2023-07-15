#!/usr/bin/perl 

#use strict;
#use warnings;

# Function that returns a value
sub check_condition {
    my $id = shift;
    return 'NA' if ($id eq 4 ); 
    return "unit_FPGA/"; 
}

# Main loop
my $idx = 0; 
print "starting: $idx \n "; 
while ( $idx <  11  && ( my $testcase = check_condition($idx) ) ne 'NA' ) {
    # Perform actions inside the loop
    # You can add your code here
    print "sleeping $idx  | testcase:$testcase\n"; 
    #sleep 2;
    $idx++;
}

# Code after the loop
print "Loop exited.\n";

