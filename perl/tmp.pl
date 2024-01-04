#!/usr/bin/perl
use strict;
use warnings;
use File::Find;
use File::Basename;

my $base_dir = '/path/to/your/source/files'; # Replace with the base directory path
my $output_file = 'navigator_bootstrap.html'; # Output HTML file name

# Open output file for writing
open(my $fh, '>', $output_file) or die "Cannot open file '$output_file' for writing: $!";

# Write HTML header with Bootstrap CDN links
print $fh <<EOF;
<!DOCTYPE html>
<html>
<head>
    <title>Bootstrap Left Side Navigator</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .dropdown-submenu {
            position: relative;
        }
        .dropdown-submenu .dropdown-menu {
            top: 0;
            left: 100%;
            margin-top: -1px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bootstrap Left Side Navigator</h1>
        <div class="list-group">
EOF

# Subroutine to generate list items for directories and files
sub process_dir {
    my ($dir) = @_;
    my @subdirs;
    my @files;

    opendir(my $dh, $dir) or die "Cannot open directory '$dir': $!";
    while (my $file = readdir($dh)) {
        next if ($file =~ /^\./); # Skip hidden files
        if (-d "$dir/$file") {
            push @subdirs, $file;
        } elsif (-f "$dir/$file") {
            push @files, $file;
        }
    }
    closedir($dh);

    foreach my $subdir (@subdirs) {
        print $fh "<a href='#' class='list-group-item list-group-item-action list-group-item-primary dropdown-toggle' data-toggle='dropdown'>$subdir</a>\n";
        print $fh "<div class='dropdown-menu'>\n";
        process_dir("$dir/$subdir");
        print $fh "</div>\n";
    }

    foreach my $file (@files) {
        my $file_path = "$dir/$file";
        my $file_name = basename($file_path);
        print $fh "<a href='$file_path' class='list-group-item list-group-item-action'>$file_name</a>\n";
    }
}

# Call the subroutine for the base directory
process_dir($base_dir);

# Write HTML footer with Bootstrap JavaScript CDN link
print $fh <<EOF;
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
EOF

# Close the output file
close($fh);

print "HTML file '$output_file' generated successfully.\n";

#
#sudo yum install -y wget
#sudo wget -O /etc/yum.repos.d/adoptopenjdk.repo https://adoptopenjdk.jfrog.io/adoptopenjdk/rpm/centos/adoptopenjdk.repo
