module PolyDerivative (
    derivative
) where

derivative :: (Num a) => [a] -> [a]
derivative [] = [0]
derivative [_] = [0]
derivative cs =
    map (\(c, i) -> c * fromIntegral i ) cs_i
    where
        cs_i = zip (init cs) [length cs - 1, length cs - 2 ..]
