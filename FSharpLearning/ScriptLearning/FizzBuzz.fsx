
let isWordModulo modulus (word:string) (x, s) =
    match x % modulus = 0 with
    | true -> (x, $"{s}{word}")
    | false -> (x, s)

let isFizz = isWordModulo 3 "Fizz"
let isBuzz = isWordModulo 5 "Buzz"

let fillBlanks (x,s) =
    match s with
    | "" -> (x,$"{x}")
    | _ -> (x, s)

let FizzBuzz nums = 
    nums 
    |> List.map isFizz
    |> List.map isBuzz
    |> List.map fillBlanks
    |> List.map (fun (x,s) -> s)

let nums = [for i in [1..50] -> (i, "")]

let result = FizzBuzz nums 

printf "%A" result