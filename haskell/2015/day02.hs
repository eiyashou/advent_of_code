import System.IO
import System.Environment

splitString :: [Char] -> [Char] -> [[Char]]
splitString _ ""=[]
splitString sChar xs=one : splitString sChar (drop 1 two)
    where (one, two) = break (`elem` sChar) xs

parseInfo :: [Char] -> [(Integer, Integer, Integer)]
parseInfo xs= [ (a,b,c) | x <- splitString "\n" xs, let (a:b:c:_) = map (\n -> read n :: Integer) $ splitString "x" x ]

partOne :: [(Integer, Integer, Integer)] -> [Char]
partOne xs = show $ sum $ map (\(l,w,h) -> 2*l*w + 2*w*h + 2*h*l + 1) xs

partTwo :: [(Integer, Integer, Integer)] -> [Char]
partTwo xs = show $ sum $ map (\(l,w,h) -> l*w*h + minimum [2*a+2*b | (a,b) <- [(l,w),(h,l),(w,h)]]) xs

main :: IO ()
main = do
    inputPath <- getArgs
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle

    let inputData = parseInfo contents

    putStrLn ("Result part one: " ++ partOne inputData)
    putStrLn ("Result part two: " ++ partTwo inputData)