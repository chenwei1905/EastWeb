import React from "react";
import ReactDOM from "react-dom";
import Board from "./Board";

export default function() {
    return (
        <div>
            <Board knightPosition={[0, 1]} />
            <Board knightPosition={[0, 2]} />
            <Board knightPosition={[0, 3]} />
            <Board knightPosition={[0, 4]} />
            <Board knightPosition={[0, 5]} />
            <Board knightPosition={[0, 6]} />
            <Board knightPosition={[0, 7]} />
            <Board knightPosition={[0, 8]} />
        </div>
    );
}
