module ChordMethod where

firstApprox :: (Double -> Double) -> (Double, Double) -> Double -> Double
firstApprox f (a, b) key
    | key > 0 = a - ((f(a)*(b-a)) / (f(b) - f(a)))
    | key < 0 = b - ((f(b)*(b-a)) / (f(b) - f(a)))

method :: (Double -> Double) -> Double -> (Double, Double) -> Double -> Double
method f e (a0, b0) key
    | (abs (a - a0)) < e = a
    | otherwise = method f e (a, b0) key
    where
        a = firstApprox f (a0, b0) key

chordMethod :: (Double -> Double) -> (Double -> Double) -> (Double -> Double) -> Double -> (Double, Double) -> Double
chordMethod f f' f'' e (a, b) = method f e (a, b) key
    where key = f' b * f'' b
