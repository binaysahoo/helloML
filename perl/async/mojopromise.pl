use Mojo::Promise qw(collect);

# Create some promises...
my $promise1 = Mojo::Promise->new;
my $promise2 = Mojo::Promise->new;
my $promise3 = Mojo::Promise->new;

# Register a catch callback for a new promise that collects the results of the other promises
collect($promise1, $promise2, $promise3)->catch(sub {
  my ($collect_err) = @_;
  # Handle the error that caused the promise to be rejected...
});

# Resolve the promises...
$promise1->resolve('value1');
$promise2->resolve('value2');
$promise3->resolve('value3');

