module TangentMethod where

firstApprox :: (Double -> Double) -> (Double -> Double) -> (Double, Double) -> Double -> Double
firstApprox f f' (a, b) key
    | key > 0 = b - f b / f' b
    | key < 0 = a - f a / f' a


method :: (Double -> Double) -> (Double -> Double) -> Double -> (Double, Double) -> Double -> Double
method f f' e (a0, b0) key
    | (abs (a - a0)) < e = a
    | otherwise = method f f' e (a, b0) key
    where
        a = firstApprox f f' (a0, b0) key


tangentMethod :: (Double -> Double) -> (Double -> Double) -> (Double -> Double) -> Double -> (Double, Double) -> Double
tangentMethod f f' f'' e (a, b) = method f f' e (a, b) key
    where key = f' b * f'' b
