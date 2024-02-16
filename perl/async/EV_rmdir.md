Sure, if you want to use asynchronous programming with `EV` (a Perl interface to libev), you can leverage the `EV` module along with non-blocking calls. Here's a simple example using `EV`:

```perl
use strict;
use warnings;
use File::stat;
use EV;

my $dir_path = '/path/to/directories';

# Get a list of directories in the specified path
opendir my $dir_handle, $dir_path or die "Cannot open directory: $!";
my @directories = grep { -d "$dir_path/$_" && ! /^\.{1,2}$/ } readdir $dir_handle;
closedir $dir_handle;

# Sort directories by modification time (latest first)
my @sorted_directories = map  { $_->[0] }
                         sort { $b->[1] <=> $a->[1] }
                         map  { [$_, stat("$dir_path/$_")->mtime] }
                         @directories;

# Keep the latest three directories
my @directories_to_keep = @sorted_directories[0..2];

# Set up EV watcher for asynchronous processing
my $ev = EV::loop->new;
my $async_watcher;

# Function to remove directory asynchronously
sub remove_directory {
    my ($directory) = @_;

    my $full_path = "$dir_path/$directory";
    next if grep { $_ eq $directory } @directories_to_keep;

    rmdir $full_path or warn "Failed to remove directory $full_path: $!";
    
    # Stop the watcher if all directories are processed
    $ev->now_update;
    $async_watcher->stop if !@directories;

    return;
}

# Watcher for asynchronous processing
$async_watcher = EV::timer 0, 0, sub {
    my $directory = shift @directories;
    return unless defined $directory;

    remove_directory($directory);
};

EV::loop;  # Start the event loop
```

This script uses the `EV` module and sets up an asynchronous timer (`EV::timer`) for processing directories. The `remove_directory` function is called asynchronously for each directory, and the watcher stops when all directories are processed. Adjust the `$dir_path` variable according to your directory path.
