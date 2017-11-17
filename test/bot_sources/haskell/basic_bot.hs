module Main where
import Control.Monad
import System.IO
import System.Random

randomRPS = do
  randInt <- randomRIO (0, 3 :: Int)
  if randInt == 0 then do putStrLn "rock";
  else do
    if randInt == 1 then do putStrLn "paper";
    else do putStrLn "scissors"

process (x:xs) = do
  case x of
    "action" -> do randomRPS
    _        -> return ()

loop = do
    line <- getLine
    process (words line)
    eof <- isEOF
    unless eof loop

main = loop
