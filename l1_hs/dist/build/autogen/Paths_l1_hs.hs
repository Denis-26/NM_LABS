module Paths_l1_hs (
    version,
    getBinDir, getLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/home/denis/.cabal/bin"
libdir     = "/home/denis/.cabal/lib/x86_64-linux-ghc-7.10.3/l1-hs-0.1.0.0-IBKPPhT9CblJ6vROVONDAz"
datadir    = "/home/denis/.cabal/share/x86_64-linux-ghc-7.10.3/l1-hs-0.1.0.0"
libexecdir = "/home/denis/.cabal/libexec"
sysconfdir = "/home/denis/.cabal/etc"

getBinDir, getLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "l1_hs_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "l1_hs_libdir") (\_ -> return libdir)
getDataDir = catchIO (getEnv "l1_hs_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "l1_hs_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "l1_hs_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
