import System.IO
import System.Environment

partOne :: [Integer] -> String
partOne xs = show $ head [ n*(2020-n) | n <- xs, 2020-n `elem` xs ]

partTwo :: [Integer] -> String
partTwo xs = show $ head [ n*m*(2020-n-m) | (i, n) <- zip [1..] xs, m <- drop i xs, 2020-n-m `elem` xs ]


main :: IO ()
main = do
    inputPath <- getArgs 
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle
    let inputData = map read (lines contents)
        
    putStrLn ("Result part one: " ++ partOne inputData)
    putStrLn ("Result part two: " ++ partTwo inputData)