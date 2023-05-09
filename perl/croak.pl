use Carp;

sub divide {
    my ($dividend, $divisor) = @_;
    if ($divisor == 0) {
        print "Divide by zero error\n";
        return;
    }
    return $dividend / $divisor;
}

sub divide_with_croak {
    my ($dividend, $divisor) = @_;
    croak "Divide by zero error" if $divisor == 0;
    return $dividend / $divisor;
}

my $result = divide(10, 0);
print "Result: $result\n";

my $croak_result = divide_with_croak(10, 0);
print "Result: $croak_result\n";

