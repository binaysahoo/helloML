use strict;
use warnings;

# Create a pipe
my ($parent_rdr, $child_wtr);
FORK: {
  if (pipe($parent_rdr, $child_wtr)) {
    # Fork the child process
    my $pid = fork();
    die "Failed to fork: $!" unless defined $pid;
    
    # Child process
    if ($pid == 0) {
      close $parent_rdr;
      print $child_wtr "Hello from child process (PID $$)!\n";
      exit 0;
    }
    
    # Parent process
    close $child_wtr;
    my $message;
    read $parent_rdr, $message, 1024;
    print "Received message from child process (PID $pid): $message\n";
  }
}

print "Parent process (PID $$) finished.\n";

