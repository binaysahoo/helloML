#!/usr/bin/perl

$SIG{INT} = \&handle_sigint;

sub handle_sigint {
    print "Received SIGINT signal. Exiting...\n";
    exit;
}

my $i = 0; 
print "Child:$i\n";
while(1) {
  $i++;
  print "count:$i\n";
  sleep 1;
  last if ($i eq 100);
}
