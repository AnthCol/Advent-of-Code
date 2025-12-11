const fs = require('fs'); 

const filename = 'input'; 

const filedata = fs.readFileSync(filename, 'utf-8'); 

const lines = filedata.split('\n'); 

const grid = []; 

for (const l of lines) {
    grid.push(l.split('')); 
}



let maxlen = 0; 

for (const g of grid) {
    maxlen = Math.max(maxlen, g.length); 
}

maxlen += 1; 

// pad the data
for (let i = 0; i < grid.length; i++) {
    while (grid[i].length !== maxlen) {
        grid[i].push(' '); 
    }
}


let chunk = []; 
let sum = 0; 

for (let i = 0; i < grid[0].length; i++) {
    let allBlank = true; 

    for (let j = 0; j < grid.length; j++) {
        if (grid[j][i] !== ' ') {
            allBlank = false;
            break;
        }
    }

    if (!allBlank) {
        for (let j = 0; j < grid.length; j++) {
            if (chunk[j] === undefined) {
                chunk[j] = []; 
            }
            chunk[j].push(grid[j][i]); 
        }
    } else {
        // process the chunk here. 
        const rows = chunk.length; 
        const columns = chunk[0].length; 
    
        const values = [];         


        for (let k = 0; k < columns; k++) {
            let val = ''; 

            for (let l = 0; l < rows - 1; l++) {
                val += chunk[l][k]; 
            }

            values.push(parseInt(val)); 
        }
    
        let operation = null; 

        for (let k = 0; k < columns; k++) {
            if (chunk[rows - 1][k] !== ' ') {
                operation = chunk[rows - 1][k]; 
                break;
            }
        }

        let total = values[0]; 
        for (let k = 1; k < values.length; k++) {
            if (operation === '+') {
                total += values[k]; 
            } else {
                total *= values[k]; 
            }
        }

        sum += total; 

        chunk = []; 
    }
}

console.log(sum); 



// const fs = require('fs'); 

// const filename = 'input'; 

// const filedata = fs.readFileSync(filename, 'utf-8'); 

// const lines = filedata.split('\n'); 

// const grid = []; 

// for (const l of lines) {
//     grid.push(l.trim().split(/\s+/)); 
// }

// console.log(JSON.stringify(grid)); 

// let sum = 0; 
// for (let i = 0; i < grid[0].length; i++) {

//     const operation = grid[grid.length - 1][i]; 

//     const values = []; 

//     for (let j = 0; j < grid.length - 1; j++) {
//         values.push(grid[j][i]); 
//     }

//     let calculation = parseInt(values[0]); 

//     for (let j = 1; j < values.length; j++) {
//         if (operation === '+') {
//             calculation += parseInt(values[j]); 
//         } else {
//             calculation *= parseInt(values[j]); 
//         }
//     }


//     sum += calculation; 
// }

// console.log(sum); 