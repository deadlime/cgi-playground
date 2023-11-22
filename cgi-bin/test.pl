#!/usr/bin/perl

print "Content-type: text/plain\n\nHello, World.\n";

print "\nEnrivonment:\n";
foreach my $key (keys %ENV) {
    print "$key=$ENV{$key}\n";
}

print "\nInput:\n";
while (<>) {
    print;
}
print "\n";
