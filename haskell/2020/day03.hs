import System.IO
import System.Environment

partOne :: [String] -> Integer -> Integer -> String
partOne xs dx dy = show $ sum [ 1 | (d, line) <- zip [0,1..] xs, y d == 0, (line !! x d) == '#']
    where 
        lenlin = toInteger $ length $ head xs
        x d = (toInteger dx*d/dy) `mod` lenlin
        y d = d `mod` dy

partTwo :: [String] -> String
partTwo xs = show $ product [ read $ partOne xs dx dy | (dx,dy) <- [(1,1),(3,1),(5,1),(7,1),(1,2)] ]

main :: IO ()
main = do
    inputPath <- getArgs
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle

    let inputData = lines contents

    putStrLn ("Result part one: " ++ partOne inputData 2 1)
    putStrLn ("Result part two: " ++ partTwo inputData)