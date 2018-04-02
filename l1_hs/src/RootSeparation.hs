module RootSeparation where
import qualified Horner as H

pairs :: [Double] -> [(Double, Double)]
pairs array = zip array $ tail array

polinom_values_pairs :: [Double] -> (Double, Double) -> [(Double, Double)]
polinom_values_pairs coeffs (x1, x2) = pairs [last $ H.horner coeffs x | x <- [x1..x2]]

diff_sign :: Double -> Double -> Bool
diff_sign x1 x2
    | x1 * x2 /= 0 = x1 * x2 < 0
    | otherwise = x1 < 0 || x2 < 0

intervals :: [(Double, Double)] -> (Double, Double) -> [((Double, Double), (Double, Double))]
intervals values (x1, x2) = filter (\( (x1, x2), (y1, y2) ) -> diff_sign x1 x2) $ zip values $ pairs [x1..x2]

separate :: [Double] -> (Double, Double) -> [(Double, Double)]
separate coeffs (x1, x2) =  map (\((x1, x2), (y1, y2)) -> (y1, y2)) $ intervals (polinom_values_pairs coeffs (x1, x2)) (x1, x2)
