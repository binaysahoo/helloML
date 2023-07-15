use Mojolicious::Lite -signatures;

# Render template "index.html.ep" from the DATA section
get '/' => sub ($c) {
  $c->render(template => 'index');
};

# WebSocket service used by the template to extract the title from a web site
websocket '/title' => sub ($c) {
  $c->on(message => sub ($c, $msg) {
    my $title = $c->ua->get($msg)->result->dom->at('title')->text;
    $c->send($title);
  });
};

app->start;
__DATA__

@@ index.html.ep
% my $url = url_for 'title';
<script>
  const ws = new WebSocket('<%= $url->to_abs %>');
  ws.onmessage = function (event) { document.body.innerHTML += event.data };
  ws.onopen    = function (event) { ws.send('https://mojolicious.org') };
</script>