use B;
use B::Deparse;

my $code = sub {
    my $x = 1;
    my $y = 2;
    my $z = $x + $y;
    print $z;
};

my $deparse = B::Deparse->new("-p", "-sC");
print $deparse->coderef2text($code);

