<!DOCTYPE html>
<html>
<head>
    <title>Side Nav with Content</title>
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
    <!-- Perl-generated links will be inserted here -->
</div>

<div class="main" id="mainContent">
    <!-- Page content will be loaded here -->
</div>

<script>
    // Function to load content when link is clicked
    function loadContent(file) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById("mainContent").innerHTML = this.responseText;
            }
        };
        xhttp.open("GET", file, true);
        xhttp.send();
    }

    // Add click event listeners to generated links
    var links = document.querySelectorAll('.sidenav a');
    for (var i = 0; i < links.length; i++) {
        links[i].addEventListener('click', function(event) {
            event.preventDefault();
            var file = this.getAttribute('href');
            loadContent(file);
        });
    }
</script>

</body>
</html>
