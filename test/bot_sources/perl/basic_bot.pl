#!/usr/bin/env perl

while (<>) {
    chomp $_;
    @_ = split(' ', $_);

    if (@_[0] eq "settings") {
        print STDERR "@_\n";
    } elsif (@_[0] eq "update") {
        print STDERR "@_\n";
    } elsif (@_[0] eq "action") {
        $random_number = int(rand(3));

        if ($random_number == 0) {
            print "rock\n";
        } elsif ($random_number == 1) {
            print "paper\n";
        } elsif ($random_number == 2) {
            print "scissors\n";
        }
    }
}