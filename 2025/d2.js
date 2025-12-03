const fs = require('fs'); 

const filename = 'input'; 

const filedata = fs.readFileSync(filename, 'utf-8'); 

const data = filedata.split(','); 

let sum = 0; 

for (const d of data) {
    let [start, end] = d.split('-'); 

    start = parseInt(start); 
    end = parseInt(end); 

    for (let i = start; i <= end; i++) {
        const val = String(i); 

        for (let j = 1; j < val.length; j++) {
            const needle = val.slice(0, j); 
    
            if (val.length % needle.length !== 0) {
                continue; 
            }

            let builtString = needle; 

            while (builtString.length < val.length) {
                builtString += needle; 
            }

            if (builtString === val) {
                sum += i; 
                break; 
            }
        }
    }
}

console.log(sum); 





// const fs = require('fs'); 

// const filename = 'input'; 

// const filedata = fs.readFileSync(filename, 'utf-8'); 

// const data = filedata.split(','); 

// let sum = 0; 

// for (const d of data) {
//     let [start, end] = d.split('-'); 

//     start = parseInt(start); 
//     end = parseInt(end); 

//     for (let i = start; i <= end; i++) {
//         const val = String(i); 

//         for (let j = 0; j < val.length; j++) {
//             const needle = val.slice(0, j); 
//             const haystack = val.slice(j); 

//             if (needle === haystack) {
//                 sum += parseInt(i); 
//                 break;
//             }
//         }
//     }
// }

// console.log(sum); 

