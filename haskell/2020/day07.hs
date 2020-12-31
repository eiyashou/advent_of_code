import System.IO
import System.Environment

-- TODO: day 7

partOne :: any -> String
partOne _ = ""

partTwo :: any -> String
partTwo _ = ""

main :: IO ()
main = do
    inputPath <- getArgs
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle

    let inputData = lines contents

    putStrLn ("Result part one: " ++ partOne inputData)
    putStrLn ("Result part two: " ++ partTwo inputData)