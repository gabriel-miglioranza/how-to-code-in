-- Integral can receive Int and Integer types
lucky :: (Integral a) => a -> String
lucky 7 = "Lucky Number SEVEN!"
lucky x = "Sorry, you're out of luck, pal!"

sayMe :: (Integral a) => a -> String
sayMe 1 = "One"
sayMe 2 = "Two"
sayMe 3 = "Three"
sayMe 4 = "Four"
sayMe 5 = "Five"
sayMe x = "Not between 1 and 5"

-- implementing the recursive factorial function
factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n*factorial(n-1)

addVectors :: (Num a) => (a, a) -> (a, a) -> (a, a)
addVectors (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)


capital :: String -> String
capital "" = "Empty string, whoops!"
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]

-- guards
maxValue :: (Ord a) => a -> a -> a
maxValue a b
        | a > b     = a
        | otherwise = b

-- where

bmiTell :: (RealFloat a) => a -> a -> String
bmiTell weight height
    | bmi <= skinny = "You're underweight."
    | bmi <= normal = "You're supposedly normal."
    | bmi <= fat    = "You're overweight."
    | otherwise = "Go see a doctor."
    where bmi = weight / height ^ 2
          (skinny, normal, fat) = (18.5, 25, 30)

-- let in

cylinderArea :: (RealFloat a) => a -> a -> a
cylinderArea r h = 
    let sideArea = 2 * pi * r * h
        topArea = pi * r^2
    in sideArea + 2 * topArea