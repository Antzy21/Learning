module SimpleMath

let multiply3 n =
    n*3

let multiply3' =
    (*) 3

let multiply9 n =
    n
    |> multiply3
    |> multiply3'

let rec doIntFuncNtimes (f: int -> int) (x: int) (n: int) =
    if n = 0 then
        x
    else
        let x' = f x
        let n' = n-1
        doIntFuncNtimes f x' n'
        
let multiply3NTimes = doIntFuncNtimes multiply3 

let multiply3ToPowerOf n p =
    multiply3NTimes n p

let printFuncResult (f: int -> 'a) x : 'a =
    let result = f x
    printfn $"Result of function on {x} is {result}"
    result


type MyDiscUnion =
    | One
    | Two
    | Three