use AnyEvent;
use AnyEvent::Socket;
use AnyEvent::Handle;

my $port = 1234;

my $server = tcp_server "0.0.0.0", $port, sub {
    my ($fh, $host, $port) = @_;
    my $handle = AnyEvent::Handle->new(
        fh => $fh,
        on_read => sub {
            my ($handle) = @_;
            my $data = $handle->rbuf;
            $handle->rbuf = '';
            $handle->push_write("received: $data");
        },
        on_error => sub {
            my ($handle, $fatal, $message) = @_;
            $handle->destroy();
        }
    );
};

print "Listening on port $port...\n";
AnyEvent->condvar->recv;

