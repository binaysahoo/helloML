FORK: {
    my $pid = fork();
    die "Cannot fork: $!" unless defined $pid;
    unless ($pid) {
        # This code is executed by the child process
        print "Hello pid:$pid from child process! and sleep for 3\n";
        sleep 3;
        exit;
    }
    # This code is executed by the parent process
    waitpid($pid, 0);
    last FORK;
}
# This code is executed by the parent process after the FORK block
print "Hello from parent process!\n";

