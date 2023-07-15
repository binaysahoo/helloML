#!/usr/bin/env perl
use Mojolicious::Lite -signatures;

get '/' => sub ($c) {
  $c->stash( guser => 222 ); # store in stash , which can be passed to templates
  $c->render(template => 'index');
};

get '/hello' => sub ($c) {
  $c->render(text => "how u you doing today");
};

get '/user' => sub ($c) {
  my $user = $c->param('username');
  
  $c->render(text => "how u you doing today : $user" );
};

# Access request information
get '/agent' => sub ($c) {
  my $host = $c->req->url->to_abs->host;
  my $ua   = $c->req->headers->user_agent;
  $c->render(text => "Request by $ua reached $host.");
};

# GET|POST|PATCH /bye
any ['GET', 'POST', 'PATCH'] => '/bye' => sub ($c) {
  $c->render(text => 'Bye World!');
};
# * /whatever
any '/whatever' => sub ($c) {
  my $method = $c->req->method;
  $c->render(text => "You called /whatever with $method.");
};


#------------------------------------------------
# use @ARGV to pick a command 
# ./myapp.pl get /hello
# /myapp.pl daemon  -l 'http://*:8888'
#-------------------------------------------------
#app->start;

# Start the Daemon Command 
app->start('daemon','-l','http://*:8888');
__DATA__

@@ index.html.ep
% layout 'default';
% title 'Welcome';
<h1>Welcome to the Mojolicious real-time web framework!</h1>

@@ layouts/default.html.ep
<!DOCTYPE html>
<html>
  <head><title><%= title %></title></head>
  <body>
    <%= content %>
    The user name is : <%= $guser %>
  </body>
</html>
