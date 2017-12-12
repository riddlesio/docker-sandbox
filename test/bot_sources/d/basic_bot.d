module main;

import std.string;
import std.stdio;
import std.conv;
import std.random;

void main(string[] args)
{
    foreach(str; stdin.byLine){
        auto s = to!string(str);
        auto splittedString = split(s);

        if (splittedString[0] == "settings") {
            stderr.writeln(s);
        } else if (splittedString[0] == "update") {
            stderr.writeln(s);
        } else if (splittedString[0] == "action") {
            auto i = uniform(0, 3);
            if( i == 0){
                stdout.writeln("rock");
            }
            if( i == 1){
                stdout.writeln("paper");
            }
            if( i == 2){
                stdout.writeln("scissors");
            }
        }
    }
}