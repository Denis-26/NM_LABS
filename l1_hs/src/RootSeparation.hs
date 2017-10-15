module RootSeparation where
import qualified Horner as H

pairs :: [Int] -> [(Int, Int)]
pairs array = zip array $ tail array

polinom_values_pairs :: [Int] -> (Int, Int) -> [(Int, Int)]
polinom_values_pairs coeffs (x1, x2) = pairs [last $ H.horner coeffs x | x <- [x1..x2]]

intervals :: [(Int, Int)] -> (Int, Int) -> [((Int, Int), (Int, Int))]
intervals values (x1, x2) = filter (\( (x1, x2), (y1, y2) ) -> x1 * x2 < 0) $ zip values $ pairs [x1..x2]

separate :: [Int] -> (Int, Int) -> [(Int, Int)]
separate coeffs (x1, x2) =  map (\((x1, x2), (y1, y2)) -> (y1, y2)) $ intervals (polinom_values_pairs coeffs (x1, x2)) (x1, x2)
