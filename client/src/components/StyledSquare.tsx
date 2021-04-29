import { RecordWithTtl } from 'node:dns';
import * as React from 'react';
import styled from 'styled-components';
import { Value } from './GameState';

const StyledSquare = styled.button`
    width:34px;
    height: 34px;
    background: #fff;
    border: 1px solid #999;
    padding:0;
    font-size:24px;
    font-weight:bold;
`;
export type SquareProps = {
    value: Value;
    pos: Array<Number>;
    onClick: () => void;
};
export function Square(props: SquareProps) {
    return (
        <StyledSquare onClick={props.onClick}>
            {props.pos[0]},{props.pos[1]}
        </StyledSquare>
    );
}
