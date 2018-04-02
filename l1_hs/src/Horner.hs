module Horner where

upperBorder :: [Double] -> Double -> Double
upperBorder coeffs step
    | compare_coeffs $ horner coeffs step = step
    | otherwise = upperBorder coeffs (step + 1)

lowerBorder :: [Double] -> Double -> Double
lowerBorder coeffs step
    | compare_coeffs $ horner normal_coeffs step = negate step
    | otherwise = lowerBorder normal_coeffs (step + 1)
    where normal_coeffs = transform coeffs

horner :: [Double] -> Double -> [Double]
horner coeffs point = tail $ scanl (\acc x -> acc * point + x) 0 coeffs

compare_coeffs :: [Double] -> Bool
compare_coeffs horner_coeffs = (head horner_coeffs) >= 0 && (all (>0) $ tail horner_coeffs)

transform :: [Double] -> [Double]
transform coeffs = [((-1)^i)*coeff | (i, coeff) <- zip [0..length coeffs] coeffs]
