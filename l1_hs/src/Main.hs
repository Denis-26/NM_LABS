module Main where

import qualified Horner as H
import qualified RootSeparation as R
import qualified TangentMethod as T
import qualified ChordMethod as C
import qualified CombineMethod as Co

main :: IO ()
main = do
    let
        coeffs = [1, 0, -6, 2]
        step = 1
        acc = 0.001

        f x = x^3 - 6*x + 2
        f' x = 3*x^2 - 6
        f'' x = 6*x

        upperBorder = H.upperBorder coeffs step
        lowerBorder = H.lowerBorder coeffs step

        separated_roots = R.separate coeffs (lowerBorder, upperBorder)

        tngMethodResult = map (\(a,b) -> T.tangentMethod f f' f'' acc (a, b)) separated_roots
        chordMethodResult = map (\(a,b) -> C.chordMethod f f' f'' acc (a, b)) separated_roots
        combineMethodResult = map (\(a,b) -> Co.combineMethod f f' f'' acc (a, b)) separated_roots

    print tngMethodResult
    print chordMethodResult
    print combineMethodResult
