open SimpleMath
open Shapes
open Option
open FSharp.Numerics

[<EntryPoint>]
let main argv =

    let twotimesnine = multiply9 2
    printfn $"{twotimesnine}"

    let sidelength = 5
    let area = AreaCalculation.square sidelength
    printfn $"area of a square with length side %d{sidelength} %d{area}"

    let x = 5
    let p = 3
    let multiply5with3topowerof = multiply3ToPowerOf 5
    let result = multiply5with3topowerof p
    printfn $"{x} multiply3topowerof {p} = {result}"

    printFuncResult multiply9 9 |> ignore

    0 //Return from main
