module Horner where

upperBorder :: [Int] -> Int
upperBorder coeffs = sum (takeWhile (\x -> not $ compare_coeffs $ horner coeffs x ) [0..])


horner :: [Int] -> Int -> [Int]
horner coeffs point = tail $ scanl (\acc x -> acc * point + x) 0 coeffs


compare_coeffs :: [Int] -> Bool
compare_coeffs horner_coeffs = (head horner_coeffs) >= 0 && (all (>0) $ tail horner_coeffs)
