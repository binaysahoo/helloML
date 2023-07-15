#!/usr/bin/perl

my @commands = ('one','two');

my %running = (
    'cmd1' => 'pid1',
    'cmd2' => 'pid2',
);

my %default = (
  'zero' => 0
);
#my %show = (%running, map{; 'pending' => $_} @commands);
my %show = (%default,%running, map{; 'pending' => [$_] } @commands);

#my $message = join("\n", map {; "-- $_ => @{$show{$_}->{cmd}}" }  grep { defined $show{$_}->{cmd} } sort keys %show );
my $message = join("\n", map {; "-- $_ => @{$show{$_}->{cmd}}" }  sort keys %show );

for my $key (keys %show) {
  print "$key -> $show{$key} \n";
};

print "MSG:$message\n"; 
