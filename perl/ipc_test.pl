use IPC::Run qw(run timeout);

my @cmd = ('ls', '-l');

my ($out, $err);

# Run the command and capture its output and error streams
run \@cmd, '>', \$out, '2>', \$err, timeout(10) or die "Failed to run @cmd: $!";

print "Output:\n$out\n";
print "Error:\n$err\n";

