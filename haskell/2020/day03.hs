import System.IO
import System.Environment

partOne :: [String] -> Int-> Int -> String
partOne xs dx dy = show $ sum [ 1 | (i, line) <- drop 1 $ zip [0,1..] xs, posY i `mod` dy == 0, line !! posX i == '#']
    where 
        lenlin = length $ head xs
        posX d = mod (d*dx `div` dy) lenlin
        posY d = d

partTwo :: [String] -> String
partTwo xs = show $ product [ read $ partOne xs dx dy | (dx,dy) <- [(1,1),(3,1),(5,1),(7,1),(1,2)] ]

main :: IO ()
main = do
    inputPath <- getArgs
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle

    let inputData = lines contents

    putStrLn ("Result part one: " ++ partOne inputData 3 1)
    putStrLn ("Result part two: " ++ partTwo inputData)