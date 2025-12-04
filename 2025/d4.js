const fs = require('fs'); 


const filename = 'input'; 

const filedata = fs.readFileSync(filename, 'utf-8'); 
const lines = filedata.split('\n'); 

const grid = []; 

for (const l of lines) {
    grid.push(l.split('')); 
}

let goodCount = 0; 
let visited = new Set(); 
let goodLocs = new Set(); 

function validIndex(grid, row, col) {
    const result = 
        row > -1 && col > -1 && row < grid.length && col < grid[0].length; 
    return result; 
}

function goodLoc(grid, row, col) {
    if (grid[row][col] !== '@') {
        return false; 
    }


    const directions = [
        [row + 1, col],
        [row + 1, col + 1],
        [row + 1, col - 1],
        [row, col + 1],
        [row, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row - 1, col - 1],
    ]; 

    let rollCount = 0; 

    for (const [r, c] of directions) {
        if (!validIndex(grid, r, c)) {
            continue; 
        }
        
        if (grid[r][c] === '@') {
            rollCount += 1; 

            if (rollCount >= 4) {
                return false; 
            }
        }
    }

    return true; 
}


function dfs(grid, row, col) {
    if (!validIndex(grid, row, col)) {
        return;
    }

    const key = row + ":" + col; 
    if (visited.has(key)) {
        return;
    }

    visited.add(key); 
    
    if (goodLoc(grid, row, col)) {
        goodCount += 1;
        goodLocs.add(key); 
    }

    const directions = [
        [row + 1, col], 
        [row - 1, col], 
        [row, col + 1], 
        [row, col - 1], 
    ]

    for (const [r, c] of directions) {
        dfs(grid, r, c); 
    }
}

let startingGoodCount = Infinity; 
do {
    startingGoodCount = goodCount; 
    dfs(grid, 0, 0); 

    for (const k of goodLocs) {
        let [r, c] = k.split(':'); 
        r = parseInt(r); 
        c = parseInt(c); 
        grid[r][c] = 'x'; 
    }

    visited = new Set(); 
    goodLocs = new Set(); 

} while (goodCount !== startingGoodCount); 


console.log(goodCount); 

// const fs = require('fs'); 


// const filename = 'input'; 

// const filedata = fs.readFileSync(filename, 'utf-8'); 
// const lines = filedata.split('\n'); 

// const grid = []; 

// for (const l of lines) {
//     grid.push(l.split('')); 
// }

// let goodCount = 0; 
// const visited = new Set(); 

// function validIndex(grid, row, col) {
//     const result = 
//         row > -1 && col > -1 && row < grid.length && col < grid[0].length; 
//     return result; 
// }

// function goodLoc(grid, row, col) {
//     const directions = [
//         [row + 1, col],
//         [row + 1, col + 1],
//         [row + 1, col - 1],
//         [row, col + 1],
//         [row, col - 1],
//         [row - 1, col],
//         [row - 1, col + 1],
//         [row - 1, col - 1],
//     ]; 

//     let rollCount = 0; 

//     for (const [r, c] of directions) {
//         if (!validIndex(grid, r, c)) {
//             continue; 
//         }
        
//         if (grid[r][c] === '@') {
//             rollCount += 1; 

//             if (rollCount >= 4) {
//                 return false; 
//             }
//         }
//     }

//     return true; 
// }


// function dfs(grid, row, col) {
//     if (!validIndex(grid, row, col)) {
//         return;
//     }

//     const key = row + ":" + col; 
//     if (visited.has(key)) {
//         return;
//     }

//     visited.add(key); 
    
//     if (grid[row][col] === '@') {
//         goodCount += goodLoc(grid, row, col); 
//     }

//     const directions = [
//         [row + 1, col], 
//         [row - 1, col], 
//         [row, col + 1], 
//         [row, col - 1], 
//     ]

//     for (const [r, c] of directions) {
//         dfs(grid, r, c); 
//     }
// }

// dfs(grid, 0, 0); 
// console.log(goodCount); 

