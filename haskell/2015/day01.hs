import System.IO
import System.Environment

partOne :: [Integer] -> [Char]
partOne xs = show $ sum xs

partTwo :: [Integer] -> [Char]
partTwo xs = show $ head [ i | (i,x) <- zip [0..] (scanl (+) 0 xs), x == -1]

main :: IO ()
main = do
    inputPath <- getArgs
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle

    let inputData = fmap (\x -> if x=='(' then 1 else -1) contents

    putStrLn ("Result part one: " ++ partOne inputData)
    putStrLn ("Result part two: " ++ partTwo inputData)