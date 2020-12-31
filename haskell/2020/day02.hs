import System.IO
import System.Environment
import Data.List
{--
countOcc :: Char -> String -> Int
countOcc ch = foldl (\acc x -> if x == ch then acc+1 else acc) 0

partOne :: [(Int, Int, Char, String)] -> String
partOne xs = show $ sum [ 1 | (a,b,cha,pw) <- xs, let c = countOcc cha pw, a-1 < c && b+1 > c]

partTwo :: [(Int, Int, Char, String)] -> String
partTwo xs = show $ sum [ 1 | (a,b,cha,pw) <- xs, let af = (pw !! (a-1)) == cha, let bf = (pw!!(b-1)) ==cha, af && not bf || not af && bf]

splitString :: String -> [String]
splitString "" = [""]
splitString xs = [head $ break (`elem` [" ","-",":"]) xs]:(splitString $ tail $ break (`elem` [" ","-",":"]) xs)

-- TODO: string stuffff

parsePassword :: String -> (Int, Int, Char, String)
parsePassword xs = (read (head stuff) :: Int, read (stuff !! 1) :: Int, head (stuff !! 2), stuff !! 3)
    where 
        stuff = splitString xs

_ = span (`elem` [" ",":"])

main :: IO ()
main = do
    inputPath <- getArgs
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle

    let inputData = map parsePassword (lines contents)

    putStrLn ("Result part one: " ++ partOne inputData)
    putStrLn ("Result part two: " ++ partTwo inputData)--}