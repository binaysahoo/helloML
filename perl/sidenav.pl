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
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        /* Custom style for the main content area */
        .main {
            padding: 20px;
        }
    </style>
</head>
<body>

<div class="container-fluid">
    <div class="row">
        <nav class="col-md-2 d-none d-md-block bg-light sidebar">
            <div class="sidebar-sticky">
                <ul class="nav flex-column">
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
        foreach my $subdir (@subdirs) {
            print $fh "<li class='nav-item dropdown'>\n";
            print $fh "<a class='nav-link dropdown-toggle' href='#' role='button' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'>$subdir</a>\n";
            print $fh "<ul class='dropdown-menu'>\n";
            process_dir("$dir/$subdir");
            print $fh "</ul>\n";
            print $fh "</li>\n";
        }
    }

    if (@files) {
        foreach my $file (@files) {
            my $file_path = "$dir/$file";
            my $file_name = $file;
            print $fh "<li class='nav-item'><a class='nav-link file-link' href='$file_path'>$file_name</a></li>\n";
        }
    }
}

# Call the subroutine for the base directory
process_dir($base_dir);

# Write HTML footer and JavaScript
print $fh <<EOF;
                </ul>
            </div>
        </nav>

        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
            <div class="main" id="mainContent">
                <!-- Page content will be loaded here -->
            </div>
        </main>
    </div>
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
</script>

<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js"></script>
</body>
</html>
EOF

# Close the output file
close($fh);

print "HTML file '$output_file' generated successfully.\n";
