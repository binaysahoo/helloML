use Mojolicious::Lite;
use Mojo::Server::Daemon;

# Define your Mojolicious routes
get '/' => sub {
    my $c = shift;
    $c->render(text => 'Hello, world!');
};

# Create a server instance
my $daemon = Mojo::Server::Daemon->new(app => app);

# Start the server and listen on port 3000
$daemon->listen(['http://*:3000']);

# Start the event loop
$daemon->run;

