import System.IO
import System.Environment
import Data.List

xor :: Bool -> Bool -> Bool
xor a b=a&&not b||not a&&b

countOcc :: Char -> String -> Int
countOcc ch = foldl (\acc x -> if x == ch then acc+1 else acc) 0

partOne :: [(Int, Int, Char, String)] -> String
partOne xs = show $ sum [ 1 | (a,b,cha,pw) <- xs, let c = countOcc cha pw, a-1 < c && b+1 > c]

partTwo :: [(Int, Int, Char, String)] -> String
partTwo xs = show $ sum [ 1 | (a,b,cha,pw) <- xs, let af = (pw !! (a-1)) == cha, let bf = (pw!!(b-1)) ==cha, af `xor` bf]

splitString :: [Char] -> [[Char]]
splitString ""=[]
splitString xs=one : splitString (drop 1 two)
    where (one, two) = break (`elem` [' ','-',':']) xs

parsePassword :: String -> (Int, Int, Char, String)
parsePassword xs = (read (head stuff) :: Int, read (stuff !! 1) :: Int, head (stuff !! 2), stuff !! 4)
    where stuff = splitString xs

main :: IO ()
main = do
    inputPath <- getArgs
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle

    let inputData = map parsePassword $ lines contents

    putStrLn ("Result part one: " ++ partOne inputData)
    putStrLn ("Result part two: " ++ partTwo inputData)