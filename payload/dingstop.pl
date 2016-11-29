# dingstop.pl
# by Baran Balkan
# used to stop dingrod. 
use strict;
use warnings;

my $raw   = `ps -ef | grep "[d]ingrod"`;
my @lines = split "\n", $raw;

foreach my $line (@lines)
{
  my @words = split " ", $line;
  print $words[1];
  if ($words[0] eq "dingrod")
  { system("kill",$words[1]);}
}
exit 0;
