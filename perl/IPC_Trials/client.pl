use strict;
use warnings;
use IO::Socket::UNIX;
use JSON;
use Data::Dumper;

my $socket_path = '/tmp/mysocket.sock';
my $client = IO::Socket::UNIX->new(
    Type => SOCK_STREAM,
    Peer => $socket_path
) or die "Failed to create client socket: $!";

#========================================================================================== 
# request from client         | response to client
#------------------------------------------------------------------------------------------
# { action => "gettest" } | respose: { testcase => "name|NA","status" => "OK" } 
# { action => "testinfo", pid => 123, rundir => "rundirname", runoption => "" , runlog => "" }   | response { "status => "OK" }
# { action => "testdone" } | respose: { "status" => "OK" } 
#========================================================================================== 

my $testid = 0 ; 
while ((my $testcase = get_testcase($client) ) ne 'NA' ) { 
    $testid++; 
    print "RESPONSE: Run Testcases $testcase\n "; 
   
    my $pid = fork(); 
    # now run the testcase | fork and return the pid 
    if (defined $pid){
        # child process
        if($pid == 0 ) {
          run_test($testcase);
        }else{  # parent process
          print "Running Child PID:$pid\n"; 
	  my $data = { action => "testinfo", pid => $pid, rundir => "rundirname", runoption => "" , runlog => "" };
	  # send test run info
	  my $resp = send_rec_socket($client,$data); 
	  print "RESP: " . Dumper ($resp) . "\n"; 

          # wait 
          my $childstatus = waitpid($pid, 0);
          if($childstatus != -1 ){
            print "DONE CHILD PROCESS:$pid \n";
            my $respdone = send_rec_socket($client,{ action => "testdone", pid=>$pid , testcase => $testcase} );  
            print "RESP: " . Dumper ($respdone) . "\n"; 
          }
        } 
    }


  
} # while

#========================================================================================== 
# 
#========================================================================================== 
sub run_test {
   my $testcase = shift;
   print "Running Testcase: $testcase\n";
   sleep 60 ; 
   print "Done Testcase: $testcase\n";
   exit 0; 
}

sub send_rec_socket {
   my $socket  = shift;  
   my $data    = shift;
   my $jsondata = encode_json($data);

   print $socket "$jsondata\n";

   #shutdown($socket, 1);    # incase SEND DATA SOCKET to be CLOSED and RECEIVE to remain OPEN

   while (my $response = <$socket> ) {
      chomp $response;
      my $res = decode_json($response);
      return $res;
  }
  return { "status" => "OK" } ; 
}

sub get_testcase {
   my $socket  = shift;  
   my $request = { action => "gettest" };
   my $response = send_rec_socket($socket,$request);
   return $response->{testcase} // 'NA'; 
}


close $client;

