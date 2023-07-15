$test->{runs} = {
    'run1' => { "key11" =>  'value1' },
    'run2' => 'value2',
    'run3' => 'value3',
};

my $h = join ' ', map{; my $r = 1; "$r,12"} sort keys $test->{runs}->%* ; 

print "$h\n";

use v5.10;

my $value = 42;

given ($value) {
    when (1) {
        say "The value is one";
    }
    when (42) {
        say "The value is forty-two";
    }
    default {
        say "The value is something else";
    }
}

foreach my $key (keys $test->{runs}->%*) {
   print "Key : $key | $test->{runs}->{$key}\n";
}
