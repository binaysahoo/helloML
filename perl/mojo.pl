use Mojolicious::Lite;

# WebSocket route
websocket '/echo' => sub {
    my $c = shift;

    # Handle incoming messages
    $c->on(message => sub {
        my ($c, $msg) = @_;
        $c->send("You said: $msg");
    });
};
get '/' => {text => 'I Mojolicious!'};
app->start;
