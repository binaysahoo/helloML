my $hashref = { foo => 1, bar => 2, baz => 3 };

#foreach my $pair ($hashref->%*) {
foreach my $pair ($hashref->%*) {
    my ($key, $value) = @$pair;
    print "$key => $value\n";
}

