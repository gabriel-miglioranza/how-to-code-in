-- first doc in haskell

doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe y

numbers = [1,2,3,4,5]
concatList = [1,2,3,4] ++ [2,3,6]
-- result [1,2,3,4,2,3,6]
concatNumberList = 1:2:3:[]
-- result [1,2,3]
numbersHead = head numbers
numbersTail = tail numbers
numbersLast = last numbers
numbersInit = init numbers
numbersLength = length numbers 
isNumbersNull = null numbers
reverseNumbers = reverse numbers
takeFirst3Numbers = take 3 numbers
dropLast3Numbers = drop 3 numbers
greastestNumber = maximum numbers
smallestNumber = minimum numbers
sumNumbers = sum numbers
productNumbers = product numbers
forthElement = 4 `elem` numbers

-- texas ranges -- 
oneToTen = [1..10]
aToz = ['a'..'z']
-- cycle is a infinite cycle
infiniteCycle = cycle [0,1]
-- slice with take
slicedCycle = take 10 (infiniteCycle)

-- repeat ad infinitum
repeat5 = repeat 5
-- sliced result
slicedRepeat = take 10 (repeat5)


-- lists comprehension --

-- 1 to 10 squared

oneToTenSquared = [x^2 | x <- [1..10]]
oneToTenSquaredVar = [x^2 | x <- oneToTen]

-- x*2, with x from 0 to 20 and x*2 > 12
thisWeirdList = [x^2 | x <-[0..20], x^2 > 12] 

-- tuples --
aPair = ("first", "second")
aTuple = (1,2,5,6,"name",3.22)
firstElement = fst aPair
secondElement = snd aPair

-- zip to lists
oneToFive = [1..5]
wOneToFive = ["one", "two", "three", "four", "five"]
resultList = zip oneToFive wOneToFive

-- zip into a infinite list
aInfiniteList = [1..]
animals = ["dog", "cat", "mouse", "bird"]
fruits = ["apple", "banana", "orange"]
indexedAnimals = zip aInfiniteList animals
indexedFruits = zip aInfiniteList fruits

-- a set of right triangles (a, b, c)
rightTriangles = [(a, b, c) | c <- [1..10], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2]