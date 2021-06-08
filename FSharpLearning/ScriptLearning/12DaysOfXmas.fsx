
type DayAndGift = {Day: string; Gift: string}

let daysAndGifts = [
    { Day = "First"; Gift = "A partridge in a pear tree"}
    { Day = "Second"; Gift = "Two turtle doves"}
    { Day = "Third"; Gift = "Three french hens"}
    { Day = "Fourth"; Gift = "Four calling birds"}
    { Day = "Fifth"; Gift = "Five golden rings"}
    { Day = "Sixth"; Gift = "Six geese a-laying"}
    { Day = "Seventh"; Gift = "Seven swans a-swimming"}
    { Day = "Eigth"; Gift = "Eight maids a-milking"}
    { Day = "Ninth"; Gift = "Nine ladies dancing"}
    { Day = "Tenth"; Gift = "Ten lords a-leaping"}
    { Day = "Eleventh"; Gift = "Eleven pipers piping"}
    { Day = "Twelth"; Gift = "Twelve drummers drumming"}
]

let rec printAccumulatedGifts (gifts: string List) =
    match gifts.Length with
        | 0 -> ()
        | 1 ->
            printfn $"{gifts.Head}"
            printAccumulatedGifts gifts.Tail
        | 2 ->
            printfn $"{gifts.Head} and"
            printAccumulatedGifts gifts.Tail
        | _ -> 
            printfn $"{gifts.Head},"
            printAccumulatedGifts gifts.Tail

let rec printSongWithAccumulatedGifts (accumulatedGifts: string List) (daysAndGifts: DayAndGift List) =
    match daysAndGifts.Length > 0 with
        | true ->
            printfn "On the %s day of Christmas" daysAndGifts.Head.Day
            printfn "My true love gave to me:"
            let moreAccumulatedGifts = (daysAndGifts.Head.Gift :: accumulatedGifts)
            printAccumulatedGifts moreAccumulatedGifts
            printfn ""
            printSongWithAccumulatedGifts moreAccumulatedGifts daysAndGifts.Tail
        | false -> ()

let printSong = printSongWithAccumulatedGifts []

printSong daysAndGifts