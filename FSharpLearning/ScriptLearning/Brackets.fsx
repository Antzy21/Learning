open System

let numberString = "135782904"

// Goal -> (1((3((5((7(8))))))2(((((((9)))))))))0((((4))))

// ToDo: Should check for valid numeric string input
let rec getIntList numberString =
    match numberString with
    | [] -> []
    | _ -> Int32.Parse $"{numberString.Head}" :: getIntList numberString.Tail

let convertToIntList (numberString : string) =
    numberString
    // Put .ToCharArray as pipe somehow?
    //|> String.ToCharArray
    |> Seq.iter (fun c -> c)
    |> Array.toList
    |> getIntList

let bracketStringBetweenInts preInt postInt =
    match (preInt < postInt) with
    | true -> String.replicate (postInt - preInt) "("
    | false -> String.replicate (preInt - postInt) ")"

let rec placeBrackets (intList: int List) accumulatingString =
    match intList.Length with
    | 0 -> accumulatingString
    | 1 -> 
        let brackets = bracketStringBetweenInts intList.Head 0
        let newAccumulatingString = $"{accumulatingString}{brackets}"
        placeBrackets intList.Tail newAccumulatingString
    | _ -> 
        let brackets = bracketStringBetweenInts intList.Head intList.Tail.Head
        printfn $"{brackets}"
        let newAccumulatingString = $"{accumulatingString}{brackets}{intList.Tail.Head}"
        placeBrackets intList.Tail newAccumulatingString

let brackifyString numberString = 
    // Include 0 as to not miss the first digit
    let intList = 0 :: convertToIntList numberString
    placeBrackets intList ""


let result = brackifyString numberString
printfn $"{result}"
