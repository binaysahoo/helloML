#!/usr/bin/perl

use File::Basename;
use FIle::Spec::Functions;

BEGIN {
  #for (@INC) {
     #$_ = File::Spec->rel2abs($_);
  #}
}

for (@INC){
  print "PATH:$_\n";
}
# Set up some I/O watchers
my $fd1 = fileno(STDIN);
# Set up some I/O watchers
my $fd2 = fileno(STDOUT);
print "INFO : -----$fd1 | $fd2\n"; 

###########################################3
############################################3
use B::Deparse;

sub foo {
    my $x = 1;
    my $y = 2;
    return $x + $y;
}

my $deparser = B::Deparse->new();
my $code = \&foo;
my $source = $deparser->coderef2text($code);
print $source . "\n";
############################################3
use Opcode;

sub my_sub {
    my $x = shift;
    my $y = shift;
    return $x + $y;
}

#my $opcodes = Opcode::opcodes(\&my_sub);

#foreach my $opcode (@$opcodes) {
#    my $name = Opcode::opname($opcode);
#    my $desc = Opcode::opdesc($opcode);
#    print "$name ($desc)\n";
#}

############################################3
use Hash::Util;

my %my_hash = (
    foo => 1,
    bar => 2,
    baz => 3,
);

Hash::Util::lock_hash(%my_hash);

$my_hash{qux} = 4; # This will cause an error because the hash is locked


