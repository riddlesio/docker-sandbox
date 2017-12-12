#!/usr/bin/env ruby

while input = gets do
    splitInput = input.split(' ')

    if (splitInput[0].eql? "action")
        puts ["rock", "paper", "scissors"].sample
    end
end
