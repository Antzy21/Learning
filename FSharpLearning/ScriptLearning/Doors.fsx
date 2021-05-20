

let toggleDoorsModulo m doors =
    doors
    |> List.map (fun (n, d) ->
        match n % m with 
        | 0 -> (n, not d)
        | _ -> (n, d)
    )

let rec toggleDoors doors i =
    match i with
    | 0 -> doors
    | _ -> toggleDoors (toggleDoorsModulo i doors) (i-1)

let doors = [for i in 1..100 -> (i, false)]

let toggledDoors = toggleDoors doors 100   

printf "%A" toggledDoors