
my $i = 0; 
print "Child:$i\n";
while(1) {
  $i++;
  print "count:$i\n";
  sleep 1;
  last if ($i eq 10);
}
