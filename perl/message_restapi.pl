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
