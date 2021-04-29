import React, { Component } from 'react';
import { BoardState } from './GameState';
import { SquareProps, Square } from './StyledSquare';
import { Column, Row } from "./LayoutProps";

type BoardProps = {
    board: BoardState;
    rows: Array<Number>;
    cols: Array<Number>;
    onClick: (square: number) => void;
};
export function Board({ board, onClick, rows, cols }: BoardProps) {
    const createProps = (square: number): SquareProps => {
        return {
            value: board[square],
            onClick: () => onClick(square),
        };
    };
    // for (i = 0; i < rows.length(); i++) {
    //     for (int j = 0; j < cols.length(); j++) {
    //         console.log(i, j)
    //     }
    // }
    return (
        <Square pos={[0, 1]} {...createProps(0)} />
    )


    //     return (

    //         <Column gap={0}>
    //             <Row gap={0}>
    //                 <Square col={0} row={0} {...createProps(0)} />
    //                 <Square {...createProps(1)} />
    //                 <Square {...createProps(2)} />
    //             </Row>
    //             <Row gap={0}>
    //                 <Square {...createProps(3)} />
    //                 <Square {...createProps(4)} />
    //                 <Square {...createProps(5)} />
    //             </Row>
    //             <Row gap={0}>
    //                 <Square {...createProps(6)} />
    //                 <Square {...createProps(7)} />
    //                 <Square {...createProps(8)} />
    //             </Row>
    //         </Column>
    //     );
    // }



    // export default class Board extends Component {

    //     render() {
    //         return (
    //             <Column gap={0}>
    //                 <Row gap={0}>
    //                     <Square col={0} row={0} {...createProps(0)} />
    //                     <Square {...createProps(1)} />
    //                     <Square {...createProps(2)} />
    //                 </Row>
    //             </Column>
    //         )
    //     }
}