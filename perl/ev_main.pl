use EV;

          # TIMERS

          my $w = EV::timer 2, 0, sub {
             warn "is called after 2s";
          };

          my $w = EV::timer 2, 2, sub {
             warn "is called roughly every 2s (repeat = 2)";
          };

          undef $w; # destroy event watcher again

          my $w = EV::periodic 0, 60, 0, sub {
             warn "is called every minute, on the minute, exactly";
          };

          # IO

          my $w = EV::io *STDIN, EV::READ, sub {
             my ($w, $revents) = @_; # all callbacks receive the watcher and event mask
             warn "stdin is readable, you entered: ", <STDIN>;
          };

          # SIGNALS

          my $w = EV::signal 'QUIT', sub {
             warn "sigquit received\n";
          };

          # CHILD/PID STATUS CHANGES

          my $w = EV::child 666, 0, sub {
             my ($w, $revents) = @_;
             my $status = $w->rstatus;
          };

          # STAT CHANGES
          my $w = EV::stat "/etc/passwd", 10, sub {
             my ($w, $revents) = @_;
             warn $w->path, " has changed somehow.\n";
          };

          # MAINLOOP
          EV::run;                # loop until EV::break is called or all watchers stop
          EV::run EV::RUN_ONCE;   # block until at least one event could be handled
          EV::run EV::RUN_NOWAIT; # try to handle same events, but do not block
