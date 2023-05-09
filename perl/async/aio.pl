use IO::AIO;

# Open a file for asynchronous I/O
open(my $fh, '<', 'myfile.txt') or die "Cannot open file: $!";
my $offset = 0;
my $length = 1024;
my $reg = {
    fh => $fh,
    cb => sub { my $buf = shift; print $buf },
    mask => AIO_READ,
    offset => $offset,
    length => $length
};
my $aioreq = AIO::aioreg_pri($reg);

