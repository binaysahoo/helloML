use LWP::UserAgent;
use HTTP::Request;

my $rabbitmq_api_url = 'http://localhost:15672/api/exchanges/%2F/my_exchange/publish';
my $json_message = '{"key": "value"}';

my $ua = LWP::UserAgent->new;
my $request = HTTP::Request->new(
    POST => $rabbitmq_api_url,
    ['Content-Type' => 'application/json'],
    $json_message
);

$ua->request($request);



use LWP::UserAgent;
use HTTP::Request;

my $rabbitmq_api_url = 'http://guest:guest@localhost:15672/api/exchanges/%2F/my_exchange/publish';
my $json_message = '{"key": "value"}';

my $ua = LWP::UserAgent->new;
my $request = HTTP::Request->new(
   POST => $rabbitmq_api_url,
   ['Content-Type' => 'application/json'],
   $json_message
);

my $response = $ua->request($request);

if ($response->is_success) {
   print "Message published successfully.\n";
} else {
   print "Error publishing message: " . $response->status_line . "\n";
}
