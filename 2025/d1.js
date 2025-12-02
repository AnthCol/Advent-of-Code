const fs = require('fs'); 
const filename = 'input'; 
const filedata = fs.readFileSync(filename, 'utf-8'); 

const lines = filedata.split('\n');

let counter = 0; 
let position = 50; 

for (const l of lines) {
    const command = l[0]; 
    const value = parseInt(l.slice(1)); 

    for (let i = 0; i < value; i++) {
        if (command === 'L') {
            position = (position - 1) % 100; 
        } else {
            position = (position + 1) % 100; 
        }

        counter += position === 0; 
    }
}

console.log(counter); 

// const fs = require('fs'); 
// const filename = 'input'; 
// const filedata = fs.readFileSync(filename, 'utf-8'); 

// const lines = filedata.split('\n');

// let counter = 0; 
// let position = 50; 

// for (const l of lines) {
//     const command = l[0]; 
//     const value = parseInt(l.slice(1)); 

//     if (command === 'L') {
//         position = (position - value) % 100; 
//     } else {
//         position = (position + value) % 100; 
//     }

//     counter += position === 0; 
// }

// console.log(counter); 
