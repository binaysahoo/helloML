#!/usr/bin/perl
use strict;
use warnings;
use File::Find;

my $base_dir = '/path/to/your/source/files'; # Replace with the base directory path
my $output_file = 'index.html'; # Output HTML file name

# Open output file for writing
open(my $fh, '>', $output_file) or die "Cannot open file '$output_file' for writing: $!";

# Write HTML header
print $fh <<EOF;
<!DOCTYPE html>
<html>
<head>
    <title>Side Nav with Content</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        /* Style for the side navigation */
        .sidenav {
            height: 100%;
            width: 250px;
            position: fixed;
            z-index: 1;
            top: 0;
            left: 0;
            background-color: #f1f1f1;
            overflow-x: hidden;
            padding-top: 20px;
        }

        .sidenav a {
            padding: 6px 8px 6px 16px;
            text-decoration: none;
            font-size: 18px;
            color: black;
            display: block;
        }

        .sidenav a:hover {
            background-color: #ddd;
        }

        /* Style for the main content area */
        .main {
            margin-left: 250px;
            padding: 20px;
        }
    </style>
</head>
<body>

<div class="sidenav">
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
            print $fh "<ul class='nested'>\n";
            process_dir("$dir/$subdir");
            print $fh "</ul>\n";
            print $fh "</li>\n";
        }
        print $fh "</ul>\n";
    }

    if (@files) {
        print $fh "<ul>\n";
        foreach my $file (@files) {
            my $file_path = "$dir/$file";
            my $file_name = $file;
            print $fh "<li><a href='$file_path' class='file-link'>$file_name</a></li>\n";
        }
        print $fh "</ul>\n";
    }
}

# Call the subroutine for the base directory
process_dir($base_dir);

# Write HTML footer and JavaScript
print $fh <<EOF;
</div>

<div class="main" id="mainContent">
    <!-- Page content will be loaded here -->
</div>

<script>
    // Load content when file link is clicked
    $('.file-link').on('click', function(event) {
        event.preventDefault();
        var file = $(this).attr('href');
        $.get(file, function(data) {
            $('#mainContent').html('<pre>' + data + '</pre>');
        });
    });

    // Script to handle dropdown functionality
    $('.dropdown').on('click', function() {
        $(this).toggleClass("active");
        var nested = $(this).next();
        if (nested.css('display') === 'block') {
            nested.css('display', 'none');
        } else {
            nested.css('display', 'block');
        }
    });
</script>

</body>
</html>
EOF

# Close the output file
close($fh);

print "HTML file '$output_file' generated successfully.\n";
