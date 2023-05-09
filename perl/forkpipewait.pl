use strict;
use warnings;

my $pid = fork();
if (not defined $pid) {
    die "Failed to fork: $!";
}
elsif ($pid == 0) {
    # Child process
    my ($rdr, $wtr);
    pipe($rdr, $wtr) or die "Failed to create pipe: $!";

    # Write to the pipe
    print $wtr "Hello from child process (PID $$)!\n";
    close $wtr;

    # Exit
    exit 0;
}
else {
    # Parent process
    my ($rdr, $wtr);
    pipe($rdr, $wtr) or die "Failed to create pipe: $!";

    # Read from the pipe
    my $message;
    while (defined(my $line = <$rdr>)) {
        $message .= $line;
    }
    close $rdr;

    # Wait for the child process to finish
    my $pid_status = waitpid($pid, 0);
    if ($pid_status == -1) {
        die "Failed to wait for child process: $!";
    }
    elsif ($pid_status & 0x7F) {
        die sprintf("Child process died with signal %d", ($pid_status & 0x7F));
    }
    else {
        my $exit_code = $pid_status >> 8;
        print "Received message from child process (PID $pid, exit code $exit_code): $message";
    }
}

