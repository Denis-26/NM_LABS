module CombineMethod where
import qualified ChordMethod as C
import qualified TangentMethod as T


method :: (Double -> Double) -> (Double -> Double) -> Double -> (Double, Double) -> Double -> Double
method f f' e (a0, b0) key
    | (abs (a - b)) < e = a
    | otherwise = method f f' e (a, b) key
    where
        a = C.firstApprox f (a0, b0) key
        b = T.firstApprox f f' (a0, b0) key


combineMethod :: (Double -> Double) -> (Double -> Double) -> (Double -> Double) -> Double -> (Double, Double) -> Double
combineMethod f f' f'' e (a, b) = method f f' e (a, b) key
    where key = f' b * f'' b
