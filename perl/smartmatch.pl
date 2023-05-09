my $a = 42;
my $b = "42";
if ($a ~~ $b) {
    print "Equal\n";
} else {
    print "Not equal\n";
}
my @array = (1, 2, 3, 4, 5);
if (3 ~~ @array) {
    print "Found\n";
} else {
    print "Not found\n";
}

