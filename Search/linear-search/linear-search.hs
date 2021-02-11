linear_search [] _ = False
linear_search (x:xs) y
    | x == y = True
    | otherwise = linear_search xs y

main = do
    _ <- getLine
    numbers_str <- getLine
    let numbers = [ read x::Int | x <- words numbers_str]
    targets_str <- getLine
    let targets = [ read x::Int | x <- words targets_str]
    
    let search_results = [ linear_search numbers x | x <- targets]
    print search_results
