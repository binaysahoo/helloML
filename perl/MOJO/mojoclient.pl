use Mojo::WebSocket::Client;

my $client = Mojo::WebSocket::Client->new;
$client->connect('ws://localhost/echo' => sub {
    my ($client, $tx) = @_;
    $tx->send('Hello, server!');
    $tx->on(message => sub {
        my ($tx, $msg) = @_;
        print "Received: $msg\n";
    });
});

