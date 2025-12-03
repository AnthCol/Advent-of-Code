
const fs = require('fs'); 

const filename = 'input'; 

const filedata = fs.readFileSync(filename, 'utf-8'); 

const lines = filedata.split('\n')

let sum = 0; 


for (const l of lines) {

    const stack = [l[0]]; 

    for (let i = 1; i < l.length; i++) {
        const c = l[i]; 
       
        if (c > stack.at(-1)) {
            const amountLeft = l.length - i - 1;
            while(stack.at(-1) < c) {
                if (amountLeft + stack.length < 12) {
                    break;
                } 
                stack.pop(); 
            }
            stack.push(c); 
        } else if (stack.length !== 12) {
            stack.push(c); 
        }
    }

    const val = parseInt(stack.join('')); 

    sum += val; 
}

console.log(sum); 






// const fs = require('fs'); 

// const filename = 'input'; 

// const filedata = fs.readFileSync(filename, 'utf-8'); 

// const lines = filedata.split('\n')

// let sum = 0; 


// for (const l of lines) {
//     let firstNum = 0; 
//     let max = 0; 
//     for (let i = 0; i < l.length; i++) {
//         const c = parseInt(l[i]); 
        
//         if (i + 1 !== l.length && c > firstNum) {
//             firstNum = c; 
//         } else if (firstNum * 10 + c > max) {
//             max = firstNum * 10 + c; 
//         }
//     }

//     sum += max; 
// }


// console.log(sum); 

