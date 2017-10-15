module Horner where

upperBorder :: [Int] -> Int -> Int
upperBorder coeffs x
    | compare_coeffs $ horner coeffs x = x
    | otherwise = upperBorder coeffs (x + 1)

lowerBorder :: [Int] -> Int -> Int
lowerBorder coeffs x
    | compare_coeffs $ horner normal_coeffs x = negate x
    | otherwise = lowerBorder normal_coeffs (x + 1)
    where normal_coeffs = transform coeffs

horner :: [Int] -> Int -> [Int]
horner coeffs point = tail $ scanl (\acc x -> acc * point + x) 0 coeffs

compare_coeffs :: [Int] -> Bool
compare_coeffs horner_coeffs = (head horner_coeffs) >= 0 && (all (>0) $ tail horner_coeffs)

transform :: [Int] -> [Int]
transform coeffs = [((-1)^i)*coeff | (i, coeff) <- zip [0..length coeffs] coeffs]
