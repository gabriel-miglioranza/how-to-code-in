multThree :: (Num a) => a -> a -> a-> a
multThree x y z = x * y * z

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

square :: (Num a) => a -> a
square x = x^2

-- maps
-- map apply a defined function in every element of a list
oneToTen = [1..10]
-- square every element and return a list as a result
sOneToTen = map square oneToTen
-- filter
-- filter some list using a bool expression
isGreaterThan50 x = x > 50

filteredSquares = filter isGreaterThan50 sOneToTen

-- lambda
-- filtering and mapping with lambda
lOneToTen = map (\x -> x^2) oneToTen
lFilteredSquares = filter (\x -> x > 50) lOneToTen