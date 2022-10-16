
let isWordModulo (m: int) (word:string) (n, s) =
    match n % m = 0 with
    | true -> (n, $"{s}{word}")
    | false -> (n, s)

let isFizz = isWordModulo 3 "Fizz"
let isBuzz = isWordModulo 5 "Buzz"

let fillBlanks (n,s) =
    match s with
    | "" -> (n,$"{n}")
    | _ -> (n, s)

let FizzBuzz nums = 
    nums 
    |> List.map isFizz
    |> List.map isBuzz
    |> List.map fillBlanks
    |> List.map (fun (n,s) -> s)

let nums = [for i in [1..50] -> (i, "")]

let result = FizzBuzz nums 

printf "%A" result