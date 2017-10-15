import qualified Horner as H
import qualified RootSeparation as R

main = do
    print $ H.upperBorder [2, -4, 5, -2] 1
    print $ H.lowerBorder [2, -4, 5, -2] 1
    print $ R.separate [1, 0, -6, 2] [3, 0, 1, 0] (-3, 3)
