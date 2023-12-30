#!/usr/bin/perl
use strict;
use warnings;
use File::Find;
use File::Basename;

my $base_dir = '/path/to/your/source/files'; # Replace with the base directory path
my $output_file = 'navigator.html'; # Output HTML file name

# Open output file for writing
open(my $fh, '>', $output_file) or die "Cannot open file '$output_file' for writing: $!";

# Write HTML header
print $fh <<EOF;
<!DOCTYPE html>
<html>
<head>
    <title>Left Side Navigator</title>
    <style>
        .dropdown {
            position: relative;
            display: inline-block;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }
        .dropdown:hover .dropdown-content {
            display: block;
        }
    </style>
</head>
<body>
    <h1>Left Side Navigator</h1>
    <ul>
EOF

# Subroutine to generate dropdowns and links
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

    if (@subdirs) {
        print $fh "<ul>\n";
        foreach my $subdir (@subdirs) {
            print $fh "<li class='dropdown'>$subdir\n";
            process_dir("$dir/$subdir");
            print $fh "</li>\n";
        }
        print $fh "</ul>\n";
    }

    if (@files) {
        print $fh "<ul>\n";
        foreach my $file (@files) {
            my $file_path = "$dir/$file";
            my $file_name = basename($file_path);
            print $fh "<li><a href='$file_path'>$file_name</a></li>\n";
        }
        print $fh "</ul>\n";
    }
}

# Call the subroutine for the base directory
process_dir($base_dir);

# Write HTML footer
print $fh <<EOF;
    </ul>
</body>
</html>
EOF

# Close the output file
close($fh);

print "HTML file '$output_file' generated successfully.\n";
