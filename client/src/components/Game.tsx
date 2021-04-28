import * as React from 'react'
import styled from 'styled-components'

type LayoutProps = {
    gap: number,
}

const Row = styled.div<LayoutProps>`
display:flex;
flex-direction:row;
gap: ${(props) => props.gap}px
`;

const Column = styled.div<LayoutProps>`
display:flex;
flex-direction:column;
gap: ${(props) => props.gap}px
`;

function Game() {
    return (
        <Row gap={20}>
            <Column gap={20}>
                <div>Status</div>
                <Board />
            </Column>
            <Log />
        </Row>
    );
}

function Board() {
    return (
        <Column gap={0}>
            <Row gap={0}>
                <Square />
                <Square />
                <Square />
            </Row>
            <Row gap={0}>
                <Square />
                <Square />
                <Square />
            </Row>
            <Row gap={0}>
                <Square />
                <Square />
                <Square />
            </Row>
        </Column>
    );
}

const StyledSquare = styled.button`
    width:34px;
    height: 34px;
    background: #fff;
    border: 1px solid #999;
    padding:0;
    font-size:24px;
    font-weight:bold;
`;
function Square() {
    return (
        <StyledSquare>
            X
        </StyledSquare>
    )
}
function Log() {
    return (
        <ol>
            <li><button>Go To Move</button></li>
        </ol>
    );
}

export default Game;