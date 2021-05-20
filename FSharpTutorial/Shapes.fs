namespace Shapes
open System

module AreaCalculation =

    let rect h w =
        h * w

    let square h =
        rect h h

    let circle r =
        r
        |> (*) r
        |> (*) Math.PI 