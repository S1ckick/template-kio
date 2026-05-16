use strict;
use warnings;

while (<>) {
    s/^(\@[a-zA-Z]+\{)([^,\s]+)/$1EN-$2/;
    print;
}