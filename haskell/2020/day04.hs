import System.IO
import System.Environment

newtype Passport = Passport [(String, String)] deriving Show

splitString :: [Char] -> [Char] -> [[Char]]
splitString _ ""=[]
splitString sChar xs=one : splitString sChar (drop 1 two)
    where (one, two) = break (`elem` sChar) xs

-- TODO: for another day, day4 in hs

getField :: Passport -> String
getField pp = ""

partOne :: [Passport] -> String
partOne _ = ""

partTwo :: [Passport] -> String
partTwo _ = ""

main :: IO ()
main = do
    inputPath <- getArgs
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle

    let passports = splitString "\n " contents

    print passports

    --putStrLn ("Result part one: " ++ partOne inputData)
    --putStrLn ("Result part two: " ++ partTwo inputData)