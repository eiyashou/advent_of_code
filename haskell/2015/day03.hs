import System.IO
import System.Environment
import qualified Data.Set as S

every :: Int -> [a] -> [a]
every n xs = case xs of
              (y:ys) -> y : every n (drop (n-1) ys)
              [] -> []

parseInfo :: [Char] -> [(Integer, Integer)]
parseInfo = map d
    where d x = case x of '^' -> (0,-1)
                          'v' -> (0,1)
                          '<' -> (-1,0)
                          '>' -> (1,0)

vplus :: (Integer, Integer) -> (Integer, Integer) -> (Integer, Integer)
vplus (xa,ya) (xb,yb) = (xa+xb, ya+yb)

partOne :: [(Integer, Integer)] -> [Char]
partOne xs = show $ length $ S.toList $ S.fromList $ scanl vplus (0,0) xs

partTwo :: [(Integer, Integer)] -> [Char]
partTwo xs = show $ length $ S.toList $ S.fromList (robo ++ real) 
    where robo = scanl vplus (0,0) $ every 2 xs
          real = scanl vplus (0,0) $ every 2 $ tail xs

main :: IO ()
main = do
    inputPath <- getArgs
    handle <- openFile (head inputPath) ReadMode
    contents <- hGetContents handle

    let inputData = parseInfo contents

    putStrLn ("Result part one: " ++ partOne inputData)
    putStrLn ("Result part two: " ++ partTwo inputData)