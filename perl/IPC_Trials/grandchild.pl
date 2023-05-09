use POSIX qw(mkfifo);

# Create named pipes
mkfifo("pipe1", 0600);
mkfifo("pipe2", 0600);

# Fork first child
my $pid1 = fork();
die "Error: fork failed" unless defined $pid1;

if ($pid1 == 0) {
    # Child process 1
    open(my $pipe1, '>', "pipe1") or die "Error: can't open pipe1";
    #print $pipe1 "Message from child process 1\n";
    #my $out1 = qx{/Users/binaysahoo/workspace/perl/map.pl } ;
    my $out1 = qx{/bin/date} ;
    print $pipe1 "OUT1: $out1\n";
    print "OUT1: $out1\n";
    close $pipe1;
    exit;
}

# Fork second child
my $pid2 = fork();
die "Error: fork failed" unless defined $pid2;

if ($pid2 == 0) {
    # Child process 2
    open(my $pipe2, '>', "pipe2") or die "Error: can't open pipe2";
    print $pipe2 "Message from child process 2\n";
    close $pipe2;
    exit;
}

# Parent process
open(my $pipe1, '<', "pipe1") or die "Error: can't open pipe1";
my $message1 = <$pipe1>;
close $pipe1;

open(my $pipe2, '<', "pipe2") or die "Error: can't open pipe2";
my $message2 = <$pipe2>;
close $pipe2;

print "Message from child process 1: $message1";
print "Message from child process 2: $message2";

