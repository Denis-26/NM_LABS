module RootSeparation where

polinom_in_point :: [Int] -> Int -> Int
polinom_in_point coeffs point = sum [ (coeffs !! (length coeffs - x - 1)) * (point ^ x) | x <- reverse [0..length coeffs-1] ]

pairs :: [Int] -> [(Int, Int)]
pairs array = zip array $ tail array

polinom_values_pairs :: [Int] -> (Int, Int) -> [(Int, Int)]
polinom_values_pairs coeffs (x1, x2) = pairs [polinom_in_point coeffs x | x <- [x1..x2]]

intervals :: [(Int, Int)] -> (Int, Int) -> [((Int, Int), (Int, Int))]
intervals values (x1, x2) = filter (\( (x1, x2), (y1, y2) ) -> x1 * x2 < 0) ints
    where ints = zip values $ pairs [x1..x2]

separate :: [Int] -> (Int, Int) -> [(Int, Int)]
separate coeffs (x1, x2) =  map (\((x1, x2), (y1, y2)) -> (y1, y2)) $ intervals (polinom_values_pairs coeffs (x1, x2)) (x1, x2)
