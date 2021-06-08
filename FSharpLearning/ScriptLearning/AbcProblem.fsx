open System

//http://rosettacode.org/wiki/ABC_problem

type Block = {L1: Char; L2: Char}

let blockContainsChar character block =
    character = block.L1 || character = block.L2

let searchAvailableBlocksForChar character (availableBlocks: Block list) : Block Option =
    let blocksWithChar = availableBlocks |> List.filter (blockContainsChar character)
    match blocksWithChar.IsEmpty with
        | false -> Some(blocksWithChar.Head)
        | true -> None

let rec indexRemove i list =
    match i, list with
    | 0, x::xs -> xs
    | i, x::xs -> x::indexRemove (i - 1) xs
    | i, [] -> failwith "index out of range"

let removeSingleItemFromList item list =
    indexRemove (list |> List.findIndex (fun i -> i = item)) list

let removeFirstElement array =
   Array.sub array 1 (array.Length-1)

let rec tryNewBlock (requiredCharacters:char[]) (availableBlocks: Block list) =
    match requiredCharacters.Length with
    | 0 -> true
    | _ -> ( match availableBlocks.Length with
            | 0 -> false
            | _ -> (
                    let nextChar = requiredCharacters.[0]
                    match searchAvailableBlocksForChar nextChar availableBlocks with 
                    | None -> false //Try More
                    | Some(block) -> 
                        let newRequiredChars = removeFirstElement requiredCharacters
                        let newAvailableBlocks = removeSingleItemFromList block availableBlocks
                        tryNewBlock newRequiredChars newAvailableBlocks
            )
    )

let canMakeWord (word:string) availableBlocks = 
    let characters = word.ToUpper().ToCharArray()
    let result = tryNewBlock characters availableBlocks  
    match result with
    | true -> printfn $"Able to create '{word}' with the available blocks"
    | false -> printfn $"Unable to create '{word}' with the available blocks"
    result

let blocks = [
    { L1 = 'B'; L2 = 'O' }
    { L1 = 'X'; L2 = 'K' }
    { L1 = 'D'; L2 = 'Q' }
    { L1 = 'C'; L2 = 'P' }
    { L1 = 'N'; L2 = 'A' }
    { L1 = 'G'; L2 = 'T' }
    { L1 = 'R'; L2 = 'E' }
    { L1 = 'T'; L2 = 'G' }
    { L1 = 'Q'; L2 = 'D' }
    { L1 = 'F'; L2 = 'S' }
    { L1 = 'J'; L2 = 'W' }
    { L1 = 'H'; L2 = 'U' }
    { L1 = 'V'; L2 = 'I' }
    { L1 = 'A'; L2 = 'N' }
    { L1 = 'O'; L2 = 'B' }
    { L1 = 'E'; L2 = 'R' }
    { L1 = 'F'; L2 = 'S' }
    { L1 = 'L'; L2 = 'Y' }
    { L1 = 'P'; L2 = 'C' }
    { L1 = 'Z'; L2 = 'M' }
]

canMakeWord "Book" blocks
canMakeWord "Bark" blocks
canMakeWord "Treat" blocks
