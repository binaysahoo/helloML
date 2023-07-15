use Opcode;

# Get a list of all the opcodes
my @opcodes = Opcode::opset();

# Print out each opcode with its description
foreach my $opcode (@opcodes) {
    my ($name, $desc) = @$opcode;
    print "$name: $desc\n";
}

