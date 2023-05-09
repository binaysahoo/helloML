use Promise::XS;
Promise::XS::use_event('AnyEvent');

my $promise = Promise::XS->new(sub {
    my ($resolve, $reject) = @_;
    # Perform some asynchronous operation
    my $timer = AnyEvent->timer(after => 1, cb => sub {
        # Operation completed successfully
        $resolve->('Hello, world!');
    });
});

$promise->then(sub {
    my $result = shift;
    print "$result\n";
})->catch(sub {
    my $error = shift;
    warn "Error: $error\n";
});

