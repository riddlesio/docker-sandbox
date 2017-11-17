#!/usr/bin/env lua

function mysplit(inputstr, sep)
    if sep == nil then
            sep = "%s"
    end
    local t={} ; i=1
    for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
            t[i] = str
            i = i + 1
    end
    return t
end

while true do
    input = io.read()
    if input == nil then break end
    
    inputSplit = mysplit(input, " ")
    if inputSplit[1] == "action" then
        getRandomNumber =  math.random(3)
        if getRandomNumber == 1 then
            print("rock")
        elseif getRandomNumber == 2 then
            print("paper")
        elseif getRandomNumber == 3 then
            print("scissors")
        end
    end
end
