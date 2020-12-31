import System.IO
import System.Environment

quicksort :: (Ord a) => [a] -> [a]  
quicksort [] = []  
quicksort (x:xs) =   
    let smallerSorted = quicksort [a | a <- xs, a <= x]  
        biggerSorted = quicksort [a | a <- xs, a > x]  
    in  smallerSorted ++ [x] ++ biggerSorted  

binToID :: [Char] -> Int
binToID xs=sum [ 2^i | (i,x) <- zip [0,1..] (reverse xs), x `elem` ['B','R'] ]

partOne :: [Int] -> String
partOne xs = show $ maximum xs

partTwo :: [Int] -> String
partTwo xs = show $ head [ a+1 | (a,b) <- zip xs (drop 1 xs), b-a > 1 ]

main :: IO ()
main = do
    inputPath <- getArgs
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle

    let inputData = quicksort $ map binToID $ lines contents

    putStrLn ("Result part one: " ++ partOne inputData)
    putStrLn ("Result part two: " ++ partTwo inputData)