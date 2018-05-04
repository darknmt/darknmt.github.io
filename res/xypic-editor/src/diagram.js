import {h, render, Diagram, Node, Edge} from 'jsx-tikzcd'
import * as helper from './helper'

export function toJSON(diagram) {
    let leftTop = [0, 1].map(i => diagram.nodes.reduce(
        (min, node) => Math.min(min, node.position[i]),
        Infinity
    ))

    return JSON.stringify({
        nodes: diagram.nodes.map(node => ({
            ...node,
            id: undefined,
            position: node.position.map((x, i) => x - leftTop[i])
        })),

        edges: diagram.edges.map(edge => ({
            ...edge,
            from: diagram.nodes.findIndex(node => node.id === edge.from),
            to: diagram.nodes.findIndex(node => node.id === edge.to)
        }))
    })
}

export function fromJSON(json) {
    let obj = JSON.parse(json)
    let nodes = obj.nodes.map(node => ({
        ...node,
        id: helper.getId()
    }))

    return {
        nodes,
        edges: obj.edges.map(edge => ({
            ...edge,
            from: nodes[edge.from].id,
            to: nodes[edge.to].id
        }))
    }
}

export function toBase64(diagram) {
    return btoa(toJSON(diagram))
}

export function fromBase64(base64) {
    return fromJSON(atob(base64))
}

export function toTeX(diagram) {
    return render(
        <Diagram>
            {diagram.nodes.map((node, i) =>
                <Node
                    key={node.id}
                    position={node.position}
                    value={node.value}
                />
            )}

            {diagram.edges.map(edge => [
                <Edge
                    from={edge.from}
                    to={edge.to}
                    value={edge.value}
                    labelPosition={edge.labelPosition}
                    args={[
                        ...[edge.tail, edge.line, edge.head].map((id, i) => ({
                            none: ['', '-', ''][i],
                            default: ['', '-', '>'][i],
                            null: ['', '-', '>'][i],                            
                            undefined: ['', '-', '>'][i],
                            harpoon: '^>',
                            harpoonalt: "_>'",
                            hook: '^{(}',
                            hookalt: "_{(}",
                            mapsto: '|',
                            tail: ')',
                            twoheads: '>>',
                            dashed: '--',
                            dotted: '.',
                            solid: '-',
                            double: '='
                        })[id]),
                    ].filter(x => x != null)}
                    xybend={
                        edge.bend > 0 ? `@/^${ {30: '', 49: '1pc', 60: '1.5pc', 67: '2pc', 71: '2.5pc', 74: '3pc', 76: '3.5pc' , 78: '4pc', 79: '4.5pc', 80: '5pc'}[edge.bend]}/`
                        : edge.bend < 0 ? `@/_${ {30: '', 49: '1pc', 60: '1.5pc', 67: '2pc', 71: '2.5pc', 74: '3pc', 76: '3.5pc' , 78: '4pc', 79: '4.5pc', 80: '5pc'}[-edge.bend]}/`
                        : ''
                    }

                />
            ])}
        </Diagram>
    )
}
