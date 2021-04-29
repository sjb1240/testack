import { link } from 'node:fs';
import * as React from 'react'
import { Board } from './BoardProps';
import { GameState, useGameState } from './GameState';
import { Row, Column } from './LayoutProps';
import { Log } from './LogProps';

function Game() {
    const {
        gameState,
        current,
        xIsNext,
        jumpTo,
        winner,
        handleClick,
    } = useGameState();
    return (
        <Row gap={20}>
            <Column gap={20}>
                <div>{
                    winner ? `Winner ${winner}` : `Next Player ${xIsNext ? 'X' : 'O'}`
                }</div>
                <Board board={current} onClick={handleClick} rows={3} cols={3} />
            </Column>
            <Log history={gameState.history} jumpTo={jumpTo} />
            <Column gap={50}>
                <button>New Row</button>
                <button>New Col</button>
            </Column>
        </Row>
    );
}
export default Game;